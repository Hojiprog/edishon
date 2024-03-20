#!/usr/bin/python3

def focus(gyt):
    gyt=gyt[6:]
    n='@'*len(gyt)

    focus = f'''
@@{n}@@
@@{gyt}@@
@@{n}@@
    '''
    return focus
