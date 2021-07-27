

class InputMode():
    """ """

    def __init__(self, img, quote):
        
        self.img = img
        self.quote = quote
    
    def __repr__(self):
        return f'<{self.img}, {self.quote}'