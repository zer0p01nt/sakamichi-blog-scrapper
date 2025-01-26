from bs4 import BeautifulSoup
import requests
import certifi

def hinata(url):
    r = requests.get(url, verify=certifi.where())
    soup = BeautifulSoup(r.content, "html.parser")
    image = soup.find("div", class_="c-blog-article__text").find_all("img")
    result = []
    for i in image:
        link = i["src"]
        result.append(link)
    return result