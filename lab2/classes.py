class Node(object):
    def __init__(self, declarations, fundefs, instructions):
        self.declarations = declarations
        self.fundefs = fundefs
        self.instructions = instructions
        self.i = 0

    def __str__(self):
        return self.printTree()

class Variable(Node):
    def __init__(self, value):
        self.value = value
        self.type = type(value)

    def __str__(self):
        return self.printTree()

class BinaryExpression(Node):
    def __init__(self, operator, left, right):
        self.op = operator
        self.left = left
        self.right = right

    def __str__(self):
        return self.printTree()


class Instruction(Node):
    def __init__(self, instruction):
        self.instruction = instruction

    def __str__(self):
        return self.printTree()

class Instructions(Node):
    def __init__(self, instructions, instruction):
        self.instructions = instructions
        self.instruction = instruction

    def __str__(self):
        return self.printTree()

class PrintInstruction(Node):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.printTree()
        
class Assignment(Node):
    def __init__(self, id, assignType):
        self.assignType = assignType
        self.id = id

class BeginAssignment(Node):
    def __init__(self, id, type):
        self.id = id
        self.type = type

class MiddleAssignment(Assignment):
    def __init__(self, id, type, assignment):
        super(MiddleAssignment, self).__init__(id, type)
        self.expression = assignment

    def __str__(self):
        return self.printTree()

class EndAssignment(Assignment):
    def __init__(self, id, type, expression):
        super(EndAssignment, self).__init__(id, type)
        self.expression = expression

    def __str__(self):
        return self.printTree()

class If(Node):
    def __init__(self, condition, instructions):
        self.condition = condition
        self.instructions = instructions

    def __str__(self):
        return self.printTree()


class IfElse(Node):
    def __init__(self, condition, instructions, else_instructions):
        self.condition = condition
        self.instructions = instructions
        self.else_instructions = else_instructions

    def __str__(self):
        return self.printTree()


class While(Node):
    def __init__(self, condition, instructions):
        self.condition = condition
        self.instructions = instructions

    def __str__(self):
        return self.printTree()

class ReturnInstruction(Node):
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return self.printTree()


class Break(Node):
    def __str__(self):
        return self.printTree()


class Continue(Node):
    def __str__(self):
        return self.printTree()

class PrintExpression(Node):
    def __init__(self, to_print):
        self.to_print = to_print

    def __str__(self):
        return self.printTree()

class PrintExpressions(Node):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

    def __str__(self):
        return self.printTree()


class UnaryExprssion(Node):
    def __init__(self, expression, operator):
        self.expression = expression
        self.operator = operator

    def __str__(self):
        return self.printTree()


class InstructionBlock(Node):
    def __init__(self, instructions):
        self.instructions = instructions

    def __str__(self):
        return self.printTree()

class Range(Node):
    def __init__(self, variable, from_variable, to_variable):
        self.variable = variable
        self.from_variable = from_variable
        self.to_variable = to_variable

    def __str__(self):
        return self.printTree()

class ForInstruction(Node):
    def __init__(self, range, instruction_block):
        self.range = range
        self.instruction_block = instruction_block

    def __str__(self):
        return self.printTree()

class MatrixInitializer(Node):
    def __init__(self, rows, row):
        self.rows = rows
        self.row = row

    def __str__(self):
        return self.printTree()


class MatrixReference(Node):
    def __init__(self, matrix_id, location):
        self.matrix_id = matrix_id
        self.location = location

    def __str__(self):
        return self.printTree()


class MatrixLocations(Node):
    def __init__(self, dim_locations, location):
        self.dim_locations = dim_locations
        self.location = location

    def __str__(self):
        return self.printTree()


class ZerosInitMatrix(Node):
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return self.printTree()


class OneswsInitMatrix(Node):
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return self.printTree()


class EyeInitMatrix(Node):
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return self.printTree()
