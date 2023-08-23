import random
import api_openai_functions as api

# Themes that are input by user
theme1 = input("Input theme 1: ")
theme2 = input("Input theme 2: ")

# Names of entities output by API
title = api.txt_generate(f"Give a title for a story around the themes {theme1} and {theme2}")

mystical_figure = api.txt_generate(f"Give a name for an advisory figure based on {theme1} and {theme2}")

enemy1 = api.txt_generate(f"Give an enemy name based on {theme1} and {theme2} for a melee enemy")
enemy2 = api.txt_generate(f"Give an enemy name based on {theme1} and {theme2} for a ranged enemy")
enemy3 = api.txt_generate(f"Give an enemy name based on {theme1} and {theme2} for a swarm enemy")
enemy_boss = api.txt_generate(f"Give a single boss name based on a god in mythology, {theme1}, {theme2}")

item1 = api.txt_generate(f"Give an item needed before fighting {enemy_boss} of 2 words in length")
item2 = api.txt_generate(f"Give an item needed to unlock {enemy_boss} of 2 words in length")

passages = [api.txt_generate(f"A passageway name based on {theme1} or {theme2}")[2:] for i in range(1, random.randint(3, 5))]
print(passages)

print(title.upper())
