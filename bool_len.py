class Notebook:

    def __init__(self,notes):
        self.notes = list(notes)

    def __getitem__(self, item):
        return self.notes[item]

    def __setitem__(self, key, value):
        if key >= 0:
            self.notes[key] = value

    def __delitem__(self, key):
        del self.notes[key]

bebra = Notebook([33, 45])

print(bebra[1])
