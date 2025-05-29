# lib/shoe.py

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        # backing attribute for validation
        self._size = None
        self.size = size
        # condition attribute is set when shoe is cobbled

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        # after repair, set condition and print message
        self.condition = "New"
        print("Your shoe is as good as new!")