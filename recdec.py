# -*- coding: utf-8 -*-

def variable():
    if words[0] == "a" or words[0] == "b" or words[0] == "c":
        print words[0]
        variables.append(words[0])
        words.pop(0)
    else:
        print "Invalid variable supplied"
        exit()
    return

def digit():
    if words[0] == "0" or words[0] == "1" or words[0] == "2":
        print words[0]
        words.pop(0)
    else:
        print "Invalid digit supplied"
        exit()
    return

def expr():
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
        assignments.append(words[0])
        words.pop(0)
    else:
        print "Missing or invalid assignment operator"
        exit()
    expr()
    return

def testexpr():
    variable()
    if words[0] == "<=":
        print words[0]
        words.pop(0)
        expr()
    else:
        print "Invalid test expression"
        exit()
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
        exit()
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
        exit()
    return

def morestmts():
    if words[0] == ";":
        words.pop(0)
        stmtlist()
    return

def stmt():
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
    stmt()
    morestmts()
    return

def block():
    if words[0] == "begin":
        print words[0]
        words.pop(0)
        stmtlist()
        if words[0] == "end":
            print words[0]
            words.pop(0)
        else:
            print "Missing end statement for block"
            exit()
    else:
        print "Invalid program."
        exit()
    return

def program():
    if words[0] == "program":
        print words[0]
        words.pop(0)
        block()
        if words[0] != ".":
            print "Invalid program."
            exit()
    return

# Read in file input
import sys

data = sys.stdin.read()
words = data.split()
for index, word in enumerate(words):
    if len(word) > 1:
        if word[-1:] == ";" or word[-1:] == ".":
            words[index] = word[:-1]
            words.insert(index + 1, word[-1:])

# Handle tracking assignments and variables
assignments = []
variables = []

# Parse
program()

# Print output
print str(len(assignments)) + " assignments, " + str(len(variables)) + " variable references."

