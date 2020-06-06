import requests

def shorten(url):
    sUrl = requests.get("https://chl.li/api/v1/shorten?url="+url).text
    sUrl = sUrl.replace("<h1>","").replace("</h1>","")
    return (sUrl)
