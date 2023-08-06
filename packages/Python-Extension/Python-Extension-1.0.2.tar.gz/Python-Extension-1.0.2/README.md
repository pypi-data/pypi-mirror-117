This is a extension of Python 3.10 or more later.

Caution
========== ========== ========== ========== ==========
This library is for Python 3.10 or more later,
so you can’t install it at Python 3.9 or more older.

License
========== ========== ========== ========== ==========
Copyright (C) 2021 Yile WangThis program is free software: you can redistribute it and/or modifyit under the terms of the GNU Affero General Public License aspublished by the Free Software Foundation, either version 3 of theLicense, or (at your option) any later version.This program is distributed in the hope that it will be useful,but WITHOUT ANY WARRANTY; without even the implied warranty ofMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See theGNU Affero General Public License for more details.

Functions
========== ========== ========== ========== ==========

pyextension
========== ========== ========== ==========
1. askvalue(title=‘’, msg=‘’, arg=(0, 100))
If args are string,
it will create a tkinter window with title, msg
and a Spinbox that can choose a item in args.

If args are two int,
it will create a tkinter window with title, msg
and a Spinbox that can choose numbers between two int


2. askitem(title=‘’, msg=‘’, items=[], number=1, normal=0)
It will create a tkinter window with title, msg
and a Listbox that can choose things in the items.

The number of the things can choose depends on argument : number
And ‘normal’ means if you do not do anythings before enter,
the choosen item will be the index ‘normal’ in list ‘items’