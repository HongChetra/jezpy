import os 
import secrets 
from PIL import Image
from flask import current_app
#from sec import app




# Saving image into path with random hex number 
# profile image 
def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_f_name, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn )
	form_picture.save(picture_path)
	
	output_size = (125, 125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)

	i.save(picture_path)
	return picture_fn



# post image + save
def save_photo(form_photo):
	random_hex = secrets.token_hex(8)
	_f_name, f_ext = os.path.splitext(form_photo.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(current_app.root_path, 'static/post_pics', picture_fn )
	form_photo.save(picture_path)
	
	return picture_fn