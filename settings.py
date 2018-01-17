#print("What tags do you want to search for?\nInput each tag followed by a comma (Example: Monkey, Food, Restaurant):")
#x= input()

print("Hellow Knighty")
TRACK_TERMS = ["dota2","gaming"]
CONNECTION_STRING = "sqlite:///tweets.db"
CSV_NAME = "tweets.csv"
TABLE_NAME = "data"

try:
    from private import *
except Exception:
    pass