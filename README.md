# FFXIV Craft Complete
Helps you plan what you wish to craft.
Primarily designed for completing craft logs.

## download_item_ids.py
Retrieve all item ids by fetching https://jp.finalfantasyxiv.com/lodestone/playguide/db/recipe/?page={}&order=4
Ids (one per line) will be saved under **item_ids** folder.
You don't need to run this script unless you want ids of new items.

## download_item_recipes.py
Retrieve all recipes by fetching https://jp.finalfantasyxiv.com/lodestone/playguide/db/recipe/{}/
Recipes HTML will be saved under **item_recipes** folder.
You don't need to run this script unless you got new items or recipes got updated.
Running this script for all items is not recommended (will take 3+ hours).

## parse_item_recipes.py
Generate **public/all_recipes.json** from files under **item_recipes** folder.
This script doesn't issue any HTTP requests.

## list_materials.py
Output materials you need (you need to update this script for now)

## !!! WARNING !!!
Follow FFXIV terms of use.
DO NOT change/remove sleep seconds in the scraping scripts. This ensures you to not harm FFXIV official website.
For all game data, (C) SQUARE ENIX CO., LTD. All Rights Reserved.
