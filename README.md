# gen_feed

gen_feed.py is a script demonstrating how to use the [feedgen
library](https://github.com/lkiesow/python-feedgen) to generate a podcast RSS
feed from a directory of mp3 files.

## Requirements

* Python 3.6 or greater
* `pip install feedgen`

## Usage

All of the mp3 files and the cover image file (optional) should be in the same
directory. The feed will be ordered by sorting the mp3 file names
alphabetically.

Links in the RSS feed will all be made relative to the `--site` argument.

```
usage: gen_feed.py [-h] --title TITLE [--description DESCRIPTION] --site SITE
                   [--cover COVER] [--path PATH]

Generate a podcast RSS feed for a directory of mp3 files.

optional arguments:
  -h, --help            show this help message and exit
  --title TITLE, -t TITLE
                        Podcast title
  --description DESCRIPTION, -d DESCRIPTION
                        Podcast description
  --site SITE, -s SITE  Root URL to base feed links on
  --cover COVER, -c COVER
                        Cover image file name
  --path PATH, -p PATH  Path containing source files
```

## Example use case

For this example, we go through the steps of converting an audiobook from
Audible that you legally own into a locally hosted podcast. A similar process
works for any collection of mp3  files.

1. Download the .aax file.
2. Extract your auth code with [audible-activator](https://github.com/inAudible-NG/audible-activator).
3. Use the auth code to convert the .aax file into a directory of mp3 files with [AAXtoMP3](https://github.com/KrumpetPirate/AAXtoMP3).
4. (Optional) Download a cover art file for the RSS feed.
5. Run gen_feed.py on the directory of mp3 files. For example, if the working directory is the directory with the mp3 files and cover.jpg and one's laptop host name was `mylaptop.lan`, one could do:

        gen_feed.py --title "My Book" --cover cover.jpg --site http://mylaptop.lan:8000 > podcast.xml

6. Serve the feed and files by running `python -m http.server` in the directory with the feed and files. This is assuming you only plan to access the files on your local LAN. Otherwise, a more robust file server should be used.
7. Subscribe to `http://mylaptop.lan:8000/podcast.xml` in your podcatcher.
