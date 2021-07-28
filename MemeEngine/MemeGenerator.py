"""Adds Quotes to Images"""

import random
import os

from PIL import Image, ImageFont, ImageDraw


class MemeEngine:
    """Read, Process, Add Quote and Save output image"""

    def __init__(self, output_dir):
        """saving resulting image"""

        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)

        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """return: generated image path

        REF: for adding text using pillow:
        https://stackoverflow.com/questions/16373425/add-text-on-image-using-pil
        """

        try:
            with Image.open(img_path) as im:

                # resize in place & maintain aspect ratio
                im_new_size = min(500, width)
                im.thumbnail((im_new_size, im_new_size), Image.ANTIALIAS)

                # Add text
                draw = ImageDraw.Draw(im)
                font = ImageFont.truetype("arial.ttf", 14, encoding="unic")

                im_y, im_x = im.size
                offset = 50
                x_pos = random.randint(offset, im_x - offset)
                y_pos = random.randint(offset, im_y - offset)

                quote_text = text + "\n --by " + author

                draw.text(
                    (x_pos, y_pos), quote_text,
                    (255, 0, 0), font=font)

                path_outputfile = (
                    f'{self.output_dir}/out_{random.randint(0, 1000000)}.jpeg')

                im.save(path_outputfile)

        except FileNotFoundError:
            print("file not found ...", img_path)

        return path_outputfile
