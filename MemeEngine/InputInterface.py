"""Strategy to dynamically enable different input behaviors"""


from abc import ABC, abstractmethod
#from .InputModel import InputModel

class InputInterface(ABC):
    """Strategy for handling various interactive inputs"""

    @classmethod
    @abstractmethod
    def generate_meme(cls, path: str,body: str, author: str):
        pass


''' 
class IngestorInterface(ABC):
    """Strategy for parsing various file formats"""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """extract file extension from a path

        :path (str)    : system path to file of interest
        :return (bool) : real time check if the extension has
                        a strategy that implements the desired behavior
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
'''