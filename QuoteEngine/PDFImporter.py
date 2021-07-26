"""Handling files with .pdf extension"""

import subprocess
import os
import random

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFImporter(IngestorInterface):
    """Implement parse() to read .pdf files by calling an installed
    system program xpdf that converts pdf file to .txt file. It then
    utilizes a composition to QuoteModelclass which defines the
    used pattern"""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """parse .pdf file. Every row is encapsulated by QuoteModel obj.

        :path (str)       : system path to the file of interest
        :return (list)    : quote_list (List of QuoteModel objects).
                            every object encapsulate one line.
        """

        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        quote_list = []

        with open(tmp, 'r') as file_ref:

            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()

                if len(line) > 0:
                    parsed = line.split('-')
                    new_quote = QuoteModel(parsed[0], parsed[1])
                    quote_list.append(new_quote)

        os.remove(tmp)

        return quote_list
