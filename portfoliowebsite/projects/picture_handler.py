import os
from flask import url_for,current_app
from PIL import Image

def add_picture(pic_upload):

    filename = pic_upload.filename
    extension = filename.split('.')[-1]
    storage_filename = str(filename)+'.'+extension
    filepath = os.path.join(current_app.root_path,'static/media',storage_name)

    output_size = (200,200)
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
