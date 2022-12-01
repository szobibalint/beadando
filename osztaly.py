import random
import nevek


class Nev:
    vezeteknev = ""
    nev = ""
    nem = ""
    vezeteknev_sorsolas = None
    fiu_sorsolas = None
    lany_sorsolas = None

    def __init__(self):
        self.vezeteknev_sorsolas = False
        self.fiu_sorsolas = False
        self.lany_sorsolas = False

    def veznevgenerator(self):
        veznev = []
        self.vezeteknev = ""
        if self.vezeteknev_sorsolas:
            veznev = veznev + nevek.vezeteknevek
            self.vezeteknev = self.vezeteknev + veznev[random.randint(0, len(veznev) - 1)]
        else:
            self.vezeteknev = ""
        return self.vezeteknev

    def nevgenerator(self):
        lista = []
        self.nev = ""
        if self.lany_sorsolas or self.fiu_sorsolas:
            if self.lany_sorsolas:
                lista = lista + nevek.lany_nev
            if self.fiu_sorsolas:
                lista = lista + nevek.fiu_nev
            self.nev = self.nev + lista[random.randint(0, len(lista) - 1)]
        else:
            self.nev = ""
        return self.nev

    def f_vagy_l(self):
        self.nem = ""
        if self.lany_sorsolas:
            self.nem = "Női"
        if self.fiu_sorsolas:
            self.nem = "Férfi"
        return self.nem


n = Nev()
print(n.veznevgenerator())
print(n.nevgenerator())
print(n.f_vagy_l())
