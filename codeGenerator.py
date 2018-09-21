from random import randint
import string
import random


def generate_gosub():
    letters = string.ascii_letters
    char = random.choice(letters)
    code = 'GOSUB ' + char + '\n'
    return code


def generate_arithmetic():
    items = ['+', '-', '/', '*']
    arith = items[random.randrange(len(items))]
    code = str(randint(0, 9)) + ' ' + arith + ' ' + str(randint(0, 9))
    if randint(1, 10) > 5:
        code += generate_arithmetic()
    return code


def generate_assignment(terminator=True, indent=True):
    val = randint(0, 9)
    letters = string.ascii_letters
    char = random.choice(letters)
    if randint(1, 10) > 5:
        code = char + ' ' + ':=' + ' ' + str(val)
    else:
        code = char + ' ' + ':=' + ' ' + generate_arithmetic()
    if terminator:
        code += ';\n'
        if randint(1, 10) > 5:
            if indent:
                code += '\t' + 'PRINT ' + char + ';\n'
            else:
                code += 'PRINT ' + char + ';\n'
    return code


def generate_condition(assignments):
    assignment = generate_assignment(False)
    code = 'IF ' + assignment + ' THEN\n'
    for j in range(assignments):
        code += '\t' + generate_assignment()
    code += 'ENDIF;\n'
    return code


def generate_loop(assignments):
    val = randint(0, 9)
    letters = string.ascii_letters
    char = random.choice(letters)
    code = 'FOR ' + char + ' := ' + str(val) + ' TO ' + str(randint(val, val+9)) + '\n'
    for j in range(assignments):
        code += '\t' + generate_assignment()
    code += 'NEXT ' + char + ';' + '\n'
    return code


def generate_return():
    letters = string.ascii_letters
    char = random.choice(letters)
    code = 'RETURN ' + char + ';\n'
    return code


def generate_file(count=None):
    if count is None:
        count = randint(5, 14)
    code = ''
    for i in range(count):
        j = randint(1, 4)
        assignments = randint(1, 5)
        if j == 1:
            code += generate_assignment(True, False)
        elif j == 2:
            code += generate_condition(assignments)
        elif j == 3:
            code += generate_loop(assignments)
        elif j == 4:
            code += generate_gosub()
    if randint(1, 10) > 5:
        code += generate_return()
    return code


numberOfFiles = 100
sameCodeExists = True
if sameCodeExists:
    sameCode = generate_file(3)
else:
    sameCode = ''
for counter in range(numberOfFiles):
    codeToWrite = generate_file()
    file = open('input/sample/file-' + str(counter) + '.txt', 'w')
    file.write(sameCode)
    file.write(codeToWrite)
    file.close()
