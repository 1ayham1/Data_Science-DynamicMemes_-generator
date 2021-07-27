""" dddd """

import os
import random
import argparse

import MemeEngine

from QuoteEngine import QuoteModel, Ingestor

class Meme():
    """ """

    def __init__(self, img=None, quote=None):
        """Generate default values for a meme given an path and a quote """

        


    @classmethod
    def generate_meme(self, path=None, body=None, author=None):
        """ Generate a meme given an path and a quote """
        

        img = self.img if path is None else path[0]
       
        if body is None:
            quote = self.quote
        else:
            if author is None:
                raise Exception('Author Required if Body is Used')
            quote = QuoteModel(body, author)


        path = self.get_meme_path(img, quote)

        
        return path


    def get_meme_path(self, img, quote):
        """ """

        meme = MemeEngine('./tmp')
        path = meme.make_meme(img, quote.body, quote.author)

        return path






if __name__ == "__main__":
    """parse the following CLI arguments
    
    -path - path to an image file
    -body - quote body to add to the image
    -author - quote author to add to the image """
    
    parser = argparse.ArgumentParser(description="please provide the path")
    parser.add_argument(
        '--path', type=str, default=None, help="path to desired image")
    parser.add_argument(
        '--body', type=str, default=None, help="quote to be added")
    parser.add_argument(
        '--author', type=str, default=None, help="quote author")

    args = parser.parse_args()
    path = args.path
    body = args.body
    author = args.author
    
    print(f'The following path: {path} by\n{author} and he wrote\n {body}')

    #print(generate_meme(args.path, args.body, args.author))
