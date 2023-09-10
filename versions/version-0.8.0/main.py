from story import story_functions as story

story.story_read("story/story_beg.txt")

while not story.game_won:
    story.story_read("story/story_mid/story_mid.txt")

    if story.choice == "1":
        story.story_read("story/story_mid/story_mid_passage1/story_mid_passage1.txt")
        if story.choice == "1":
            story.story_read("story/story_mid/story_mid_passage1/story_mid_passage1-1.txt")
            if story.choice == "1":
                story.story_read("story/story_mid/story_mid_passage1/story_mid_passage1-2.txt")
                if story.choice == "1":
                    story.story_read("story/story_mid/story_mid_passage1/story_mid_passage1-2-1.txt")
                elif story.choice == "2":
                    story.story_read("story/story_mid/story_mid_passage1/story_mid_passage1-2-2.txt")
                    story.enemy1_won = True
        elif story.choice == "2":
            # 'sin' denotes what happens without drinking potion first
            story.story_read("story/story_mid/story_mid_passage1/story_mid_passage1-2sin.txt")
    elif story.choice == "2":
        pass

    elif story.choice == "3":
        pass

story.story_read("story/story_end.txt")
