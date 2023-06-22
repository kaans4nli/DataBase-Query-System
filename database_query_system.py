from ast import Try
from asyncio.windows_events import NULL
from contextlib import nullcontext
import csv
from pickletools import markobject
from posixpath import split
from re import S
from sys import setswitchinterval
from traceback import print_tb
from unicodedata import name




students = dict()

with open("students.csv", "r") as my_file:
    # pass the file object to reader()
    file_reader = csv.reader(my_file, delimiter=";")
    # do this for all the rows
    splitted_header = next(file_reader)

    for row in file_reader:
        # print the rows
        student = dict()
        student[splitted_header[0]] = int(row[0])
        student[splitted_header[1]] = row[1]
        student[splitted_header[2]] = row[2]
        student[splitted_header[3]] = row[3]
        student[splitted_header[4]] = int(row[4])
        students[int(row[0])] = student
my_file.close()

students = dict(sorted(students.items(), key=lambda item: item[0]))  # for ASC
# reversed_students = dict(sorted(students.items(), reverse=True, key=lambda item: item[0]))  # for DSC
# print(students)


def asd(hname, hoperator):  # take operator
    if hname == "id":
        if hoperator == "=":
            return 0
        elif hoperator == "!=":
            return 1
        elif hoperator == "<":
            return 2
        elif hoperator == ">":
            return 3
        elif hoperator == "<=" or hoperator == "!>":
            return 4
        elif hoperator == ">=" or hoperator == "!<":
            return 5
    elif hname == "name":
        return 0
    elif hname == "lastname":
        return 0
    elif hname == "email":
        return 0
    elif hname == "grade":
        if hoperator == "=":
            return 0
        elif hoperator == "!=":
            return 1
        elif hoperator == "<":
            return 2
        elif hoperator == ">":
            return 3
        elif hoperator == "<=" or hoperator == "!>":
            return 4
        elif hoperator == ">=" or hoperator == "!<":
            return 5
    return -1


def asdf(fname, fvalue):  # Decide parameter
    if fname == "grade" or fname == "id":
        return int(fvalue)
    return str(fvalue)


def asdfg(fname, fvalue):  # get rid of quote
    if fname == "name" or fname == "lastname" or fname == "email":
        print(fvalue[1:len(fvalue) - 1])
        return fvalue[1:len(fvalue) - 1]
    return fvalue


def asdff(fname, index):  # for searches values
    if fname == "grade" or fname == "id":
        return int(students[int(index)].get(fname))
    return str(students[int(index)].get(fname)).lower()


def deleteValues(hname, hoperator, hvalue):

    op = asd(hname, hoperator)
    hvalue = asdf(hname, hvalue)
    hvalue = asdfg(hname, hvalue)

    for i in list(students):
        searched_value = asdff(hname, i)

        if op == 0 and searched_value == hvalue:
            print(students.pop(i), end=',')
        if op == 1 and searched_value != hvalue:
            print(students.pop(i), end=',')
        if op == 2 and searched_value < hvalue:
            print(students.pop(i), end=',')
        if op == 3 and searched_value > hvalue:
            print(students.pop(i), end=',')
        if op == 4 and searched_value <= hvalue:
            print(students.pop(i), end=',')
        if op == 5 and searched_value >= hvalue:
            print(students.pop(i), end=',')
        # print(end='\n')


def deleteandValues(hname, hoperator, hvalue, hname2, hoperator2, hvalue2):

    op1 = asd(hname, hoperator)
    op2 = asd(hname2, hoperator2)
    hvalue = asdf(hname, hvalue)
    hvalue2 = asdf(hname2, hvalue2)
    hvalue = asdfg(hname, hvalue)
    hvalue2 = asdfg(hname2, hvalue2)

    for i in list(students):
        searched_value = asdff(hname, i)
        searched_value2 = asdff(hname2, i)

        if op1 == 0 and op2 == 0 and searched_value == hvalue and searched_value2 == hvalue2:
            print(students.pop(i), end=',')
        if op1 == 0 and op2 == 1 and searched_value == hvalue and searched_value2 != hvalue2:
            print(students.pop(i), end=',')
        if op1 == 0 and op2 == 2 and searched_value == hvalue and searched_value2 < hvalue2:
            print(students.pop(i), end=',')
        if op1 == 0 and op2 == 3 and searched_value == hvalue and searched_value2 > hvalue2:
            print(students.pop(i), end=',')
        if op1 == 0 and op2 == 4 and searched_value == hvalue and searched_value2 <= hvalue2:
            print(students.pop(i), end=',')
        if op1 == 0 and op2 == 5 and searched_value == hvalue and searched_value2 >= hvalue2:
            print(students.pop(i), end=',')

        if op1 == 1 and op2 == 0 and searched_value != hvalue and searched_value2 == hvalue2:
            print(students.pop(i), end=',')
        if op1 == 1 and op2 == 1 and searched_value != hvalue and searched_value2 != hvalue2:
            print(students.pop(i), end=',')
        if op1 == 1 and op2 == 2 and searched_value != hvalue and searched_value2 < hvalue2:
            print(students.pop(i), end=',')
        if op1 == 1 and op2 == 3 and searched_value != hvalue and searched_value2 > hvalue2:
            print(students.pop(i), end=',')
        if op1 == 1 and op2 == 4 and searched_value != hvalue and searched_value2 <= hvalue2:
            print(students.pop(i), end=',')
        if op1 == 1 and op2 == 5 and searched_value != hvalue and searched_value2 >= hvalue2:
            print(students.pop(i), end=',')

        if op1 == 2 and op2 == 0 and searched_value < hvalue and searched_value2 == hvalue2:
            print(students.pop(i), end=',')
        if op1 == 2 and op2 == 1 and searched_value < hvalue and searched_value2 != hvalue2:
            print(students.pop(i), end=',')
        if op1 == 2 and op2 == 2 and searched_value < hvalue and searched_value2 < hvalue2:
            print(students.pop(i), end=',')
        if op1 == 2 and op2 == 3 and searched_value < hvalue and searched_value2 > hvalue2:
            print(students.pop(i), end=',')
        if op1 == 2 and op2 == 4 and searched_value < hvalue and searched_value2 <= hvalue2:
            print(students.pop(i), end=',')
        if op1 == 2 and op2 == 5 and searched_value < hvalue and searched_value2 >= hvalue2:
            print(students.pop(i), end=',')

        if op1 == 3 and op2 == 0 and searched_value > hvalue and searched_value2 == hvalue2:
            print(students.pop(i), end=',')
        if op1 == 3 and op2 == 1 and searched_value > hvalue and searched_value2 != hvalue2:
            print(students.pop(i), end=',')
        if op1 == 3 and op2 == 2 and searched_value > hvalue and searched_value2 < hvalue2:
            print(students.pop(i), end=',')
        if op1 == 3 and op2 == 3 and searched_value > hvalue and searched_value2 > hvalue2:
            print(students.pop(i), end=',')
        if op1 == 3 and op2 == 4 and searched_value > hvalue and searched_value2 <= hvalue2:
            print(students.pop(i), end=',')
        if op1 == 3 and op2 == 5 and searched_value > hvalue and searched_value2 >= hvalue2:
            print(students.pop(i), end=',')

        if op1 == 4 and op2 == 0 and searched_value <= hvalue and searched_value2 == hvalue2:
            print(students.pop(i), end=',')
        if op1 == 4 and op2 == 1 and searched_value <= hvalue and searched_value2 != hvalue2:
            print(students.pop(i), end=',')
        if op1 == 4 and op2 == 2 and searched_value <= hvalue and searched_value2 < hvalue2:
            print(students.pop(i), end=',')
        if op1 == 4 and op2 == 3 and searched_value <= hvalue and searched_value2 > hvalue2:
            print(students.pop(i), end=',')
        if op1 == 4 and op2 == 4 and searched_value <= hvalue and searched_value2 <= hvalue2:
            print(students.pop(i), end=',')
        if op1 == 4 and op2 == 5 and searched_value <= hvalue and searched_value2 >= hvalue2:
            print(students.pop(i), end=',')

        if op1 == 5 and op2 == 0 and searched_value >= hvalue and searched_value2 == hvalue2:
            print(students.pop(i), end=',')
        if op1 == 5 and op2 == 1 and searched_value >= hvalue and searched_value2 != hvalue2:
            print(students.pop(i), end=',')
        if op1 == 5 and op2 == 2 and searched_value >= hvalue and searched_value2 < hvalue2:
            print(students.pop(i), end=',')
        if op1 == 5 and op2 == 3 and searched_value >= hvalue and searched_value2 > hvalue2:
            print(students.pop(i), end=',')
        if op1 == 5 and op2 == 4 and searched_value >= hvalue and searched_value2 <= hvalue2:
            print(students.pop(i), end=',')
        if op1 == 5 and op2 == 5 and searched_value >= hvalue and searched_value2 >= hvalue2:
            print(students.pop(i), end=',')


def deleteorValues(hname, hoperator, hvalue, hname2, hoperator2, hvalue2):

    op1 = asd(hname, hoperator)
    op2 = asd(hname2, hoperator2)
    hvalue = asdf(hname, hvalue)
    hvalue2 = asdf(hname2, hvalue2)
    hvalue = asdfg(hname, hvalue)
    hvalue2 = asdfg(hname2, hvalue2)

    for i in list(students):
        searched_value = asdff(hname, i)
        searched_value2 = asdff(hname2, i)

        if op1 == 0 and op2 == 0 and searched_value == hvalue or searched_value2 == hvalue2:
            print(students.pop(i), end=',')
        if op1 == 0 and op2 == 1 and searched_value == hvalue or searched_value2 != hvalue2:
            print(students.pop(i), end=',')
        if op1 == 0 and op2 == 2 and searched_value == hvalue or searched_value2 < hvalue2:
            print(students.pop(i), end=',')
        if op1 == 0 and op2 == 3 and searched_value == hvalue or searched_value2 > hvalue2:
            print(students.pop(i), end=',')
        if op1 == 0 and op2 == 4 and searched_value == hvalue or searched_value2 <= hvalue2:
            print(students.pop(i), end=',')
        if op1 == 0 and op2 == 5 and searched_value == hvalue or searched_value2 >= hvalue2:
            print(students.pop(i), end=',')

        if op1 == 1 and op2 == 0 and searched_value != hvalue or searched_value2 == hvalue2:
            print(students.pop(i), end=',')
        if op1 == 1 and op2 == 1 and searched_value != hvalue or searched_value2 != hvalue2:
            print(students.pop(i), end=',')
        if op1 == 1 and op2 == 2 and searched_value != hvalue or searched_value2 < hvalue2:
            print(students.pop(i), end=',')
        if op1 == 1 and op2 == 3 and searched_value != hvalue or searched_value2 > hvalue2:
            print(students.pop(i), end=',')
        if op1 == 1 and op2 == 4 and searched_value != hvalue or searched_value2 <= hvalue2:
            print(students.pop(i), end=',')
        if op1 == 1 and op2 == 5 and searched_value != hvalue or searched_value2 >= hvalue2:
            print(students.pop(i), end=',')

        if op1 == 2 and op2 == 0 and searched_value < hvalue or searched_value2 == hvalue2:
            print(students.pop(i), end=',')
        if op1 == 2 and op2 == 1 and searched_value < hvalue or searched_value2 != hvalue2:
            print(students.pop(i), end=',')
        if op1 == 2 and op2 == 2 and searched_value < hvalue or searched_value2 < hvalue2:
            print(students.pop(i), end=',')
        if op1 == 2 and op2 == 3 and searched_value < hvalue or searched_value2 > hvalue2:
            print(students.pop(i), end=',')
        if op1 == 2 and op2 == 4 and searched_value < hvalue or searched_value2 <= hvalue2:
            print(students.pop(i), end=',')
        if op1 == 2 and op2 == 5 and searched_value < hvalue or searched_value2 >= hvalue2:
            print(students.pop(i), end=',')

        if op1 == 3 and op2 == 0 and searched_value > hvalue or searched_value2 == hvalue2:
            print(students.pop(i), end=',')
        if op1 == 3 and op2 == 1 and searched_value > hvalue or searched_value2 != hvalue2:
            print(students.pop(i), end=',')
        if op1 == 3 and op2 == 2 and searched_value > hvalue or searched_value2 < hvalue2:
            print(students.pop(i), end=',')
        if op1 == 3 and op2 == 3 and searched_value > hvalue or searched_value2 > hvalue2:
            print(students.pop(i), end=',')
        if op1 == 3 and op2 == 4 and searched_value > hvalue or searched_value2 <= hvalue2:
            print(students.pop(i), end=',')
        if op1 == 3 and op2 == 5 and searched_value > hvalue or searched_value2 >= hvalue2:
            print(students.pop(i), end=',')

        if op1 == 4 and op2 == 0 and searched_value <= hvalue or searched_value2 == hvalue2:
            print(students.pop(i), end=',')
        if op1 == 4 and op2 == 1 and searched_value <= hvalue or searched_value2 != hvalue2:
            print(students.pop(i), end=',')
        if op1 == 4 and op2 == 2 and searched_value <= hvalue or searched_value2 < hvalue2:
            print(students.pop(i), end=',')
        if op1 == 4 and op2 == 3 and searched_value <= hvalue or searched_value2 > hvalue2:
            print(students.pop(i), end=',')
        if op1 == 4 and op2 == 4 and searched_value <= hvalue or searched_value2 <= hvalue2:
            print(students.pop(i), end=',')
        if op1 == 4 and op2 == 5 and searched_value <= hvalue or searched_value2 >= hvalue2:
            print(students.pop(i), end=',')

        if op1 == 5 and op2 == 0 and searched_value >= hvalue or searched_value2 == hvalue2:
            print(students.pop(i), end=',')
        if op1 == 5 and op2 == 1 and searched_value >= hvalue or searched_value2 != hvalue2:
            print(students.pop(i), end=',')
        if op1 == 5 and op2 == 2 and searched_value >= hvalue or searched_value2 < hvalue2:
            print(students.pop(i), end=',')
        if op1 == 5 and op2 == 3 and searched_value >= hvalue or searched_value2 > hvalue2:
            print(students.pop(i), end=',')
        if op1 == 5 and op2 == 4 and searched_value >= hvalue or searched_value2 <= hvalue2:
            print(students.pop(i), end=',')
        if op1 == 5 and op2 == 5 and searched_value >= hvalue or searched_value2 >= hvalue2:
            print(students.pop(i), end=',')


def takeValues(hname, hoperator, hvalue, sname):

    split_selected_lines = sname.split(",")

    op = asd(hname, hoperator)
    hvalue = asdf(hname, hvalue)
    hvalue = asdfg(hname, hvalue)

    for i in students:
        searched_value = asdff(hname, i)

        for selectname in split_selected_lines:
            if op == 0 and searched_value == hvalue:
                print(students[int(i)].get(selectname), end=',')
            if op == 1 and searched_value != hvalue:
                print(students[int(i)].get(selectname), end=',')
            if op == 2 and searched_value < hvalue:
                print(students[int(i)].get(selectname), end=',')
            if op == 3 and searched_value > hvalue:
                print(students[int(i)].get(selectname), end=',')
            if op == 4 and searched_value <= hvalue:
                print(students[int(i)].get(selectname), end=',')
            if op == 5 and searched_value >= hvalue:
                print(students[int(i)].get(selectname), end=',')
        # print(end='\n')


def takeandValues(hname, hoperator, hvalue, hname2, hoperator2, hvalue2, sname):

    split_selected_lines = sname.split(",")

    op1 = asd(hname, hoperator)
    op2 = asd(hname2, hoperator2)
    hvalue = asdf(hname, hvalue)
    hvalue2 = asdf(hname2, hvalue2)
    hvalue = asdfg(hname, hvalue)
    hvalue2 = asdfg(hname2, hvalue2)

    for i in students:
        searched_value = asdff(hname, i)
        searched_value2 = asdff(hname2, i)

        for selectname in split_selected_lines:
            if op1 == 0 and op2 == 0 and searched_value == hvalue and searched_value2 == hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 0 and op2 == 1 and searched_value == hvalue and searched_value2 != hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 0 and op2 == 2 and searched_value == hvalue and searched_value2 < hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 0 and op2 == 3 and searched_value == hvalue and searched_value2 > hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 0 and op2 == 4 and searched_value == hvalue and searched_value2 <= hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 0 and op2 == 5 and searched_value == hvalue and searched_value2 >= hvalue2:
                print(students[int(i)].get(selectname), end=',')

            if op1 == 1 and op2 == 0 and searched_value != hvalue and searched_value2 == hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 1 and op2 == 1 and searched_value != hvalue and searched_value2 != hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 1 and op2 == 2 and searched_value != hvalue and searched_value2 < hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 1 and op2 == 3 and searched_value != hvalue and searched_value2 > hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 1 and op2 == 4 and searched_value != hvalue and searched_value2 <= hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 1 and op2 == 5 and searched_value != hvalue and searched_value2 >= hvalue2:
                print(students[int(i)].get(selectname), end=',')

            if op1 == 2 and op2 == 0 and searched_value < hvalue and searched_value2 == hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 2 and op2 == 1 and searched_value < hvalue and searched_value2 != hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 2 and op2 == 2 and searched_value < hvalue and searched_value2 < hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 2 and op2 == 3 and searched_value < hvalue and searched_value2 > hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 2 and op2 == 4 and searched_value < hvalue and searched_value2 <= hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 2 and op2 == 5 and searched_value < hvalue and searched_value2 >= hvalue2:
                print(students[int(i)].get(selectname), end=',')

            if op1 == 3 and op2 == 0 and searched_value > hvalue and searched_value2 == hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 3 and op2 == 1 and searched_value > hvalue and searched_value2 != hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 3 and op2 == 2 and searched_value > hvalue and searched_value2 < hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 3 and op2 == 3 and searched_value > hvalue and searched_value2 > hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 3 and op2 == 4 and searched_value > hvalue and searched_value2 <= hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 3 and op2 == 5 and searched_value > hvalue and searched_value2 >= hvalue2:
                print(students[int(i)].get(selectname), end=',')

            if op1 == 4 and op2 == 0 and searched_value <= hvalue and searched_value2 == hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 4 and op2 == 1 and searched_value <= hvalue and searched_value2 != hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 4 and op2 == 2 and searched_value <= hvalue and searched_value2 < hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 4 and op2 == 3 and searched_value <= hvalue and searched_value2 > hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 4 and op2 == 4 and searched_value <= hvalue and searched_value2 <= hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 4 and op2 == 5 and searched_value <= hvalue and searched_value2 >= hvalue2:
                print(students[int(i)].get(selectname), end=',')

            if op1 == 5 and op2 == 0 and searched_value >= hvalue and searched_value2 == hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 5 and op2 == 1 and searched_value >= hvalue and searched_value2 != hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 5 and op2 == 2 and searched_value >= hvalue and searched_value2 < hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 5 and op2 == 3 and searched_value >= hvalue and searched_value2 > hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 5 and op2 == 4 and searched_value >= hvalue and searched_value2 <= hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 5 and op2 == 5 and searched_value >= hvalue and searched_value2 >= hvalue2:
                print(students[int(i)].get(selectname), end=',')


def takeorValues(hname, hoperator, hvalue, hname2, hoperator2, hvalue2, sname):

    split_selected_lines = sname.split(",")

    op1 = asd(hname, hoperator)
    op2 = asd(hname2, hoperator2)
    hvalue = asdf(hname, hvalue)
    hvalue2 = asdf(hname2, hvalue2)
    hvalue = asdfg(hname, hvalue)
    hvalue2 = asdfg(hname2, hvalue2)

    for i in students:
        searched_value = asdff(hname, i)
        searched_value2 = asdff(hname2, i)

        for selectname in split_selected_lines:
            if op1 == 0 and op2 == 0 and searched_value == hvalue or searched_value2 == hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 0 and op2 == 1 and searched_value == hvalue or searched_value2 != hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 0 and op2 == 2 and searched_value == hvalue or searched_value2 < hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 0 and op2 == 3 and searched_value == hvalue or searched_value2 > hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 0 and op2 == 4 and searched_value == hvalue or searched_value2 <= hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 0 and op2 == 5 and searched_value == hvalue or searched_value2 >= hvalue2:
                print(students[int(i)].get(selectname), end=',')

            if op1 == 1 and op2 == 0 and searched_value != hvalue or searched_value2 == hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 1 and op2 == 1 and searched_value != hvalue or searched_value2 != hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 1 and op2 == 2 and searched_value != hvalue or searched_value2 < hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 1 and op2 == 3 and searched_value != hvalue or searched_value2 > hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 1 and op2 == 4 and searched_value != hvalue or searched_value2 <= hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 1 and op2 == 5 and searched_value != hvalue or searched_value2 >= hvalue2:
                print(students[int(i)].get(selectname), end=',')

            if op1 == 2 and op2 == 0 and searched_value < hvalue or searched_value2 == hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 2 and op2 == 1 and searched_value < hvalue or searched_value2 != hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 2 and op2 == 2 and searched_value < hvalue or searched_value2 < hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 2 and op2 == 3 and searched_value < hvalue or searched_value2 > hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 2 and op2 == 4 and searched_value < hvalue or searched_value2 <= hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 2 and op2 == 5 and searched_value < hvalue or searched_value2 >= hvalue2:
                print(students[int(i)].get(selectname), end=',')

            if op1 == 3 and op2 == 0 and searched_value > hvalue or searched_value2 == hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 3 and op2 == 1 and searched_value > hvalue or searched_value2 != hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 3 and op2 == 2 and searched_value > hvalue or searched_value2 < hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 3 and op2 == 3 and searched_value > hvalue or searched_value2 > hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 3 and op2 == 4 and searched_value > hvalue or searched_value2 <= hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 3 and op2 == 5 and searched_value > hvalue or searched_value2 >= hvalue2:
                print(students[int(i)].get(selectname), end=',')

            if op1 == 4 and op2 == 0 and searched_value <= hvalue or searched_value2 == hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 4 and op2 == 1 and searched_value <= hvalue or searched_value2 != hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 4 and op2 == 2 and searched_value <= hvalue or searched_value2 < hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 4 and op2 == 3 and searched_value <= hvalue or searched_value2 > hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 4 and op2 == 4 and searched_value <= hvalue or searched_value2 <= hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 4 and op2 == 5 and searched_value <= hvalue or searched_value2 >= hvalue2:
                print(students[int(i)].get(selectname), end=',')

            if op1 == 5 and op2 == 0 and searched_value >= hvalue or searched_value2 == hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 5 and op2 == 1 and searched_value >= hvalue or searched_value2 != hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 5 and op2 == 2 and searched_value >= hvalue or searched_value2 < hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 5 and op2 == 3 and searched_value >= hvalue or searched_value2 > hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 5 and op2 == 4 and searched_value >= hvalue or searched_value2 <= hvalue2:
                print(students[int(i)].get(selectname), end=',')
            if op1 == 5 and op2 == 5 and searched_value >= hvalue or searched_value2 >= hvalue2:
                print(students[int(i)].get(selectname), end=',')


while True:
    inpt = input()
    user_input = inpt.lower()

    if inpt == "exit":
        break

    if user_input[3:] == "asc":  # if ASC entered
        students = dict(sorted(students.items(), key=lambda item: item[0]))
    elif user_input[3:] == "dsc":  # if DSC entered
        reversed_students = dict(
            sorted(students.items(), reverse=True, key=lambda item: item[0]))
        students = reversed_students

    split_line = str(user_input).split(" ")
    # SELECT
    if split_line[0] == "select" and split_line[2] == "from" and split_line[3] == "students" and split_line[4] == "where":
        # none AND, OR
        if split_line[8] != "and" and split_line[8] != "or":
            header = split_line[5]
            header_operator = split_line[6]
            header_value = split_line[7]

            takeValues(header, header_operator,
                       header_value, split_line[1])
        # entered AND
        elif split_line[8] == "and":
            header1 = split_line[5]
            header1_operator = split_line[6]
            header1_value = split_line[7]
            header2 = split_line[9]
            header2_operator = split_line[10]
            header2_value = split_line[11]

            takeandValues(header1, header1_operator, header1_value,
                          header2, header2_operator, header2_value, split_line[1])
        # entered OR
        elif split_line[8] == "or":
            header1 = split_line[5]
            header1_operator = split_line[6]
            header1_value = split_line[7]
            header2 = split_line[9]
            header2_operator = split_line[10]
            header2_value = split_line[11]

            takeorValues(header1, header1_operator, header1_value,
                         header2, header2_operator, header2_value, split_line[1])
    # INSERT
    elif split_line[0] == "insert" and split_line[1] == "into" and split_line[2] == "student":
        index = user_input.index("values(") + 7
        value = user_input[index:len(user_input) - 1]
        splitted_value = value.split(",")

        students_len = len(students) + 1
        temp = dict()
        temp[splitted_header[0]] = students_len
        temp[splitted_header[1]] = students[int(splitted_value[0])].get("name")
        temp[splitted_header[2]] = students[int(
            splitted_value[0])].get("lastname")
        temp[splitted_header[3]] = students[int(
            splitted_value[0])].get("email")
        temp[splitted_header[4]] = students[int(
            splitted_value[0])].get("grade")
        students[int(students_len)] = temp

        student = dict()
        student[splitted_header[0]] = int(splitted_value[0])
        student[splitted_header[1]] = splitted_value[1]
        student[splitted_header[2]] = splitted_value[2]
        student[splitted_header[3]] = splitted_value[3]
        student[splitted_header[4]] = int(splitted_value[4])
        students[int(splitted_value[0])] = student
    # DELETE
    elif split_line[0] == "delete" and split_line[1] == "from" and split_line[2] == "student" and split_line[3] == "where":
        # none AND, OR
        if len(split_line) < 8:
            header = split_line[4]
            header_operator = split_line[5]
            header_value = split_line[6]

            deleteValues(header, header_operator, header_value)
        # entered AND
        elif split_line[7] == "and":
            header1 = split_line[4]
            header1_operator = split_line[5]
            header1_value = split_line[6]
            header2 = split_line[8]
            header2_operator = split_line[9]
            header2_value = split_line[10]

            deleteandValues(header1, header1_operator, header1_value,
                            header2, header2_operator, header2_value)
        # entered OR
        elif split_line[7] == "or":
            header1 = split_line[4]
            header1_operator = split_line[5]
            header1_value = split_line[6]
            header2 = split_line[8]
            header2_operator = split_line[9]
            header2_value = split_line[10]

            deleteorValues(header1, header1_operator, header1_value,
                           header2, header2_operator, header2_value)
