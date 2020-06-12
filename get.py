import feedparser
from shorten import shorten
import time
from tweet import tweet

NewsFeed = feedparser.parse("https://www.apple.com/newsroom/rss-feed.rss")

exShrt = "chl.li/xXxXx"

def cut(content, limit = 250):
    moreTxt = "..."
    limit = limit - len(moreTxt) - len(exShrt)
    if len(content) >= limit:
        content = content[:limit]+moreTxt
    return content

def prprTxt(entry):
    tweetText = cut(entry.summary.replace("<br/>", ". ").replace("<br />", ". ").split("Press Contacts")[0])
    tweetText += "\n"+shorten(entry.link)
    return tweetText

def check():
    with open('used.txt') as f:
        used=f.readlines()
    for entryN in enumerate(NewsFeed.entries[:5]):
        id = entryN[1].id.split("/")[-1]
        usedIds = []
        for ind in used:
            usedIds.append(ind.split("\n")[0])

        if id in usedIds:
            pass
        else:
            print("New article!")
            tweet(prprTxt(entryN[1]))
            with open("used.txt", "a") as f:
                f.writelines(id+"\n")