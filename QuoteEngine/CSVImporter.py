"""Handling files with .csv extension"""

from typing import List
import pandas as pd

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVImporter(IngestorInterface):
    """Implement parse() to read .csv files through pandas data frame
    and a composition to QuoteModel class that defines the used pattern"""
    
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """parse .csv file. Every row is encapsulated by QuoteModel obj.
        
        :path (str)       : system path to the file of interest
        :return (list)    : quote_list (List of QuoteModel objects).
                            every object encapsulate one line.
        """

        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        quote_list=[]
        df = pd.read_csv(path,header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'],row['author'])
            quote_list.append(new_quote)
        
        return quote_list