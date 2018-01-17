import csv
import argparse
import time
import requests

# Depends on omdbtool from https://github.com/bgr/omdb-cli

apiKey = '93d7931c' # Your personal apikey from omdb: http://www.omdbapi.com/ to get one

# These fields from the OMDB results get added to the output
omdbFields = [
    'Director',
    'Genre',
    'Writer',
    'Actors',
    'Plot',
    'Language',
    'Country',
    'Awards',
    'Poster',
    'imdbID',
    'Type',
    'DVD',
    'BoxOffice',
    'Production',
    'Website'
]

# ArgParser setup: make some command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="input file, an export from letterboxd", required=True)
parser.add_argument("-o","--output", help="output file where ya stuff goes", required=True)
args = parser.parse_args()

# Prep this variable for the csv writer so we can check it later
writer = None

with open(args.output,'w') as fout: # Get a handle on the OUTPUT file
    with open(args.input) as fin: # Get a handle on the INPUT file
        reader = csv.DictReader(fin) # Create a reader that treats each row as a "dictionary" (keys and values instead of a flat list)
        for row in reader:
            if not writer: # If the writer is still equal to None, set it up
                writer = csv.DictWriter(fout,fieldnames=list(row.keys())+omdbFields) # The fields we'll write are the original input fields plus the omdb fields listed above
                writer.writeheader() # Put a header on that csv

            # A little feedback so you know it's working
            print("Starting {}...".format(row['Name']),end='')

            payload = {'apikey':apiKey,'t':row['Name'],'y':row['Year']}
            r = requests.get("http://www.omdbapi.com",params=payload)

            # Make a tidy object from the json string returned by omdb
            omdb = r.json()

            # Add the contents of the omdb response one key at a time to the existing input data
            for f in omdbFields:
                if f in omdb: # make sure this field is in the omdb result
                    row[f] = omdb[f]
                else:       # if it's not there, put an empty string so the csvwriter doesn't choke
                    row[f] = ''
                    print("\tdidn't find {}".format(f))

            # Write the new combined row of data to the output file
            writer.writerow(row)

            # Feedback...
            print("done")

            # Don't do this more often than every 1 seconds to avoid abusing omdb.
            # If you're a patron (pay them a buck a month) you can comment this out.
            time.sleep(1)

