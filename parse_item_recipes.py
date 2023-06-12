import requests as r
from lxml import html
import time
import json

def read_item_ids(page):
    with open("item_ids/{}.txt".format(page), "r") as file:
        return map(lambda s: s.strip(), file.readlines())

def read_item_recipe(item_id):
    with open("item_recipes/{}.txt".format(item_id), "r", encoding='utf-8') as file:
        return file.read()
    
def save_all_recipes_json(recipes):
    with open("public/all_recipes.json", "w", encoding='utf-8') as file:
        file.write(json.dumps(recipes, ensure_ascii=False))

def main():
    all_recipes = []
    for p in range(1, 216):
        for item_id in read_item_ids(p):
            print("{} {}".format(p, item_id))

            text = read_item_recipe(item_id)
            tree = html.fromstring(text)
            # classは予約語
            clas = tree.xpath('//*[@id="eorzea_db"]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/p[@class="db-view__item__text__job_name"]')[0].text
            hidensyo_element = tree.xpath('//*[@id="eorzea_db"]/div[2]/div[2]/div/div[1]/div[2]/div[2]/p[@class="db-view__recipe__text__book_name"]')
            hidensyo = "" if len(hidensyo_element) == 0 else hidensyo_element[0].text
            name = tree.xpath('//*[@id="eorzea_db"]/div[2]/div[2]/div/div[1]/div[2]/div[2]/h2')[0].text.strip()
            lv_num = tree.xpath('//*[@id="eorzea_db"]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/p/span[1]')[0].text.strip()
            lv_stars = len(tree.xpath('//*[@id="eorzea_db"]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/p/span')) - 1
            lv = lv_num + ("★" * lv_stars)
            materials_elements = tree.xpath('//*[@id="eorzea_db"]/div[2]/div[2]/div/div[1]/div[3]/div[3]/div/div')

            materials = list(map(lambda div: { "name": div.get("data-name").strip(), "num": int(div.get("data-num").strip())}, materials_elements))

            crafting_conditions_elements = tree.xpath('//*[@id="eorzea_db"]/div[2]/div[2]/div/div[1]/div[3]/dl/dd')
            crafting_conditions = list(map(lambda dd: dd.text.strip(), crafting_conditions_elements))

            recipe = {
                "class": clas,
                "hidensyo": hidensyo,
                "name": name,
                "lv": lv,
                "materials": materials,
                "crafting_conditions": crafting_conditions
            }
            all_recipes.append(recipe)
    save_all_recipes_json(all_recipes)

main()