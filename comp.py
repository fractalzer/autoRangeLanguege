values = {}


def MOV(args):
    values[args[0]] = int(args[1])

def COPY(args):
    values[args[0]] = values[args[1]]

def WARP(args):
    values[args[0]],values[args[1]] = values[args[1]],values[args[0]]

def UTF(args):
    values[args[0]] = " ".join(args[1::])

def DEL(args):
    for arg in args:
        values.pop(arg)

def ADD(args):
    values[args[0]] += values[args[1]]

def SUB(args):
    values[args[0]] -= values[args[1]]

def MUL(args):
    values[args[0]] *= values[args[1]]

def DIV(args):
    values[args[0]] /= values[args[1]]

def IN(args):
    values[args[0]] = int(input(values[args[1]]))

def OUT(args):
    print(values[args[0]])

def AND(args):
    values[args[3]] = int(values[args[2]] == values[args[0]] and values[args[2]] == values[args[1]])

def OR(args):
    values[args[3]] = int(values[args[2]] == values[args[0]] or values[args[2]] == values[args[1]])

def NOT(args):
    values[args[2]] = int(values[args[0]] != values[args[1]])

def MAX(args):
    values[args[2]] = max(values[args[0]], values[args[1]])

def MIN(args):
    values[args[2]] = min(values[args[0]], values[args[1]])


commands = {
    "MOV": MOV, # Присвоить значение в регистр
    "COPY": COPY, # Скопировать значение регистра в другой регистр
    "WARP": WARP, # Поменять значения регистров местами
    "UTF": UTF, # Создать utf-8 строку, и сохранить ссылку в регистр
    "DEL": DEL, # Удалить регистр

    "ADD": ADD, # Прибавить к значению регистра значение другого регистра
    "SUB": SUB, # Вычесть из регистра значение другого регистра
    "MUL": MUL, # Умножить значение регистра на значение другого регистра
    "DIV": DIV, # Разделить значение регистра на значение другого регистра

    "IN" : IN, # Ввод значения в регистр с консоли
    "OUT": OUT, # Вывод значения регистра в консоль

    "AND": AND, # Является ли значение регистра и другого регистра значением третьего регистра, и записать резльтат в четвертый регистр
    "OR": OR, # Является ли значение регистра или другого регистра значением третьего регистра, и записать резльтат в четвертый регистр
    "NOT": NOT, # Невляется ли значение значением другого регистра, и записать резльтат в третий регистр

    "MAX": MAX, # Записать наибольшое значение из двух регистров в третий регистр
    "MIN": MIN # Записать наименьшее значение из двух регистров в третий регистр
}



code = open(
    input("FILENAME: ")+".ar",
    "r", encoding="utf-8"
).read().split("\n")

""" viev code """
for line in code:
    print(line)
print()

""" parse and work """
linecount = 0
for line in code:
    line = line.split(" ", 1)
    name = line[0]
    if name in commands:
        args = line[1].split(" ")

        try:
            linecount += 1
            commands[name](args)
        except KeyError:
            print(f"Error on line {linecount}")
            print("Line: "," ".join(line))
            print(f"Error: Not found command {name} or args {line[1]}")