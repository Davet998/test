#LEcture 84
import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("data.json"))
#print(data)
#print(data["rain"])
#print(data.keys())
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Type Y for yes, N for no: " % get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "The word dows not exist. Please check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word does not exist."

word = input("Enter word: ")
print(translate(word))

#print(SequenceMatcher(None, "rainn", "rain").ratio())
#print(get_close_matches("rainn",data.keys(), n=1, cutoff=0.6))
