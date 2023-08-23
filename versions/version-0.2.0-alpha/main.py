import time
import random
import api_openai_functions as api

# Themes that are input by user (Sci-Fi, Pirates, Ghosts, Jungle Adventure, Fairy-Tale, Superhero)
THEMES = ["Fairy-Tale", "Ghosts", "Jungle Adventure", "Pirates", "Sci-Fi", "Superhero"]
theme1 = THEMES[int(input("(1) Fairy-Tale\n"
                      "(2) Ghosts\n"
                      "(3) Jungle Adventure\n"
                      "(4) Pirates\n"
                      "(5) Sci-Fi\n"
                      "(6) Superhero\n"
                      "Theme 1: "))-1]

theme2 = THEMES[int(input("(1) Fairy-Tale\n"
                      "(2) Ghosts\n"
                      "(3) Jungle Adventure\n"
                      "(4) Pirates\n"
                      "(5) Sci-Fi\n"
                      "(6) Superhero\n"
                      "Theme 2: "))-1]

# Names of entities output by API
title = api.txt_generate(f"Give a title for a story around the themes {theme1} and {theme2}").replace('\"', '')

mystical_figure = api.txt_generate(f"Give a name for an advisory figure based on {theme1} and {theme2}").replace('\n', '')

enemy1 = api.txt_generate(f"Give an enemy name based on {theme1} and {theme2} for a melee enemy").replace('\n', '')
enemy2 = api.txt_generate(f"Give an enemy name based on {theme1} and {theme2} for a ranged enemy").replace('\n', '')
enemy3 = api.txt_generate(f"Give an enemy name based on {theme1} and {theme2} for a swarm enemy").replace('\n', '')
enemy_boss = api.txt_generate(f"Give a single boss name based on a god in mythology, {theme1}, {theme2}").replace('\n', '')

item1 = api.txt_generate(f"Give an item needed before fighting {enemy_boss} of 2 words in length").replace('\n', '')
item2 = api.txt_generate(f"Give an item needed to unlock {enemy_boss} of 2 words in length").replace('\n', '')

print([mystical_figure, enemy1, enemy2, enemy3, enemy_boss, item1, item2])

# Generates options of passageways and corrects for duplication
passages_configured = False
while not passages_configured:
    passages = [api.txt_generate(f"A passageway name based on {theme1} or {theme2}")[2:] for i in range(1, random.randint(3, 5))]
    passages.sort()
    for i in range(0, len(passages)-2):
        if passages[i] == passages[i+1]:
            passages_configured = False
        else:
            passages_configured = True
print(passages)

print(title.upper())
time.sleep(3.0)

print("[GAME] A mystical voice speaks to you from above")
time.sleep(1.5)
print("[VOICE] " + api.txt_generate("Give a welcome from the perspective of an unknown advisor to help the "
                                    "protagonist kill an evil villain in 25 words")[2:-1])
time.sleep(1.5)

protagonist_name = input("[VOICE] What is your name? Name: ")
time.sleep(1.5)
print(f"[VOICE] Ah hello {protagonist_name}, it is a pleasure to meet you.")
time.sleep(1.5)
protagonist_gender = input("[VOICE] I require your gender. Are you a man or woman? Gender: ")
time.sleep(1.5)

print("[VOICE] In this world of ours...")
time.sleep(1.5)
print("[VOICE] ...there are many ecosystems...")
time.sleep(1.5)
print("[VOICE] ...from the underground crystal jungles...")
time.sleep(1.5)
print("[VOICE] ...to the floating deserts in the clouds...")
time.sleep(1.5)
print("[VOICE] ...each of which host many beautiful creatures.")
time.sleep(1.5)
api.img_generate(f"Landscape based on {theme1} and {theme2}")
time.sleep(5.0)

print("[VOICE] At birth you would have had a spirit animal engraved into you.")
time.sleep(1.5)
protagonist_spirit = input("[VOICE] Which spirit animal has you been engraved into you. Spirit Animal: ")
time.sleep(1.5)
print("[VOICE] Also at birth you would have been given a weapon to guide you through life's perils.")
time.sleep(1.5)
protagonist_weapon = input("[VOICE] Which is yours? Weapon: ")
time.sleep(1.5)
api.img_generate(f"{protagonist_gender} holding a {protagonist_weapon} riding a {protagonist_spirit}")
time.sleep(5.0)
