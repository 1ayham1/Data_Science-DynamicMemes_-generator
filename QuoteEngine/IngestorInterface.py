""" Strategy to dynamically enable different file import behaviors

Following open/closed principle (OCP), IngestorInterface (acting as
Strategy Interface), encapsulates various import file behaviors which
is resolved in real time. This enable flexible expansion to any new
desired extension and decouples the desired behavior and the class
that uses that behavior.

The Strategy classes (CSVImporter, PDFImporter ...) encapsulate 
specific implementation by using can_ingest() and overridding
the abstract method parse(). 
"""

from abc import ABC, abstractmethod

from typing import List
from .QuoteModel import QuoteModel
class IngestorInterface(ABC):
    """Strategy for parsing various file formats"""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls,path):
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions
    
    @classmethod
    @abstractmethod
    def parse(cls,path: str) -> List(QuoteModel):
        pass