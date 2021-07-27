"""Handling Default inputs"""

import random
import os

from .InputInterface import InputInterface
from .InputModel import InputMode

from QuoteEngine import QuoteModel, Ingestor


class DefaultInput(InputInterface):
    """Implement generate_meme() to handle empty input"""

    @classmethod
    def generate_meme(cls, path: str,body: str, author: str):
        """generate meme when path,body, author are None

        :path (str)       : system path to the file of interest
        :body (str)       :
        :author (str)     :
        :return (list)    : quote_list (List of QuoteModel objects).
                            every object encapsulate one line.
        """

        images = "../_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)

        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                        './_data/DogQuotes/DogQuotesDOCX.docx',
                        './_data/DogQuotes/DogQuotesPDF.pdf',
                        './_data/DogQuotes/DogQuotesCSV.csv']
        
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))
        
        quote = random.choice(quotes)


        meme = MemeEngine('./tmp')
        path = meme.make_meme(img, quote.body, quote.author)

        return path
