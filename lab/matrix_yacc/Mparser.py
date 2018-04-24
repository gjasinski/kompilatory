#!/usr/bin/python

from matrix_lex import scanner
import ply.yacc as yacc

from matrix_yacc.AST.types import ast_node_types as types
from matrix_yacc.AST.AstNode import *

tokens = scanner.tokens

precedence = (
    # to fill ...
    # ("left", '+', '-'),
    # to fill ...
    # Przypisania
    ("right", '=', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
    ("nonassoc", "IFX"),
    ("nonassoc", "ELSE"),
    ("nonassoc", "NE", "EQ"),
    ("nonassoc", 'LT', 'GT', 'LE', 'GE'),
    ("nonassoc", ':'),
    ("left", '+', '-', 'DOTADD', 'DOTSUB'),
    ("left", '*', '/', 'DOTMUL', 'DOTDIV'),
    ("right", 'UMINUS'),
    ("right", 'SINGLE_QUOTE'),
)


def p_error(p):
    print(p)
    if p:
        print("Syntax error at line {0}, LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instructions_opt"""
    p[0] = Program(p[1])


def p_instructions_opt_1(p):
    """instructions_opt : instructions """
    p[0] = InstructionsOpt1(p[1])


def p_instructions_opt_2(p):
    """instructions_opt : """
    p[0] = InstructionsOpt2()


def p_instructions_1(p):
    """instructions : instructions instruction """
    p[0] = Instructions(p[1], p[2])


def p_instructions_2(p):
    """instructions : instruction """
    p[0] = Instruction(p[1])


def p_instr_assignment_instruction(p):
    """instruction : assignment_instruction"""
    p[0] = AssigmentInstruction(p[1])


def p_instr_conditional_instruction(p):
    """instruction : conditional_instruction"""
    p[0] = Conditional(p[1])


def p_instr_compound_instruction(p):
    """instruction : compound_instruction"""
    p[0] = Compound(p[1])


def p_instr_print_instruction(p):
    """instruction : print_instruction"""
    p[0] = PrintInstr(p[1])


def p_instr_iteration_instruction(p):
    """instruction : iteration_instruction"""
    p[0] = Iteration(p[1])


def p_instr_jump_instruction(p):
    """instruction : jump_instruction"""
    p[0] = Jump(p[1])


def p_assignment_instruction(p):
    """assignment_instruction : unary_expr '=' expr ';'
                              | unary_expr ADDASSIGN expr ';'
                              | unary_expr SUBASSIGN expr ';'
                              | unary_expr MULASSIGN expr ';'
                              | unary_expr DIVASSIGN expr ';'
    """
    p[0] = Assigment(p[1], p[2], p[3])


def p_condition_instruction_1(p):
    """conditional_instruction : IF '(' expr ')' instruction %prec IFX"""
    p[0] = If(p[3], p[5])


def p_condition_instruction_2(p):
    """conditional_instruction : IF '(' expr ')' instruction ELSE instruction"""
    p[0] = IfElse(p[3], p[5], p[7])


def p_compound_instruction_1(p):
    """compound_instruction : '{' '}'
    """
    p[0] = CompoundInstr([], p[1])


def p_compound_instruction_2(p):
    """compound_instruction : '{' instructions '}'
    """
    p[0] = CompoundInstr(p[1], p[2])


def p_print_instruction(p):
    """print_instruction : PRINT expr ';'"""
    p[0] = PrintExpressions(p[2], p[1])


def p_iteration_instruction_1(p):
    """iteration_instruction : WHILE '(' expr ')' instruction
                             | WHILE '(' expr ')' '{' instruction"""
    p[0] = While(p[3], p[5])


# def p_iteration_instruction_2(p):
#     """iteration_instruction :   FOR iterator_assignment '{' instruction"""
#     p[0] = ForInstruction(p[2], p[4])


def p_iteration_instruction_3(p):
    """iteration_instruction : FOR iterator_assignment instruction"""
    p[0] = ForInstruction(p[2], p[3])


def p_jump_instruction(p):
    """jump_instruction : BREAK ';'
                        | CONTINUE ';'
    """
    p[0] = ContinueBreak()


def p_jump_instruction_2(p):
    """jump_instruction : RETURN ';'
    """
    p[0] = ReturnInstr(p[1])

def p_primary_expr(p):
    """primary_expr : ID
                    | INTNUM
                    | FLOATNUM
                    | STRING
                    | matrix
                    | '(' expr ')'
    """
    p[0] = PrimaryExpr(p[1])


def p_postfix_expr_1(p):
    """postfix_expr : primary_expr"""
    p[0] = Postfix_expr_1(p[1])


def p_postfix_expr_2(p):
    """postfix_expr : postfix_expr '[' expr ']'
                    | postfix_expr SINGLE_QUOTE
    """
    p[0] = Postfix_expr_2(p[1], p[2])


def p_unary_expr_1(p):
    """unary_expr : postfix_expr"""
    p[0] = Unary_expr_1(p[1])


def p_unary_expr_2(p):
    """unary_expr : '-' multiplicative_expr %prec UMINUS"""
    p[0] = Unary_expr_2(p[1], p[2])


def p_mutiplicative_expr_1(p):
    """multiplicative_expr : unary_expr"""
    p[0] = Generic_expr_1(p[1])


def p_mutiplicative_expr_2(p):
    """multiplicative_expr : multiplicative_expr '*' unary_expr
                           | multiplicative_expr '/' unary_expr
                           | multiplicative_expr DOTMUL unary_expr
                           | multiplicative_expr DOTDIV unary_expr
    """
    p[0] = Generic_expr_2(p[1], p[2], p[3])


def p_additive_expr_1(p):
    """additive_expr : multiplicative_expr"""
    p[0] = Generic_expr_1(p[1])


def p_additive_expr_2(p):
    """additive_expr : additive_expr '+' multiplicative_expr
                     | additive_expr '-' multiplicative_expr
                     | additive_expr DOTADD multiplicative_expr
                     | additive_expr DOTSUB multiplicative_expr
    """
    p[0] = Generic_expr_2(p[1], p[2], p[3])


def p_relational_expr_1(p):
    """relational_expr : additive_expr"""
    p[0] = Generic_expr_1(p[1])


def p_relational_expr_2(p):
    """relational_expr : relational_expr rel_op additive_expr"""
    p[0] = Generic_expr_2(p[1], p[2], p[3])


def p_equality_expr_1(p):
    """equality_expr : relational_expr"""
    p[0] = Generic_expr_1(p[1])


def p_equality_expr_2(p):
    """equality_expr : equality_expr eq_op relational_expr"""
    p[0] = Generic_expr_2(p[1], p[2], p[3])


def p_assignment_expr_1(p):
    """assignment_expr : equality_expr"""
    p[0] = Generic_expr_1(p[1])


def p_assignment_expr_2(p):
    """assignment_expr : unary_expr assignment_op assignment_expr"""
    p[0] = Generic_expr_2(p[1], p[2], p[3])


def p_expr_1(p):
    """expr : assignment_expr"""
    p[0] = Expr_1(p[1])


def p_expr_2(p):
    """expr : expr ',' assignment_expr"""
    p[0] = Expr_2(p[1], p[3])


def p_expr_3(p):
    """expr : ZEROS '(' expr ')'
            | ONES '(' expr ')'
            | EYE '(' expr ')'
    """
    p[0] = Expr_3(p[1], p[3])


def p_matrix(p):
    """matrix : '[' outer ']'"""
    p[0] = Matrix(p[2])


def p_matrix_outer_1(p):
    """outer : outer ';' inner"""
    p[0] = MatrixOuter1(p[1], p[3], p[2])


def p_matrix_outer_2(p):
    """outer : inner"""
    p[0] = MatrixOuter2(p[1])


def p_matrix_inner_1(p):
    """inner : inner ',' elem"""
    p[0] = MatrixInner_1(p[1], p[3], p[2])


def p_matrix_inner_2(p):
    """inner : elem"""
    p[0] = MatrixInner_2(p[1])


def p_matrix_elem(p):
    """elem : expr"""
    p[0] = MatrixElem(p[0])


def p_iterator_assignment(p):
    """iterator_assignment : ID '=' expr ':' expr"""
    p[0] = IteratorAssignment(p[1], p[3], p[5], p[4])


def p_assignment_operator(p):
    """assignment_op : '='
                     | ADDASSIGN
                     | SUBASSIGN
                     | MULASSIGN
                     | DIVASSIGN
    """
    p[0] = p[1]


def p_relational_operator(p):
    """rel_op : LT
              | LE
              | GT
              | GE
    """
    p[0] = p[1]


def p_equality_operator(p):
    """eq_op : EQ
             | NE
    """
    p[0] = p[1]


parser = yacc.yacc()
