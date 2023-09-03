from st_story import story_functions as story

story.story_read(open("st_story/story_beg.txt", 'r'))  # Fixed

story.story_write()  # Edit 'story_mid.txt'
story.story_read(open("st_story/story_mid.txt", 'r'))  # Not Fixed

story.story_read(open("st_story/story_end.txt", 'r'))  # Fixed
