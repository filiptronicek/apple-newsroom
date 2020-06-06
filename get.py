import feedparser
from shorten import shorten
NewsFeed = feedparser.parse("https://www.apple.com/newsroom/rss-feed.rss")

entry = NewsFeed.entries[1]

exShrt = "chl.li/xXxXx"

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
print(prprTxt())