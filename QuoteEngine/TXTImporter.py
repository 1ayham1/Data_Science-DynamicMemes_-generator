"""Handling files with .txt extension"""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TXTImporter(IngestorInterface):
    """Implement parse() to read .txt files through doc module
    and a composition to QuoteModel class that defines the used pattern"""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """parse .txt file. Every row is encapsulated by QuoteModel obj.

        :path (str)       : system path to the file of interest
        :return (list)    : quote_list (List of QuoteModel objects).
                            every object encapsulate one line.
        """

        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quote_list = []
 
        with open(path, 'r') as f:
            Lines = f.readlines()

            for line in Lines:
                body,author = line.strip().split('-')
                new_quote = QuoteModel(body, author)
                quote_list.append(new_quote)
   
        return quote_list
