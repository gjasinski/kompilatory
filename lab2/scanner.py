#!/usr/bin/python
# Author: Grzegorz Jasinski
import ply.lex as lex;
import ply.yacc as yacc;

reserved = {
    'if'    :   'IF',
    'else'  :   'ELSE',
    'for'   :   'FOR',
    'while' :   'WHILE',
    'break' :   'BREAK',
    'continue'  : 'CONTINUE',
    'return'    : 'RETURN',
    'eye'   : 'EYE',
    'zeros' :   'ZEROS',
    'ones'  :   'ONES',
    'print' :   'PRINT'
}

tokens = ['DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV',
   'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN',
    'SMALLEROP', 'SMALLEROREQOP', 'BIGGEROP', 'BIGGEROREQOP', 'NOTEQOP', 'EQOP',
    'ID',
    'INTNUM', 'FLOATINPOINTNUM',
    'NEWLINE', 'ERROR', "COMMENT"
 ] + list(reserved.values())

literals = "+-*/()[]{}:'<>=,;"

t_DOTADD    = r'\.\+'
t_DOTSUB   = r'\.-'
t_DOTMUL   = r'\.\*'
t_DOTDIV  = r'\./'
t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'/='
t_SMALLEROP = r'<'
t_SMALLEROREQOP = r'<='
t_BIGGEROP = r'>'
t_BIGGEROREQOP = r'>='
t_NOTEQOP = r'!='
t_EQOP = r'=='
t_ignore = '  \t'

def t_COMMENT(t):
    r'\#.*'
    pass

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_FLOATINPOINTNUM(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t) :
    print "Ln " + str(t.lexer.lineno) + " Illegal character '" + str(t.value[0]) + "'"
    t.lexer.skip(1)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

lexer = lex.lex()