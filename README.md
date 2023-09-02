# StoryTime
**Latest Version:** 0.5.0

## 1) Introduction
The StoryTime application makes use of Python's `openai` module in order to generate exciting text-based adventures for the user to navigate through as well as images relating to the events in the story. Most of the text and story's structure is set, whilst some is generated using the `text-davinci-003` API, and all of the images are generated via the `dall-e 2` API architecture.

The goal of this project was to use generative AI to enterain and engage the user. The arbitrary and unrefined state of generative AI at this point in time does mean that outputs can be undesireable - I do admit this. However, even though generative AI is in its infancy, some very accurate and impressive results have been produced. Skill is required in creating prompts and vague inputs are not enough. Hence, I have optimised the prompts used to follow the structure below as much as I can:

```python
# Mood/Emotion + Quality + Lense + Source + Description + Subject + Setting + Purpose + Destination

user_input = """Happy, 4K poster, 300mm, found on Apple's Website, of Sci-Fi iPhone,
              with coral blue background, to sell the phone, trending on ArtStation"""

response = openai.Image.create(
  prompt=user_input,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print("[IMAGE URL] " + image_url)
```
