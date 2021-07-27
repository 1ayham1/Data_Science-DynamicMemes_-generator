"""
The project defines a MemeGenerator module with the following responsibilities:



- Add a caption to an image (string input) with a body
 and author to a random location on the image.
-The class depends on the Pillow library to complete the defined,
 incomplete method signatures so that they work with JPEG/PNG files.

-The method signature to make the meme should be: 
make_meme(self, img_path, text, author, width=500) -> str #generated image path

"""

from PIL import Image, ImageFont, ImageDraw 
import random

class MemeGenerator:
    """ ddd """
    
    def __init__(self,output_dir):
        """saving resulting image"""

        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """return: generated image path
        
        #REF: add_text : (https://stackoverflow.com/questions/16373425/add-text-on-image-using-pil)
        """
        
        try:
            with Image.open(img_path) as im:

                #resize in place & maintain aspect ratio
                im_new_size = min(500,width)
                im.thumbnail((im_new_size,im_new_size), Image.ANTIALIAS)

                #Add text
                draw = ImageDraw.Draw(im)
                font = ImageFont.load_default()
                #font = ImageFont.truetype("times-ro.ttf", 24)
                
                im_y, im_x = im.size
                offset = 10
                x_pos = random.randint(offset,im_x-offset)
                y_pos = random.randint(offset,im_y-offset)
                quote_text = f"{text}...\n\t\t  --by {author}"

                draw.text(
                    (x_pos, y_pos), quote_text,
                    (0,255,0),font=font,align ="right")
                
                path_outputfile = f'{self.output_dir}/out_{random.randint(0, 1000000)}.jpeg'

                im.save(path_outputfile)
        
        except FileNotFoundError:
            print("file not found ...", img_path)

        return path_outputfile