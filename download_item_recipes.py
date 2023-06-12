import requests as r
from lxml import html
import time

def read_item_ids(page):
    with open("item_ids/{}.txt".format(page), "r") as file:
        return map(lambda s: s.strip(), file.readlines())

def save_item_recipe(item_id, recipe_html):
    with open("item_recipes/{}.txt".format(item_id), "w", encoding='utf-8') as file:
        file.write(recipe_html)

def main():
    for p in range(1, 216):
        for item_id in read_item_ids(p):
            print("{} {}".format(p, item_id))
            url = "https://jp.finalfantasyxiv.com/lodestone/playguide/db/recipe/{}/".format(item_id)
            print("Downloading: {}".format(url))
            response = r.get(url)
            if response.status_code != 200:
                print("Bad response code: {}".format(response.status_code))
                print ("URL: {}".format(url))
                return

            text = response.text
            save_item_recipe(item_id, text)
            time.sleep(1)

main()