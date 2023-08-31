import time
import api_openai_functions as api

STORY_FILE = open("api_openai_story", 'r')

THEMES = ["Fairy-Tale", "Ghosts", "Jungle Adventure", "Pirates", "Sci-Fi", "Superhero"]
theme1 = THEMES[int(input("(1) Fairy-Tale\n" "(2) Ghosts\n" "(3) Jungle Adventure\n"
                      "(4) Pirates\n" "(5) Sci-Fi\n" "(6) Superhero\n" "Theme 1: "))-1]
theme2 = THEMES[int(input("Theme 2: "))-1]

enemy_boss = ""

for line in STORY_FILE.readlines():
    if line != '\n':
        # Find the first and last occurrence of a double quote (").
        start = line.find('"')
        end = line.rfind('"')
        if start != -1 and end != -1:
            extracted_text = line[start + 1:end]

            if "[TXT]" in line:
                print(extracted_text)
                time.sleep(1.5)

            if "[TXT-INP]" in line:
                _ = input(extracted_text)

                if "[INP-NAME]" in line:
                    protagonist_name = _
                if "[INP-GEN]" in line:
                    protagonist_gender = _
                if "[INP-SPIRIT]" in line:
                    protagonist_spirit = _
                if "[INP-WPN]" in line:
                    protagonist_weapon = _

                time.sleep(1.5)

            if "[TXT-GEN]" in line:

                try: formatted_string = f"{extracted_text.replace('{theme1}', theme1).replace('{theme2}', theme2).replace('{enemy_boss}', enemy_boss)}"
                except: pass

                if "- Title]" in line:
                    title = api.txt_generate(formatted_string)
                    print(title)
                if "- Mystical Figure]" in line:
                    mystical_figure = api.txt_generate(formatted_string)
                    print(mystical_figure)
                if "- Enemy1]" in line:
                    enemy1 = api.txt_generate(formatted_string)
                    print(enemy1)
                if "- Enemy2]" in line:
                    enemy2 = api.txt_generate(formatted_string)
                    print(enemy2)
                if "- Enemy3" in line:
                    enemy3 = api.txt_generate(formatted_string)
                    print(enemy3)
                if "- EnemyBoss]" in line:
                    enemy_boss = api.txt_generate(formatted_string)
                    print(enemy_boss)
                if "- Item1]" in line:
                    item1 = api.txt_generate(formatted_string)
                    print(item1)
                if "- Item2]" in line:
                    item2 = api.txt_generate(formatted_string)
                    print(item2)

            if "[IMG-GEN]" in line:
                try: formatted_string = f"{extracted_text.replace('{theme1}', theme1)}"
                except: pass

                try: formatted_string = f"{extracted_text.replace('{theme2}', theme2)}"
                except: pass

                try: formatted_string = f"{extracted_text.replace('{protagonist_gender}', protagonist_gender)}"
                except: pass

                try: formatted_string = f"{extracted_text.replace('{protagonist_weapon}', protagonist_weapon)}"
                except: pass

                try: formatted_string = f"{extracted_text.replace('{protagonist_spirit}', protagonist_spirit)}"
                except: pass

                api.img_generate(f"{formatted_string}")
