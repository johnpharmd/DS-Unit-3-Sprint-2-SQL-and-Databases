#!/usr/bin/env python 3

import pandas as pd
import sqlite3

connection = sqlite3.connect('rpg_db.sqlite3')
character_inventory = pd.read_sql_query("SELECT * from charactercreator_character_inventory;", connection)
print(character_inventory.head())
print('There are', character_inventory.shape[0], 'total Characters.')

# from README.md on github, known character base classes are Fighter, Mage,
# Cleric, and Thief. Necromancer class appears to be subclass of Mage class.

necromancers = pd.read_sql_query("SELECT * from charactercreator_necromancer;",
                                 connection)
print('There are', necromancers.shape[0], 'Necromancers.')

char_items = pd.read_sql_query("SELECT * from armory_item;", connection)
print('\nThere are', char_items.shape[0], 'total Items.')

weapons = pd.read_sql_query("SELECT * from armory_weapon;", connection)
print(weapons.shape[0], 'are weapons.')
print(char_items.shape[0] - weapons.shape[0], 'are not weapons.\n')

first_twenty_chars_item_counts = pd.read_sql_query("SELECT character_id, COUNT(item_id) AS item_count from charactercreator_character_inventory GROUP BY character_id LIMIT 20;", connection)
print(first_twenty_chars_item_counts)

first_twenty_chars_weapon_counts = pd.read_sql_query("SELECT character_id, COUNT(item_id) AS weapon_count from charactercreator_character_inventory WHERE item_id in (SELECT distinct item_ptr_id from armory_weapon) GROUP BY character_id LIMIT 20;", connection)
# Hat Tip to KS/LSDS01 for assistance in honing this query above

print('\nIn "armory_item", the weapons are all grouped from item 138 through item 174. Thus, the following query shows character_id and number of items falling in that item range (inclusive of item 174).\n')
print(first_twenty_chars_weapon_counts)

print('\nOn average, each Character has', char_items.shape[0] / character_inventory.shape[0], 'Items.')

total_weapons_ratio = (37/174)  # see above for more information
print('\nOn average, each Character has', (char_items.shape[0] * total_weapons_ratio) / character_inventory.shape[0], 'Weapons.')

