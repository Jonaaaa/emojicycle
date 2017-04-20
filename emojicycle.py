#!/usr/bin/env python
import requests
import sys
import json
import os

status = "stuff"

emojis = [
        ":trollface:",
        ":apple:",
        ":can:",
        ":neckbeard:",
        ":banana:",
        ":beers:",
        ":moneybag:",
        ":doughnut:"
        ]

def main():
    try:
        #make sure this is set
        token = os.environ["SLACK_API_TOKEN"]
        url = "https://slack.com/api/users.profile.set"
        print "[-] EMOJI TIME!!"
        while True:
            for emoji in emojis:
                json_data = {"status_text":status,"status_emoji":emoji}
                params = {'token':token,'profile': json.dumps(json_data)}
                r = requests.post(url, params=params)
    except:
       print "[!] Uh Oh..."
       sys.exit(0)


if __name__ == "__main__":
    main()
