import random

class grid:
    def __init__(self, n=3):
        """Generation of the base table"""
        self.n = n
        self.table = [[(i * n + i // n + j) % (n * n) + 1
                for j in range(n * n)] for i in range(n * n)]

    def transposing(self):
        self.table = list(map(list, zip(*self.table)))
        return self

    def swap_rows_small(self):
        tables = [self.table[i: i + self.n]
                  for i in range(0, self.n ** 2, self.n)]
        for table in tables:
            random.shuffle(table)
        self.table = [j for i in tables for j in i]
        return self

    def swap_colums_small(self):
        self.transposing()
        self.swap_rows_small()
        self.transposing()
        return self

    def swap_rows_area(self):
        tables = [self.table[i: i + self.n]
                  for i in range(0, self.n ** 2, self.n)]
        random.shuffle(tables)
        self.table = [j for i in tables for j in i]
        return self

    def swap_colums_area(self):
        self.transposing()
        self.swap_rows_area()
        self.transposing()
        return self

    def get_mixed_table(self):
        funs = ['self.transposing()', 
                'self.swap_rows_small()', 
                'self.swap_colums_small()', 
                'self.swap_rows_area()', 
                'self.swap_colums_area()']

        for _ in range(random.randint(1, 10)):
            eval(random.choice(funs))
        return self.table