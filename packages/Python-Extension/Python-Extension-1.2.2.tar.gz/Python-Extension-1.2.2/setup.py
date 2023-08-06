from setuptools import *

text = '''
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

setup(
    name = 'Python-Extension',
    version = '1.2.2',
    description = 'Python Extension Functions',
    long_description = text,
    license = 'GPL',
    author = 'Yile Wang',
    author_email = '36210280@qq.com',
    packages = find_packages(),
    python_requires = '>=2.5',
    package_requires = ['python-docx'],
    include_package_data = True
    )

