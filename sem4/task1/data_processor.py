from functools import singledispatch


class DataProcessor:
    @singledispatch
    def process(self):
        pass
