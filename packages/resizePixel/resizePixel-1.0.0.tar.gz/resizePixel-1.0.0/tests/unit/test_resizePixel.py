from resizePixel.resizePixel import rpImage,reduce_qualtiy
from tests import *
from PIL import Image
import os

# image path
image_path = r"tests\img\test.png"
image_file = Image.open(image_path)
# open the image and check the current quality
my_image = rpImage(image_path,image_file)
oldpic_info = my_image.get_image_meta()

# I am saving in the same directory 
# img_path,img_name > C:\Users\mkshgh\Downloads, img.png
img_path,img_name = os.path.split(image_path)
output_img_name = 'output_'+img_name
# decrease quality explained above
# Use quality from 1 to 99; 99 being the best and 1 being the worst quality
# If the quality of the image is already low use 1 to 20; works great with larger files.
new_image = reduce_qualtiy(output_img_name,image_file,quality=50,outputdir=img_path)

def test_reduce_qualtiy():
    assert oldpic_info['size'] >= new_image['size']

def test_dimensions():
    assert oldpic_info['width'] == new_image['width']
    assert oldpic_info['height'] == new_image['height']
    
    