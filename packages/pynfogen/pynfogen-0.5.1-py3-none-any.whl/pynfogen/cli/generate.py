import os
from pathlib import Path
from typing import Optional

import click

from pynfogen.config import config, Files
from pynfogen.nfo import NFO


@click.command(context_settings=dict(default_map=config.get("generate", {})))
@click.argument("template", type=str)
@click.argument("file", type=str)
@click.option("-a", "--artwork", type=str, default=None, help="Artwork to use.")
@click.option("-s", "--season", type=str, default=None, help="TV Show Season Number (or name).")
@click.option("-e", "--episode", type=(int, str), default=(None, None), help="TV Show Episode Number and Title.")
@click.option("-imdb", type=str, default=None, help="IMDB ID (including 'tt').")
@click.option("-tmdb", type=str, default=None, help="TMDB ID (including 'tv/' or 'movie/').")
@click.option("-tvdb", type=int, default=None, help="TVDB ID ('73244' not 'the-office-us').")
@click.option("-S", "--source", type=str, default=None, help="Source information.")
@click.option("-N", "--note", type=str, default=None, help="Notes/special information.")
@click.option("-P", "--preview", type=str, default=None, help="Preview information, typically an URL.")
def generate(template: str, file: str, artwork: Optional[str], season: NFO.SEASON_T, episode: NFO.EPISODE_T,
             imdb: Optional[str], tmdb: Optional[str], tvdb: Optional[int], source: Optional[str], note: Optional[str],
             preview: Optional[str]) -> None:
    """
    Generate an NFO for a file.

    \b
    The content type is detected based on which values are set.
    - Movie: Neither -s nor -e is set.
    - Season: -s is set and -e is not.
    - Episode: -e is set. -s can be set or not though it's recommended.
    """
    if not os.path.exists(file):
        raise click.ClickException("The provided file or folder path does not exist.")

    if isinstance(season, str) and season.isdigit():
        season = int(season)

    nfo = NFO()
    nfo.set_config(
        str(Path(file).resolve()),
        season,
        episode,
        **dict(
            imdb=imdb,
            tmdb=tmdb,
            tvdb=tvdb,
            source=source,
            note=note,
            preview=preview,
            **config
        )
    )

    template_vars = {
        "videos_pretty": nfo.get_video_print(nfo.videos),
        "audio_pretty": nfo.get_audio_print(nfo.audio),
        "subtitles_pretty": nfo.get_subtitle_print(nfo.subtitles),
        "chapters_yes_no": nfo.get_chapter_print_short(nfo.chapters),
        "chapters_named": nfo.chapters and not nfo.chapters_numbered,
        "chapter_entries": nfo.get_chapter_print(nfo.chapters)
    }

    if artwork:
        artwork_path = Path(str(Files.artwork).format(name=artwork))
        if not artwork_path.exists():
            raise click.ClickException(f"No artwork named {artwork} exists.")
        artwork = artwork_path.read_text()

    template_path = Path(str(Files.template).format(name=template))
    if not template_path.exists():
        raise click.ClickException(f"No template named {template} exists.")
    template_data = template_path.read_text()

    nfo_txt = nfo.run(template_data, art=artwork, **template_vars)
    with open(os.path.join(os.path.dirname(nfo.file), f"{nfo.release_name}.nfo"), "wt", encoding="utf8") as f:
        f.write(nfo_txt)
    print(f"Generated NFO for {nfo.release_name}")

    description_path = Path(str(Files.description).format(name=template))
    if description_path.exists():
        description_data = description_path.read_text()
        bb_txt = nfo.run(description_data, art=None, **template_vars)
        with open(os.path.join(os.path.dirname(nfo.file), f"{nfo.release_name}.desc.txt"), "wt", encoding="utf8") as f:
            f.write(bb_txt)
        print(f"Generated BBCode Description for {nfo.release_name}")
