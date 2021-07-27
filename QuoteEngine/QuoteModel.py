"""encapsulate body and author"""


class QuoteModel:

    def __init__(self, body: str, author: str) -> None:
        """initialization"""

        self.body = body
        self.author = author

    def __repr__(self):
        """machine friendly object print"""

        return f'<{self.body}, {self.author}'
