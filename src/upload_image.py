import copy

from write_to_database import upload_record, check_if_record_exists


def get_config_id(model, settings):

    meta_data = copy.deepcopy(settings)

    meta_data["model"] = model

    config_db_id = check_if_record_exists(meta_data, "image_api_imageconfigs")

    return config_db_id


def upload_photo_to_database(model, seed, prompt, negative_prompt, file_name, settings):

    config_id = get_config_id(model, settings)

    # Add photo metadata to db
    photo_metadata = {
        "prompt": prompt, 
        "negative_prompt": negative_prompt, 
        "seed": seed, 
        "configuration_id": config_id, 
        "unix_id": file_name
    }

    # prompt, n_prompt, seed
    photo_id = upload_record(photo_metadata, "image_api_imagemetadata")

    return photo_id


def upload_photo_to_bucket():

    

    return


def upload_image_to_servers(model, settings):    
    
    return
