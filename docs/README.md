# StoryTime
**Latest Version:** 0.8.0

## 1) Introduction
The StoryTime application makes use of Python's `openai` module in order to generate exciting text-based adventures for the user to navigate through as well as images relating to the events in the story. Elements of the story are generated in accordance to selected themes (`theme1` and `theme2`) through the `text-davinci-003` API. All of the images are generated via the `dall-e 2` API architecture.

The goal of this project was to use generative AI to enterain and engage the user. Do note that the arbitrary and unrefined state of generative AI at this point in time does mean that some outputs can be undesireable: either inaccurate or inappropriate to the selected themes. However, even though generative AI is in its infancy, I have optimised prompts to generate the best results.

I have chosen to build an interpreter for the stories using Python and store the story's structure in a separate text-file instead of hard-coding the story within Python.

Instead of:
```python
print("[GAME] Welcome to your adventure!")
time.sleep(1.5)
print("[GAME]")
```

I have used:
```python
#main.py
for line in file
```

## 2) Getting Started
TBA
