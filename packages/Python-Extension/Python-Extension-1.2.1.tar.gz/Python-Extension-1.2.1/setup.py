import os

try:
    import lxml
except (ModuleNotFoundError, ImportError):
    os.system('pip3 install lxml')

from setuptools import *
from lxml import etree

html = '''
<!DOCTYPE html>
<html>
  <head>
    Brief Introduction
  </head>
  <p></p>
  <font size='2'>
    Python-Extension is an extension of Python,
It is divided into pyextension and tkextension,
tkextension is particularly powerful. 
  </font>
  <p></p>
  <head>
    Pyextension
  </head>
  <p></p>
  <font size='2'>
    Pyextension includes main modules
(open source function, computer information function and digital conversion function),
mathematical function processing module, password encryption module,
English Thesaurus module and Microsoft Word document processing module.
  </font>
  <p></p>
  <head>
    Tkextension
  </head>
  <p></p>
  <font size='2'>
    Tkextense includes dialog window,tix widget,
quick generation of Tkinter object,
quick document processing (open and save as),
open source module, about module,
small blackboard module, turtle graphics drawing module and timer module
  </font>
</html>
'''

html = etree.HTML(html)

setup(
    name = 'Python-Extension',
    version = '1.2.1',
    description = 'Python Extension Functions',
    long_description = html,
    license = 'GPL',
    author = 'Yile Wang',
    author_email = '36210280@qq.com',
    packages = find_packages(),
    python_requires = '>=2.5',
    package_requires = ['python-docx', 'lxml'],
    include_package_data = True
    )

