#!/usr/bin/env python
"""Simple podcast feed generator for directory of mp3 files

Generates an RSS feed containing entries for all mp3 files in a given
directory.
"""

import argparse
import datetime
from pathlib import Path

from feedgen.feed import FeedGenerator


def main():
    parser = argparse.ArgumentParser(description="Generate a podcast RSS feed for a directory of mp3 files.")
    parser.add_argument("--title", "-t", required=True, help="Podcast title")
    parser.add_argument("--description", "-d", help="Podcast description")
    parser.add_argument("--site", "-s", required=True, help="Root URL to base feed links on")
    parser.add_argument("--cover", "-c", help="Cover image file name")
    parser.add_argument("--path", "-p", default=".", help="Path containing source files")
    args = parser.parse_args()

    site = args.site
    if site[-1] == "/":
        site = site[:-1]

    fg = FeedGenerator()
    fg.title(args.title)
    if args.description:
        fg.description(args.description)
    if args.cover:
        fg.logo(f"{site}/{args.cover}")
    fg.link(href=f"{site}/podcast.xml", rel="self")
    fg.load_extension('podcast')

    now = datetime.datetime.now().astimezone(tz=datetime.timezone(datetime.timedelta(0)))
    for index, path in enumerate(sorted(Path(args.path).glob("*.mp3"))):
        fe = fg.add_entry()
        fe.id(path.stem)
        fe.title(f"Chapter {index:03d}")
        fe.description('...')
        # Step date forward to preserve order by date
        fe.published(now + datetime.timedelta(seconds=index))
        rel_path = path.relative_to(args.path)
        fe.enclosure(f"{site}/{rel_path}", str(path.stat().st_size), 'audio/mpeg')

    print(fg.rss_str(pretty=True))


if __name__ == "__main__":
    main()
