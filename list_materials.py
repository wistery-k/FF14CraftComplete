import requests as r
from lxml import html
import json
    
def read_all_recipes_json():
    with open("public/all_recipes.json", "r", encoding="utf-8") as file:
        return json.load(file)

skip_list = [
    "ビーチ材", "ラーチ材", "ハイスチールトライデント",
    "ハイスチールナゲット", "ハイスチールインゴット", "卸し鉄", "ドマアイアン・ロングソード",
    "ハイスチールナゲット", "ハイスチール・サーマルアレンビック", "卸し鉄", "ドマアイアン・ディフェンダーガントレット", "ドマアイアン・スレイヤーガントレット", "ドマアイアン・ディフェンダーグリーヴ",
    "ドマアイアン・カイトシールド", "タイガーディフェンダーコート",
    "トリフェーン", "粘板岩砥石", "キュプロナゲット", "トリフェーンアタッカーイヤリング", "トリフェーンレンジャーイヤリング", "トリフェーンアタッカーチョーカー", "トリフェーンアタッカーブレスレット",
    "トリフェーンアタッカーリング", "キュプロインゴット", "キュプロキャスターブレスレット", "ムードスードホーン・ディフェンダーリング", "キュプロテンプルチェーン",
    "スタースピネル", "ダリウムナゲット", "スタースピネル・ディフェンダーブレスレット", "スタースピネル・ディフェンダーリング", "スタースピネル・アタッカーリング",
    "スタースピネル・ヒーラーリング", "ブルホーンニードル", "ダリウムディフェンダーヘアピン", "ダリウムスレイヤーヘアピン", "スタースピネル・ディフェンダーイヤリング",
    "スタースピネル・ディフェンダーチョーカー",
    "ガガナレザー", "ギュウキレザー", "ギュウキリストバンド", "タイガーレザー", "紅玉綿布", "紅玉綿糸", "葛布", "葛苧", "クズクロス・ディフェンダーロングキルト",
    "キュプロエンチャントインク", "ギュウキコーデックス", "活力の霊水G1", "カブトにかわ", "名匠の薬茶", "巨匠の薬茶"
]

def is_skip(recipe):
    if recipe["hidensyo"] != "":
        return True
    if recipe["class"] == "調理師":
        return True
    if recipe["name"] in skip_list:
        return True
    lv = int(recipe["lv"].replace("★", ""))
    if lv < 60 or lv > 65:
        return True
    if "簡易製作不可" in recipe["crafting_conditions"]:
        return True
    return False

def main():
    all_materials = {}
    for recipe in read_all_recipes_json():
        if is_skip(recipe) is False:
            print(recipe["name"])
            for m in recipe["materials"]:
                name = m["name"]
                num = m["num"]
                if name not in all_materials:
                    all_materials[name] = num
                else:
                    all_materials[name] = all_materials[name] + num
    print("@@@@@")
    for name in all_materials:
        print("{},{}".format(name, all_materials[name]))

main()