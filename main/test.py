# @Time : 2019/12/2 17:41
# @Author : YLXY
# @File : test.py
# -*- coding: utf-8 -*-

import sys

def Print( *args ):

    Temp_Frame = sys._getframe(1)

    filename = Temp_Frame.f_code.co_filename
    funcname = Temp_Frame.f_code.co_name
    lineno = Temp_Frame.f_lineno


    print( *args, 'File "{}", line {}, in {}'.format( filename, lineno, funcname) )

a = [1,2,3]
b = 2
Print(a,b)


