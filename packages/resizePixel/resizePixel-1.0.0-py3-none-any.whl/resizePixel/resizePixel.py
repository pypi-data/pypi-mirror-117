# Import the Images module from pillow
from PIL import Image
import os

class rpImage():

    def __init__(self,name:str,image_blob,path='/'):
        self.img_name = name
        self.img_blob = image_blob
        self.path = path

    def get_image_meta(self):
        width, height,  = self.img_blob.size
        size = str(len(self.img_blob.fp.read()))
        return {"name":self.img_name,
                "path": self.path,
                "width": width,
                "height":height,
                "size":size}


def reduce_qualtiy(output_filename,img_blob,outputdir,quality=25):
    # reduce
    my_file_locaion = os.path.join(outputdir,output_filename)
    img_blob.save(my_file_locaion, quality=quality)
    # new image
    new_img_blob = Image.open(my_file_locaion)
    img_obj = rpImage(output_filename,new_img_blob,path=outputdir)
    # return output
    return img_obj.get_image_meta()