import openai

openai.api_key = open("st_openai/openai_key.txt", "r").read()
MODEL_ENGINE = "text-davinci-003"
TEMPERATURE = 0.7

def txt_generate(user_input):
    completion = openai.Completion.create(
        engine=MODEL_ENGINE,
        prompt=user_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=TEMPERATURE,
    )
    response = completion.choices[0].text
    return str(response)

def img_generate(user_input):
    print("[GAME] Loading image...")
    response = openai.Image.create(
        prompt=user_input,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    print("[IMAGE URL] " + image_url)
