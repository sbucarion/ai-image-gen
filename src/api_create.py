import webuiapi
import random
import os 
from dotenv import load_dotenv
import time
import copy 

from api_config import settings, model, initial_seed
from write_to_database import upload_record, check_if_record_exists
from upload_image import upload_image_to_servers, get_config_id, upload_photo_to_database

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

    result = api.txt2img(
        prompt=prompt,
        negative_prompt=negative_prompt,
        seed=initial_seed+image_index,
        cfg_scale=settings['cfg_scale'],
        enable_hr=True,
        hr_scale=settings['hr_scale'],
        hr_upscaler=settings['hr_upscaler'],
        denoising_strength=settings['denoising_strength'],
    )

    return result


def save_photo(photo):

    load_dotenv()
    PROJECT_PATH = os.getenv('PROJECT_PATH')

    file_name = str(time.time()).split(".")[0]

    file_path = PROJECT_PATH + r'\\images\\{}.jpg'.format(file_name)

    photo.image.save(fp=file_path)

    return file_name
    

def main():

    prompt = """realistic cat"""
    negative_prompt = """dog"""

    api = setup_api_connection()

    for i in range(1):

        photo = generate_image(api, prompt, negative_prompt, i)

        file_name = save_photo(photo)

        print(file_name)

        # upload_image_to_servers(model, initial_seed, txt2img_settings)

        # config_id = get_config_id(model, settings)

        # print(config_id)

        # # Convert config to db id

        # # Upload file to bucket and save meta to db
        # file_name = "2354642624"
        # upload_photo_to_database(model, initial_seed + i, prompt, negative_prompt, file_name, settings)


        #upload_image()


main()
