import time
from openai_api import openai_functions as api

THEMES = ["Fairy-Tale", "Ghosts", "Jungle Adventure", "Pirates", "Sci-Fi", "Superhero", "Western"]
LINE_GAP = 0.5

theme1 = THEMES[int(input("(1) Fairy-Tale\n" "(2) Ghosts\n" "(3) Jungle Adventure\n"
                          "(4) Pirates\n" "(5) Sci-Fi\n" "(6) Superhero\n" "(7) Western\n" "Theme 1: ")) - 1]
theme2 = THEMES[int(input("Theme 2: ")) - 1]

choice = ""
game_won = False
enemy1_won = False
enemy2_won = False


def story_read(story_file):
    global title
    global protagonist_name
    global protagonist_gender
    global protagonist_weapon
    global protagonist_spirit
    global mystical_figure
    global enemy1
    global enemy2
    global enemy3
    global enemy_boss
    global item1
    global item2

    global location_passageways;
    location_passageways = []
    global location_landscape_deadly

    global choice

    end_read = False

    with open(story_file, 'r') as file:
        while not end_read:
            for line in file.readlines():
                if line != '\n':
                    # Find the first and last occurrence of a double quote (").
                    start = line.find('"')
                    end_read = line.rfind('"')
                    if start != -1 and end_read != -1:
                        extracted_text = line[start + 1:end_read]

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

                        if '{enemy1}' in extracted_text:
                            extracted_text = f"{extracted_text.replace('{enemy1}', enemy1)}"
                        if '{enemy1.upper()}' in extracted_text:
                            extracted_text = f"{extracted_text.replace('{enemy1.upper()}', enemy1.upper())}"
                        if '{enemy2}' in extracted_text:
                            extracted_text = f"{extracted_text.replace('{enemy2}', enemy2)}"
                        if '{enemy2.upper()}' in extracted_text:
                            extracted_text = f"{extracted_text.replace('{enemy2.upper()}', enemy2.upper())}"
                        if '{enemy3}' in extracted_text:
                            extracted_text = f"{extracted_text.replace('{enemy3}', enemy3)}"
                        if '{enemy3.upper()}' in extracted_text:
                            extracted_text = f"{extracted_text.replace('{enemy3.upper()}', enemy3.upper())}"
                        if '{enemy_boss}' in extracted_text:
                            extracted_text = f"{extracted_text.replace('{enemy_boss}', enemy_boss)}"

                        if '{location_landscape_deadly}' in extracted_text:
                            extracted_text = f"{extracted_text.replace('{location_landscape_deadly}', location_landscape_deadly)}"

                        if '{location_passageways[0]}' in extracted_text:
                            extracted_text = f"{extracted_text.replace('{location_passageways[0]}', location_passageways[0])}"

                        if '{location_passageways[1]}' in extracted_text:
                            extracted_text = f"{extracted_text.replace('{location_passageways[1]}', location_passageways[1])}"

                        if '{location_passageways[2]}' in extracted_text:
                            extracted_text = f"{extracted_text.replace('{location_passageways[2]}', location_passageways[2])}"

                        if '\n' in extracted_text:
                            extracted_text = extracted_text.replace('\n', '')

                        if "[TXT]" in line:
                            print(extracted_text)
                            time.sleep(LINE_GAP)

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
                            if "[INP-CHC]" in line:
                                choice = _

                            time.sleep(LINE_GAP)

                        if "[TXT-GEN]" in line:

                            if "- Title]" in line:
                                title = api.txt_generate(extracted_text)
                            if "- MysticalFigure]" in line:
                                mystical_figure = api.txt_generate(extracted_text).upper()  # ALL CAPS
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
                            if "- DeadlyRegion]" in line:
                                location_landscape_deadly = api.txt_generate(extracted_text)
                            if ("- Passageway1]" in line) or ("- Passageway2]" in line) or ("- Passageway3]" in line):
                                location_passageways.append(api.txt_generate(extracted_text))

                        if "[IMG-GEN]" in line:
                            api.img_generate(f"{extracted_text}")
                            time.sleep(2 * LINE_GAP)

                        if "[END]" in line:
                            end_read = True

            file.seek(0)


def story_write():
    pass
