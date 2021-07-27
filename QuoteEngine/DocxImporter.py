"""Handling files with .docx extension"""

from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxImporter(IngestorInterface):
    """Implement parse() to read .docx files through doc module
    and a composition to QuoteModel class that defines the used pattern"""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """parse .docx file. Every row is encapsulated by QuoteModel obj.

        :path (str)       : system path to the file of interest
        :return (list)    : quote_list (List of QuoteModel objects).
                            every object encapsulate one line.
        """

        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quote_list = []
        doc = docx.Document(path)

        for paragraph in doc.paragraphs:

            if paragraph.text != "":
                parse = paragraph.text.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quote_list.append(new_quote)

        return quote_list
