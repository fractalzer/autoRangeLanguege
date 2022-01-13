import sys
sys.setrecursionlimit(2999)

class Main:
    def __init__(self) -> None:
        self.values = {}
        self.markers = {}
        self.linecount = 0
        self.commandsInit()

        self.code = open(
            input("FILENAME: ")+".ar",
            "r", encoding="utf-8"
        ).readlines()

        for line in self.code:
            print(line.replace("\n", ""))
        print()

        self.globalWorker()
    
    def globalWorker(self):
        for line in self.code:
            self.linecount += 1
            self.lineworker(line)

    def lineworker(self, line: str):
        name, args = self.linered(line)
        if name:
            self.commands[name](args)

    def linered(self, line: str) -> str:
        line = line.replace("\n", "")
        line = line.split(" ", 1)
        name = line[0]
        if name in self.commands:
            args = line[1].split(" ")
            return name, args
        return 0, 0

    """ commands """
    def commandsInit(self):
        self.commands = {
            "MOV": self.MOV, # Присвоить значение в регистр
            "COPY": self.COPY, # Скопировать значение регистра в другой регистр
            "WARP": self.WARP, # Поменять значения регистров местами
            "UTF": self.UTF, # Создать utf-8 строку, и сохранить ссылку в регистр
            "DEL": self.DEL, # Удалить регистр

            "ADD": self.ADD, # Прибавить к значению регистра значение другого регистра
            "SUB": self.SUB, # Вычесть из регистра значение другого регистра
            "MUL": self.MUL, # Умножить значение регистра на значение другого регистра
            "DIV": self.DIV, # Разделить значение регистра на значение другого регистра

            "IN" : self.IN, # Ввод значения в регистр с консоли
            "OUT": self.OUT, # Вывод значения регистра в консоль

            "AND": self.AND, # Является ли значение регистра и другого регистра значением третьего регистра, и записать резльтат в четвертый регистр
            "XAND": self.XAND, # Не является ли значение регистра и другого регистра значением третьего регистра, и записать резльтат в четвертый регистр
            "OR": self.OR, # Является ли значение регистра или другого регистра значением третьего регистра, и записать резльтат в четвертый регистр
            "XOR": self.XOR, # Не является ли значение регистра или другого регистра значением третьего регистра, и записать резльтат в четвертый регистр
            "NOT": self.NOT, # Невляется ли значение значением другого регистра, и записать резльтат в третий регистр
            "XNOT": self.XNOT, # Является ли значение значением другого регистра, и записать резльтат в третий регистр

            "MAX": self.MAX, # Записать наибольшое значение из двух регистров в третий регистр
            "MIN": self.MIN, # Записать наименьшее значение из двух регистров в третий регистр

            "GOTO": self.GOTO, # Отправить исполнение кода к строке указанной по индексу маркера, пока значение регистра не равно 0
            "MARKER": self.MARKER # Наметить строку как маркер для GOTO
        }

    def MOV(self, args):
        self.values[args[0]] = int(args[1])

    def COPY(self, args):
        self.values[args[0]] = self.values[args[1]]

    def WARP(self, args):
        self.values[args[0]],self.values[args[1]] = self.values[args[1]],self.values[args[0]]

    def UTF(self, args):
        self.values[args[0]] = " ".join(args[1::])

    def DEL(self, args):
        for arg in args:
            self.values.pop(arg)

    def ADD(self, args):
        self.values[args[0]] += self.values[args[1]]

    def SUB(self, args):
        self.values[args[0]] -= self.values[args[1]]

    def MUL(self, args):
        self.values[args[0]] *= self.values[args[1]]

    def DIV(self, args):
        self.values[args[0]] /= self.values[args[1]]

    def IN(self, args):
        self.values[args[0]] = int(input(self.values[args[1]]))

    def OUT(self, args):
        print(self.values[args[0]])

    def AND(self, args):
        self.values[args[3]] = int(self.values[args[2]] == self.values[args[0]] and self.values[args[2]] == self.values[args[1]])
    
    def XAND(self, args):
        self.values[args[3]] = int(self.values[args[2]] != self.values[args[0]] and self.values[args[2]] != self.values[args[1]])

    def OR(self, args):
        self.values[args[3]] = int(self.values[args[2]] == self.values[args[0]] or self.values[args[2]] == self.values[args[1]])
    
    def XOR(self, args):
        self.values[args[3]] = int(self.values[args[2]] != self.values[args[0]] or self.values[args[2]] != self.values[args[1]])

    def NOT(self, args):
        self.values[args[2]] = int(self.values[args[0]] != self.values[args[1]])
    
    def XNOT(self, args):
        self.values[args[2]] = int(self.values[args[0]] == self.values[args[1]])

    def MAX(self, args):
        self.values[args[2]] = max(self.values[args[0]], self.values[args[1]])

    def MIN(self, args):
        self.values[args[2]] = min(self.values[args[0]], self.values[args[1]])

    """ GoTo Markers """
    def MARKER(self, args):
        self.markers[args[0]] = self.linecount
    
    def GOTO(self, args):
        if self.values[args[1]] != 0:
            for ind in range(self.markers[args[0]], self.linecount):
                self.lineworker(self.code[ind])
                


if __name__ == '__main__':
    Main()