class Jar:
    def __init__(self, rusult):
        self.rusult=rusult
    def __call__(self):
        return self.rusult
