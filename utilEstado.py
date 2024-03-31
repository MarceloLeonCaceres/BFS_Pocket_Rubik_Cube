class Estado(object):
    def __init__(self, tupla):
        self.tupla = tupla

    def __eq__(self, other):
        for i in range(23):
            if self.tupla[i] != other.tupla[i]:
                return False
        return True
        
    def __lt__(self, other):
        for i in range(23):
            if self.tupla[i] < other.tupla[i]:
                return True
            elif self.tupla[i] > other.tupla[i]:
                return False
        return True