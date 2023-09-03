import time
import api_openai_functions as api

STORY_FILE = open("api_openai_story", 'r')

THEMES = ["Fairy-Tale", "Ghosts", "Jungle Adventure", "Pirates", "Sci-Fi", "Superhero", "Western"]
theme1 = THEMES[int(input("(1) Fairy-Tale\n" "(2) Ghosts\n" "(3) Jungle Adventure\n"
                      "(4) Pirates\n" "(5) Sci-Fi\n" "(6) Superhero\n" "(7) Western\n" "Theme 1: "))-1]
theme2 = THEMES[int(input("Theme 2: "))-1]

for line in STORY_FILE.readlines():
    if line != '\n':
        # Find the first and last occurrence of a double quote (").
        start = line.find('"')
        end = line.rfind('"')
        if start != -1 and end != -1:
            extracted_text = line[start + 1:end]

            if '{title}' in extracted_text:
                extracted_text = f"{extracted_text.replace('{title}', title)}"
            if '{theme1}' in extracted_text:
                extracted_text = f"{extracted_text.replace('{theme1}', theme1)}"
            if '{theme2}' in extracted_text:
                extracted_text = f"{extracted_text.replace('{theme2}', theme2)}"

            if '{protagonist_name}' in extracted_text:
                extracted_text = f"{extracted_text.replace('{protagonist_name}', protagonist_name)}"
            if '{protagonist_gender}' in extracted_text:
                extracted_text = f"{extracted_text.replace('{protagonist_gender}', protagonist_gender)}"
            if '{protagonist_weapon}' in extracted_text:
                extracted_text = f"{extracted_text.replace('{protagonist_weapon}', protagonist_weapon)}"
            if '{protagonist_spirit}' in extracted_text:
                extracted_text = f"{extracted_text.replace('{protagonist_spirit}', protagonist_spirit)}"

            if '{item1}' in extracted_text:
                extracted_text = f"{extracted_text.replace('{item1}', item1)}"
            if '{item2}' in extracted_text:
                extracted_text = f"{extracted_text.replace('{item2}', item2)}"

            if '{mystical_figure}' in extracted_text:
                extracted_text = f"{extracted_text.replace('{mystical_figure}', mystical_figure)}"

            if '{enemy_boss}' in extracted_text:
                extracted_text = f"{extracted_text.replace('{enemy_boss}', enemy_boss)}"

            if '\n' in extracted_text:
                extracted_text = extracted_text.replace('\n', '')

            if "[TXT]" in line:
                print(extracted_text)
                time.sleep(3.5)

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

                time.sleep(3.5)

            if "[TXT-GEN]" in line:

                if "- Title]" in line:
                    title = api.txt_generate(extracted_text)
                if "- Mystical Figure]" in line:
                    mystical_figure = api.txt_generate(extracted_text).upper() #ALL CAPS
                if "- Enemy1]" in line:
                    enemy1 = api.txt_generate(extracted_text)
                if "- Enemy2]" in line:
                    enemy2 = api.txt_generate(extracted_text)
                if "- Enemy3]" in line:
                    enemy3 = api.txt_generate(extracted_text)
                if "- EnemyBoss]" in line:
                    enemy_boss = api.txt_generate(extracted_text)
                if "- Item1]" in line:
                    item1 = api.txt_generate(extracted_text)
                if "- Item2]" in line:
                    item2 = api.txt_generate(extracted_text)

            if "[IMG-GEN]" in line:
                api.img_generate(f"{extracted_text}")
                time.sleep(7.0)
