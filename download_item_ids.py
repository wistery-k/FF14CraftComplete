import requests as r
from lxml import html
import time

def save_item_ids(page, item_ids):
    with open("item_ids/{}.txt".format(page), "w") as file:
        file.write("\n".join(item_ids))

def main():
    for p in range(1, 216):
        item_id_list = []
        # 昇順
        url = "https://jp.finalfantasyxiv.com/lodestone/playguide/db/recipe/?page={}&order=4".format(p)
        print("Downloading: {}".format(url))
        response = r.get(url)
        if response.status_code != 200:
            print("Bad response code: {}".format(response.status_code))
            print ("URL: {}".format(response.url))
            break

        text = response.text
        tree = html.fromstring(text)
        links = tree.xpath('//*[@id="character"]/tbody/tr/td[1]/div[2]/a')
        for a in links:
            href= a.get("href")
            item_id = href.split("/")[-2]
            item_id_list.append(item_id)
        save_item_ids(p, item_id_list)
        time.sleep(1)

main()