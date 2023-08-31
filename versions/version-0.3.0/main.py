import time
import random
import api_openai_functions as api

STORY_FILE = open("api_openai_story", 'r')

theme1 = "dinosaur"
theme2 = "superhero"
enemy_boss = "T-Rex man"

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
                input(extracted_text)
                time.sleep(1.5)

            if "[TXT-GEN]" in line:
                substrings = ["- Title]", "- Mystical Figure]",
                              "- Enemy1]", "- Enemy2]", "- Enemy3]", "- EnemyBoss]",
                              "- Item1]", "- Item2]"]

                # Check if any of the substrings is present in line.
                if any(sub in line for sub in substrings):
                    formatted_string = f"{extracted_text.replace('{theme1}', theme1).replace('{theme2}', theme2).replace('{enemy_boss}', enemy_boss)}"
                    print(f"{formatted_string}")
