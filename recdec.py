# -*- coding: utf-8 -*-

def variable():
    newstr = ""
    if len(words[0]) == 2:
        newstr = words[0][-1:]
        if newstr == ";":
            print newstr
            words[0] = words[0][1:]
        else:
            print "Invalid variable supplied"
    if len(words[0]) == 1:
        if words[0] == "a" or words[0] == "b" or words[0] == "c":
            print words[0]
            words.pop(0)
            if newstr == ";":
                words.insert(0, newstr)
    else:
        print "Invalid variable supplied"
    return

def digit():
    if words[0] == "0" or words[0] == "1" or words[0] == "2":
        print words[0]
        words.pop(0)
    else:
        print "Invalid digit supplied"
    return

def expr():
    print "Expression"
    if words[0] == "+" or words[0] == "*":
        print words[0]
        words.pop(0)
        expr()
        expr()
    else:
        if words[0].isdigit():
            digit()
        else:
            variable()
    return

def assign():
    variable()
    if words[0] == "=":
        print words[0]
        words.pop(0)
    else:
        print "Missing or invalid assignment operator"
    expr()
    return

def testexpr():
    print "Test expression"
    variable()
    if words[0] == "<=":
        print words[0]
        words.pop(0)
        expr()
    else:
        print "Invalid test expression"
    return

def whilestmt():
    print words[0]
    words.pop(0)
    testexpr()
    if words[0] == "do":
        print words[0]
        words.pop(0)
        stmt()
    else:
        print "Missing do action"
    return

def ifstmt():
    print words[0]
    words.pop(0)
    testexpr()
    if words[0] == "then":
        print words[0]
        words.pop(0)
        stmt()
        if words[0] == "else":
            print words[0]
            words.pop(0)
            stmt()
    else:
        print "Missing if condition"
    return

def morestmts():
    print "more statements"
    if words[0] == ";":
        words.pop(0)
        stmtlist()
    else:
        "Invalid operator"
    return

def stmt():
    print "Statement"
    if words[0] == "if":
        ifstmt()
    elif words[0] == "while":
        whilestmt()
    elif words[0] == "begin":
        block()
    else:
        assign()
    return

def stmtlist():
    print "Statement List"
    stmt()
    morestmts()
    return

def block():
    newstr = ""
    if words[0] == "begin":
        print words[0]
        words.pop(0)
        stmtlist()
        if len(words[0]) == 4:
            newstr = words[0][-1:]
            if newstr == "." or newstr == ";":
                words[0] = words[0][:3]
            else:
                print "Invalid variable supplied"
        if words[0] == "end":
            print words[0]
            words.pop(0)
            if newstr == "." or newstr == ";":
                words.insert(0, newstr)
        else:
            print "Missing end statement for block"
    else:
        print "Invalid program."
    return

def program():
    if words[0] == "program":
        print words[0]
        words.pop(0)
        block()
        if words[0] == ".":
            print "Program valid"
    else:
        print "Invalid program."
    return

import sys

data = sys.stdin.read()
words = data.split()
program()

