import ply.lex as lex

tokens = [
    # MATRIX ELEMENT WISE OPERATORS
    'DOTADD',
    'DOTSUB',
    'DOTMUL',
    'DOTDIV',

    # EXTRA ASSIGNMENT OPERATORS
    'ADDASSIGN',
    'SUBASSIGN',
    'MULASSIGN',
    'DIVASSIGN',

    # RELATIONAL OPERATORS
    'LT',
    'GT',
    'LE',
    'GE',
    'NE',
    'EQ',

    # IDENTIFIERS
    'ID',
    'INTNUM',
    'FLOATNUM',
]

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',

    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',

    'eye': 'EYE',
    'zeros': 'ZEROS',
    'ones': 'ONES',

    'print': 'PRINT'
}

tokens += list(reserved.values())

t_DOTADD = r'\.\+'
t_DOTSUB = r'\.-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\./'

t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'/='

t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_NE = r'!='
t_EQ = r'=='

t_ignore = ' \t'


def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_FLOATNUM(t):
    r'\d+\.\d+([eE][\+-]?\d+)'
    t.value = float(t.value)
    return t


def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_COMMENT(t):
    r'\#.*'
    pass


def t_error(t):
    print("line %d: illegal character '%s'" % (t.lineno, t.value[0]))
    t.lexer.skip(1)


literals = ['+', '-', '*', '/', '(', ')', '[', ']', '{', '}', ':', '\'', ',', ';', '=']

lexer = lex.lex()


def find_column(input_data, token):
    line_start = input_data.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1
