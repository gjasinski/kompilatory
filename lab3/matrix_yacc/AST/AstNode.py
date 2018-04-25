class AstNode:
    def __init__(self, node_type, children=None, leaf=""):
        self.type = node_type
        if children:
            self.children = children
        else:
            self.children = []
        self.leaf = leaf

    def __str__(self):
        s = self.type + '('
        for child in self.children:
            s += str(child) + ', '
        s += ') ' + str(self.leaf)
        # return self.type + str(self.children) + ', ' + str(self.leaf) + ')'
        # return str(self.to_array())
        return s

    def to_array(self):
        # a = [self.type, self.leaf, list(map(lambda c: c, self.children))]
        a = [self.type, self.leaf, self.children]
        return a



class Node(object):
    pass


class Program(Node):
    def __init__(self, instructions):
        self.instructions = instructions
    #
    # def __str__(self):
    #     return "[" + self.__class__.__name__ + "]{(program: [" + str(self.program) + "])}"
    #


class InstructionsOpt1(Node):
    def __init__(self, instructions):
        self.instructions = instructions
    #
    # def __str__(self):
    #     return "[" + self.__class__.__name__ + "]{(instructions: [" + str(self.instructions) + "])}"
    #

class InstructionsOpt2(Node):
    pass
    

class Instructions(Node):
    def __init__(self, instructions, instruction):
        self.instructions = instructions
        self.instruction = instruction
    #
    # def __str__(self):
    #     return "[" + self.__class__.__name__ + "]{(instructions: [" + str(
    #         self.instructions) + "]), (instruction: [" + str(
    #         self.instruction) + "])}"
    #

class Instruction(Node):
    def __init__(self, instruction):
        self.instruction = instruction
    #
    # def __str__(self):
    #     return "[" + self.__class__.__name__ + "]{(instructions: [" + str(self.instruction) + "])}"


class AssigmentInstruction(Node):
    def __init__(self, assigment):
        self.assigment = assigment
    #
    # def __str__(self):
    #     return "[" + self.__class__.__name__ + "]{(AssigmentInstruction: [" + str(self.assigment) + "])}"


class Conditional(Node):
    def __init__(self, conditional):
        self.conditional = conditional
    #
    # def __str__(self):
    #     return "[" + self.__class__.__name__ + "]{(conditional: [" + str(self.conditional) + "])}"
    #

class Compound(Node):
    def __init__(self, compound):
        self.compound = compound
    #
    # def __str__(self):
    #     return "[" + self.__class__.__name__ + "]{(compound: [" + str(self.compound) + "])}"
    #

class PrintInstr(Node):
    def __init__(self, printInstr):
        self.printInstr = printInstr
    #
    # def __str__(self):
    #     return "[" + self.__class__.__name__ + "]{(printInstr: [" + str(self.printInstr) + "])}"
    #

class Iteration(Node):
    def __init__(self, iteration):
        self.iteration = iteration
    #
    # def __str__(self):
    #     return "[" + self.__class__.__name__ + "]{(Iteration: [" + str(self.iteration) + "])}"
    #

class Jump(Node):
    def __init__(self, jump):
        self.jump = jump
    #
    # def __str__(self):
    #     return "[" + self.__class__.__name__ + "]{(printInstr: [" + str(self.jump) + "])}"


class Assigment(Node):
    def __init__(self, variable, assignType, expression):
        self.variable = variable
        self.assignType = assignType
        self.expression = expression


class If(Node):
    def __init__(self, condition, instructions):
        self.condition = condition
        self.instructions = instructions


class IfElse(Node):
    def __init__(self, condition, instructions, else_instructions):
        self.condition = condition
        self.instructions = instructions
        self.else_instructions = else_instructions


class CompoundInstr(Node):
    def __init__(self, instr1, instr2):
        self.instr1 = instr1
        self.instr2 = instr2


class PrintExpression(Node):
    def __init__(self, to_print):
        self.to_print = to_print


class PrintExpressions(Node):
    def __init__(self, print_expressions, print_expression):
        self.print_expression = print_expression
        self.print_expressions = print_expressions


class While(Node):
    def __init__(self, condition, instructions):
        self.condition = condition
        self.instructions = instructions


class ForInstruction(Node):
    def __init__(self, iterator_assignment, instruction):
        self.iterator_assignment = iterator_assignment
        self.instruction = instruction


class ReturnInstr(Node):
    def __init__(self, expression):
        self.expression = expression


class ContinueBreak(Node):
    def __init__(self):
        pass


class PrimaryExpr(Node):
    def __init__(self, expr):
        self.expr = expr


class Postfix_expr_1(Node):
    def __init__(self, expr1):
        self.expr1 = expr1


class Postfix_expr_2(Node):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

class Postfix_expr_3(Node):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2


class Unary_expr_1(Node):
    def __init__(self, expr1):
        self.expr1 = expr1


class Unary_expr_2(Node):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2


class Generic_expr_1(Node):
    def __init__(self, expr):
        self.expr = expr


class Generic_expr_2(Node):
    def __init__(self, expr1, op, expr2):
        self.expr1 = expr1
        self.expr2 = expr2
        self.op = op

class Generic_expr_3(Node):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2


class Matrix(Node):
    def __init__(self, matrix):
        self.matrix = matrix


class MatrixOuter1(Node):
    def __init__(self, expr1, expr2, expr3):
        self.expr1 = expr1
        self.expr2 = expr2
        self.expr3 = expr3


class MatrixOuter2(Node):
    def __init__(self, expr1):
        self.expr1 = expr1


class MatrixInner_1(Node):
    def __init__(self, expr1, expr2, expr3):
        self.expr1 = expr1
        self.expr2 = expr2
        self.expr3 = expr3


class MatrixInner_2(Node):
    def __init__(self, expr1):
        self.expr1 = expr1


class MatrixElem(Node):
    def __init__(self, elem):
        self.elem = elem


class IteratorAssignment(Node):
    def __init__(self, expr1, expr2, expr3, expr4):
        self.expr1 = expr1
        self.expr2 = expr2
        self.expr3 = expr3
        self.expr4 = expr4

class Expr_1(Node):
    def __init__(self, expr1):
        self.expr1 = expr1


class Expr_2(Node):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2


class Expr_3(Node):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2