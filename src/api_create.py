import webuiapi
import random
import os 
from dotenv import load_dotenv
import time

from api_config import txt2img_settings, model


load_dotenv()
PROJECT_PATH = os.getenv('PROJECT_PATH')


def setup_api_connection():
    api = webuiapi.WebUIApi()
    api = webuiapi.WebUIApi(host='127.0.0.1', port=7860)


    # return map of current options
    options = api.get_options()


    # change sd model
    options = {}
    options['sd_model_checkpoint'] = model
    api.set_options(options)

    return api


def generate_image(api, prompt, negative_prompt, image_index):

    load_dotenv()
    PROJECT_PATH = os.getenv('PROJECT_PATH')

    result = api.txt2img(
        prompt=prompt,
        negative_prompt=negative_prompt,
        seed=txt2img_settings['seed']+image_index,
        cfg_scale=txt2img_settings['cfg_scale'],
        enable_hr=True,
        hr_scale=txt2img_settings['hr_scale'],
        hr_upscaler=txt2img_settings['hr_upscaler'],
        denoising_strength=txt2img_settings['denoising_strength'],
    )

    file_name = str(time.time()).split(".")[0]
    result.image.save(fp=PROJECT_PATH + r'\\images\\{}.jpg'.format(file_name))


def main():

    prompt = """"""
    negative_prompt = """"""

    api = setup_api_connection()

    for i in range(1):
        generate_image(api, prompt, negative_prompt, i)


main()