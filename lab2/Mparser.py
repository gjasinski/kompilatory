#!/usr/bin/python

import sys
import pprint
import ply.yacc as yacc

import classes
import scanner

tokens = scanner.tokens

precedence = (
        ("nonassoc", 'IF'),
        ("nonassoc", 'ELSE'),
        ("right", '=', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
        ("nonassoc", '<', '>', 'EQOP', 'NOTEQOP', 'SMALLEROREQOP', 'BIGGEROP'),
        ("left", '+', '-'),
        ("left", '*', '/'),
        ("left", 'DOTADD', 'DOTSUB'),
        ("left", 'DOTMUL', 'DOTDIV')
)


def p_error(p):
    if p:
        print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, scanner.find_tok_column(p), p.type, p.value))
    else:
        print("Unexpected end of input")


def p_file(p):
    ''' file : instructions '''
    p[0] = p[1]

def p_instructions_1(p):
    """instructions : instructions instruction"""
    p[0] = classes.Instructions(p[1], p[2])

def p_instructions_2(p):
    """instructions : instruction ';'"""
    p[0] = classes.Instructions(None, p[1])

def p_instruction(p):
    """ instruction : assignment_instruction
        | print_instruction
        | return_instruction
        | break_instruction
        | continue_instruction
        | for_instruction
        | while_instruction
        | choice_instruction"""
    p[0] = p[1]

def p_break_instruction(p):
    """break_instruction : BREAK"""
    p[0] = classes.Break()

def p_continue_instruction(p):
    """continue_instruction : CONTINUE"""
    p[0] = classes.Continue()

def p_return_instruction(p):
    """return_instruction : RETURN expression"""
    p[0] = classes.ReturnInstruction(p[2])

def p_print_instruction(p):
    """print_instruction : PRINT print_expressions ';' """
    p[0] = classes.PrintInstruction(p[2])

def p_print_expressions(p):
    """print_expressions : print_expressions print_expression
                            | print_expression"""
    if len(p) > 2:
        p[0] = classes.PrintExpressions(p[1], p[2])
    else:
        p[0] = classes.PrintExpressions(None, p[1])
    
def p_print_expression(p):
    """print_expression : STRING 
                        | expression"""
    p[0] = classes.PrintExpression(p[2])

def p_expression(p):
    """expression : bin_expression 
                | un_expression 
                | constant 
                | matrix_init_fun"""
    p[0] = p[1]

def p_matrix_init_fun_zeros(p):
    """matrix_init_fun : ZEROS '(' expression ')'"""
    p[0] = classes.ZerosInitMatrix(p[3])

def p_matrix_init_fun_ones(p):
    """matrix_init_fun : ONES '(' expression ')'"""
    p[0] = classes.OnesInitMatrix(p[3])

def p_matrix_init_fun_eye(p):
    """matrix_init_fun : EYE '(' expression ')'"""
    p[0] = classes.EyeInitMatrix(p[3])

def p_id_expr(p):
    """expression : ID"""


def p_const_expr(p):
    """expression : const"""


def p_paren_expression(p):
    """expression : '(' expression ')'"""


def p_bin_expression(p):
    """expression : expression '+' expression
            | expression '-' expression
            | expression '*' expression
            | expression '/' expression
            | expression '<' expression
            | expression '>' expression
            | expression SMALLEROP expression
            | expression BIGGEROP expression
            | expression NOTEQOP expression
            | expression EQOP expression
            | expression DOTADD expression
            | expression DOTSUB expression
            | expression DOTMUL expression
            | expression DOTDIV expression"""
    p[0] = classes.BinaryExpression(p[2], p[1], p[3])

def p_constant(p):
    """constant : FLOAT
                | INT
                | matrix_initialization"""
    p[0] = p[1]

def p_matrix_initialization(p):
    """matrix_initialization : '[' expression ';' expression ']'
                            | '[' expression ']'"""
    if len(p) > 4:
        p[0] = classes.MatrixInitializer(p[2], p[3])
    else:
        p[0] = classes.MatrixInitializer(None, p[2])

def p_unary_expression_div(p):
    """un_expression : expression '\'"""
    p[0] = classes.UnaryExprssion(p[2], p[1])

def p_unary_expression_sub(p):
    """un_expression : '-' expression"""
    p[0] = classes.UnaryExprssion(p[1], p[2])

def p_assign_instr_end(p):
    """assign_instr : variable assign_block expression"""
    p[0] = classes.EndAssignment(p[1], p[2], p[3])

def p_assign_instr_midle(p):
    """assign_instr : variable assign_block assign_instr"""
    p[0] = classes.MiddleAssignment(p[1], p[2], p[3])


def p_variable(p):
    """variable : ID 
                | ID '[' matrix_reference ']'"""
    if len(p) == 2:
        p[0] = classes.Variable(p[1])
    else:
        p[0] = classes.MatrixReference(p[1], p[3])

def p_matrix_reference(p):
    """matrix_reference : locations expression
                    | expression"""
    if len(p) > 2:
        p[0] = classes.MatrixLocations(p[1], p[2])
    else:
        p[0] = classes.MatrixLocations(None, p[2])

def p_assign_block(p):
    """operation_assignment : ID ADDASSIGN expression ';'
                            | ID SUBASSIGN expression ';'
                            | ID MULASSIGN expression ';'
                            | ID DIVASSIGN expression ';'"""
    p[0] = p[1]

def p_while_instr(p):
    """while_instr : WHILE '(' expression ')' instruction"""
    p[0] = classes.While(p[3], p[5])

def p_instruction_block(p):
    """instruction_block : instruction
                        | '{' instructions '}'"""
    if len(p) > 3:
        p[0] = classes.Instruction(p[1])
    else:
        p[0] = classes.InstructionBlock(p[2])

def p_if_instruction(p):
    """if_instruction : IF '(' expression ')' instruction_block 
                    | IF '(' expression ')' instruction_block ELSE instruction_block"""
    if p[6] == 'else':
        p[0] = classes.IfElse(p[3], p[5], p[7])
    else:
        p[0] = classes.If(p[3], p[5])

def p_for_instruction(p):
    """for_instruction : FOR range instruction_block"""
    p[0] = classes.ForInstruction(p[2], p[3])

def p_range(p):
    """range : ID '=' expression ':' expression"""
    p[0] = classes.Range(p[1], p[3], p[5])


parser = yacc.yacc()