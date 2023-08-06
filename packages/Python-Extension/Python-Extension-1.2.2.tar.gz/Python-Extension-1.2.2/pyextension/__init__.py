def floating_point_numbers_retain_decimal_digit(x, decimal_digit=2):
    dd = decimal_digit
    a = 10 ** dd * x
    a = int(a)
    a /= 10 ** dd
    return a

def floatdd(x, decimal_digit=2):
    return floating_point_numbers_retain_decimal_digit(x, decimal_digit)

import platform as p
import sys

def computer():
    print('===== %s =====' % p.node())
    print('''OS:
    %s''' % p.system())
    print('''Processor:
    %s''' % p.processor())
    print('''Machine:
    %s''' % p.machine())
    print('''Release:
    %s''' % p.release())
    print('''Platform:
    %s''' % p.platform())
    print('''Version:
    %s''' % p.version())

def python():
    print('===== Python ' + str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.' + str(sys.version_info[2]) + ' =====')
    print('''Version : ''')
    print(4 * ' ',end='')
    print(sys.version)
    print('''Build :
    ''',end='')
    print(p.python_build())

import pickle

def opensource(module='pyextension'):
    if module == 'pyextension':
        file = open('__init__.py')
        get = file.read()
        file.close()
        return get
    elif module == 'password':
        file = open('password.py')
        get = file.read()
        file.close()
        return get
    elif module == 'math':
        file = open('math.py')
        get = file.read()
        file.close()
        return get
    elif module == 'word bank' or module == 'word_bank':
        file = open('word_bank/__init__.py')
        get = file.read()
        file.close()
        return get
    elif module == 'word bank data':
        file = open('word_bank/wordbank.dat.py', 'rb')
        get = pickle.load(file)
        file.close()
        return get
    elif module == 'word':
        file = open('word.py')
        get = file.read()
        file.close()
        return get
    else:
        raise AttributeError('\'opensource\' object has no attribute \'%s\'' % module)

def license():
    file = open('LICENSE.py')
    get = file.read()
    file.close()
    return get

def description():
    return '''
Brief Introduction

Python-Extension is an extension of Python,
It is divided into pyextension and tkextension,
tkextension is particularly powerful. 


Pyextension

Pyextension includes main modules
(open source function, computer information function and digital conversion function),
mathematical function processing module, password encryption module,
English Thesaurus module and Microsoft Word document processing module.


Tkextension

Tkextense includes dialog window,tix widget,
quick generation of Tkinter object,
quick document processing (open and save as),
open source module, about module,
small blackboard module, turtle graphics drawing module and timer module
'''
