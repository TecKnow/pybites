class MultiplicationTable:

    def __init__(self, length: int):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self.length = length

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return pow(self.length, 2)

    def __str__(self):
        """Returns a string representation of the table"""
        table_list = [[str(row * column) for column in range(1, self.length+1)]
                      for row in range(1, self.length+1)]
        table_string = "\n".join([" | ".join(row) for row in table_list])
        return table_string

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        if 1 <= x <= self.length and 1 <= y <= self.length:
            return x * y
        else:
            raise IndexError()
