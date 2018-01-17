# letterboxd-omdb-mashup
Supplement a letterboxd export file with movie details from the Open Movie Database API

Letterboxd.com is a list-making and recommendation site for movie fans. Note what you've seen, keep track of what you'd like to see, read and write reviews, and find more movies in similar genres, liked by people with similar tastes, including the same cast or crew, and chat with other superfans.

Letterboxd has the progressive policy of giving you control of your data as well. As a registered user you can export your watchlist, reviews and so on with one convenient (and not hidden) button on your profile page. (If you're like me and sometimes prefer to work with large data sets locally, you might like that they also let you import data the same way.) One major limitation of this export feature though is that it only includes the movie's title, release year, and URI on letterboxd.com. If you're interested in supplementing that with directors' names, cast, reviews, box office gross, etc., this script will do so automatically.

This is possible thanks to the incredible publicly supported work by the OMDBAPI team (omdbapi.com). This dead simple REST API is geared for looking up a specific movie by title and optionally year, or searching on a number of parameters. It's entirely crowd-supported, so if you find this script or their facilities useful, please consider becoming a patron.

## Usage

This is a python3 script depending on the following modules:

- csv
- argparse
- time
- requests

Install those through pip and you're through the worst of it.

1. Get an OMDB API key at omdbapi.com. Paste it into mashup.py between the single quotes for the value of apiKey.

    ```
    apiKey = 'yourkeygoeshere'
    ```

1. Export your data from letterboxd at https://letterboxd.com/settings/data/
1. Your data will download as a zip file; extract it to somewhere near this script.
1. Run mashup.py against the file you're interested in supplementing:

    ```
    python3 mashup.py -i watched.csv -o output.csv
    ```

1. The script will take some time to run depending on the size of your list.

## Notes

There's a time.sleep(1) at the end of the main loop just to enforce some rate-limiting on behalf of OMDBAPI. As far as I can find they only enforce daily limits for free users, not rate limits, but be polite.

The daily limit for OMDBAPI free users, as of this README, is 1000 API requests. If you find that this is not enough (or even if you just appreciate access to a free database of movie data!) consider becoming a patron.
