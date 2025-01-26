from bs4 import BeautifulSoup
import requests
import certifi

def nogi(url):
    base_url = "https://www.nogizaka46.com"
    r = requests.get(url, verify=certifi.where())
    soup = BeautifulSoup(r.content, "html.parser")
    image = soup.find("div", class_="bd--edit").find_all("img")
    result = []
    for i in image:
        link = i["src"]
        result.append(base_url + link)
    return result