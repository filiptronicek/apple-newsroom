import feedparser
from shorten import shorten
NewsFeed = feedparser.parse("https://www.apple.com/newsroom/rss-feed.rss")

entry = NewsFeed.entries[1]

exShrt = "chl.li/xXxXx"

def check():
    with open('used.txt') as f:
        used=f.readlines()
    for i,entryN in enumerate(NewsFeed.entries[:5]):
        id = entryN.id.split("/")[-1]
        usedIds = []
        for ind in used:
            usedIds.append(ind.split("\n")[0])

        if id in usedIds:
            pass
        else:
            print("New article!")
            with open("used.txt", "a") as f:
                f.writelines(id+"\n")
        

def cut(content, limit = 280):
    moreTxt = "..."
    limit = limit - len(moreTxt) - len(exShrt)
    if len(content) >= limit:
        content = content[:limit]+moreTxt
    return content

def prprTxt():
    tweetText = cut(entry.summary.replace("<br/>", ". ").replace("<br />", ". ").split("Press Contacts")[0])
    tweetText += "\n"+shorten(entry.link)
    return tweetText
check()