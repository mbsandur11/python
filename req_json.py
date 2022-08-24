import requests
import json
import pprint

url = "https://opentdb.com/api.php?amount=1&type=multiple"
endgame = ""

while endgame != "quit":
    r = requests.get(url)
    if (r.status_code !=200):
        endgame = input("sorrym, there was a problem retriving the question. Please enter to try again or 'quit' the game")
    else:
        data =json.loads(r.text)
        pprint.pprint(data)
        input("press enter to get a new queston")