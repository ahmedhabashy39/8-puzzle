class Board:
    def __init__(self, initialstate=[]):
        self.value = initialstate
        self.poszero = initialstate.index(0)

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)

    # If 0 is in the top most block, then up is invalid

    def up(self):
        pos = self.poszero
        if pos in (0, 1, 2):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos-3] = new_val[pos-3], new_val[pos]
            return new_val

    def down(self):
        pos = self.poszero
        if pos in (6, 7, 8):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos+3] = new_val[pos+3], new_val[pos]
            return new_val

    def left(self):
        pos = self.poszero
        if pos in (0, 3, 6):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos-1] = new_val[pos-1], new_val[pos]
            return new_val

 
    def right(self):
        pos = self.poszero
        if pos in (2, 5, 8):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos+1] = new_val[pos+1], new_val[pos]
            return new_val
