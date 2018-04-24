from __future__ import print_function
import AstNode

indent_char = '|   '

def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

class TreePrinter:

    @addToClass(AstNode.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)


    @addToClass(AstNode.Program)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.instructions.printTree(indent)
        return res

    @addToClass(AstNode.InstructionsOpt1)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.instructions.printTree(indent)
        return res

    @addToClass(AstNode.InstructionsOpt2)
    def printTree(self, indent=0):
        res = indent_char * indent
        return res

    @addToClass(AstNode.Instructions)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.instructions.printTree(indent + 0)
        res += self.instruction.printTree(indent + 0)
        return res

    @addToClass(AstNode.Instruction)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.instruction.printTree(indent + 0)
        return res

    @addToClass(AstNode.AssigmentInstruction)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.assigment.printTree(indent + 0)
        return res

    @addToClass(AstNode.Conditional)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.conditional.printTree(indent + 0)
        return res

    @addToClass(AstNode.Compound)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.compound.printTree(indent + 0)
        return res

    @addToClass(AstNode.PrintInstr)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.printInstr.printTree(indent + 0)
        return res

    @addToClass(AstNode.Iteration)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.iteration.printTree(indent + 0)
        return res

    @addToClass(AstNode.Jump)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.jump.printTree(indent + 0)
        return res

    @addToClass(AstNode.Assigment)
    def printTree(self, indent=0):
        res = indent_char * indent + self.assignType + '\n'
        res += self.variable.printTree(indent + 1)
        res += self.expression.printTree(indent + 1)
        return res

    @addToClass(AstNode.If)
    def printTree(self, indent=0):
        res = indent_char * indent + 'IF' + '\n'
        res += self.condition.printTree(indent + 1)
        res += self.instructions.printTree(indent + 1)
        return res

    @addToClass(AstNode.IfElse)
    def printTree(self, indent=0):
        res = indent_char * indent + 'IF' + '\n'
        res += self.condition.printTree(indent + 1)
        res += self.instructions.printTree(indent + 1)
        res += indent_char * indent + 'ELSE' + '\n'
        res += self.else_instructions.printTree(indent + 1)
        return res

    @addToClass(AstNode.CompoundInstr)
    def printTree(self, indent=0):
        #todo tutaj moze???????
        # res = indent_char * indent + 'a' +self.instr1 + '\n'
        res = self.instr2.printTree(indent + 0)
        return res

    @addToClass(AstNode.PrintExpression)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.to_print.printTree(indent + 0)
        return res


    @addToClass(AstNode.PrintExpressions)
    def printTree(self, indent=0):
        print(self.print_expressions)
        print(self.print_expressions.printTree())
        res = indent_char * indent + self.print_expression + '\n'
        res += self.print_expressions.printTree(indent + 1)
        return res

    @addToClass(AstNode.While)
    def printTree(self, indent=0):
        res = indent_char * indent + 'WHILE' + '\n'
        res += self.condition.printTree(indent + 1)
        res += self.instructions.printTree(indent + 1)
        return res

    @addToClass(AstNode.ForInstruction)
    def printTree(self, indent=0):
        res = indent_char * indent + 'FOR' + '\n'
        res += self.iterator_assignment.printTree(indent + 1)
        res += self.instruction.printTree(indent + 1)
        return res

    @addToClass(AstNode.ReturnInstr)
    def printTree(self, indent=0):
        res = indent_char * indent
        res += self.expression.printTree(indent + 0)
        return res

    @addToClass(AstNode.ContinueBreak)
    def printTree(self, indent=0):
        res = indent_char * indent
        return res

    @addToClass(AstNode.PrimaryExpr)
    def printTree(self, indent=0):
        # print(str(self.expr))
        if type(self.expr) is AstNode.Matrix:
            res = self.expr.printTree(indent)
        else:
            res = indent_char * indent + str(self.expr) + '\n'
        return res

    @addToClass(AstNode.Postfix_expr_1)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.expr1.printTree(indent + 0)
        return res

    @addToClass(AstNode.Postfix_expr_2)
    def printTree(self, indent=0):
        res = indent_char * indent + self.expr2 + '\n'
        res += self.expr1.printTree(indent + 1)
        # res += self.expr2
        return res

    @addToClass(AstNode.Unary_expr_1)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.expr1.printTree(indent + 0)
        return res

    @addToClass(AstNode.Unary_expr_2)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.expr1.printTree(indent + 0)
        res += self.expr2.printTree(indent + 0)
        return res

    @addToClass(AstNode.Generic_expr_1)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.expr.printTree(indent + 0)
        return res

    @addToClass(AstNode.Generic_expr_2)
    def printTree(self, indent=0):
        res = indent_char * indent + self.op + '\n'
        res += self.expr1.printTree(indent + 1)
        res += self.expr2.printTree(indent + 1)
        return res

    @addToClass(AstNode.Generic_expr_3)
    def printTree(self, indent=0):
        res = indent_char * indent + self.expr1 + '\n'
        res += self.expr2.printTree(indent + 1)
        return res

    @addToClass(AstNode.Matrix)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.matrix.printTree(indent + 0)
        return res

    @addToClass(AstNode.MatrixOuter1)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.expr1.printTree(indent + 0)
        res += self.expr2.printTree(indent + 0)
        res += self.expr3
        #.printTree(indent + 0)
        return res

    @addToClass(AstNode.MatrixOuter2)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.expr1.printTree(indent + 0)
        return res

    @addToClass(AstNode.MatrixInner_1)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.expr1.printTree(indent + 0)
        res += self.expr2.printTree(indent + 0)
        res += self.expr3.printTree(indent + 0)
        return res

    @addToClass(AstNode.MatrixInner_2)
    def printTree(self, indent=0):
        # res = indent_char * indent
        res = self.expr1.printTree(indent + 0)
        return res

    @addToClass(AstNode.MatrixElem)
    def printTree(self, indent=0):
        res = indent_char * indent + str(self.elem) + '\n'
        # res = self.elem.printTree(indent + 0)
        return res

    @addToClass(AstNode.IteratorAssignment)
    def printTree(self, indent=0):
        res = indent_char * indent + self.expr1 + '\n'
        res += indent_char * indent + 'RANGE\n'
        res += self.expr2.printTree(indent + 1)
        res += self.expr3.printTree(indent + 1)
        # res += + self.expr4
        return res

    @addToClass(AstNode.Expr_1)
    def printTree(self, indent=0):
        res = self.expr1.printTree(indent + 0)
        return res

    @addToClass(AstNode.Expr_2)
    def printTree(self, indent=0):
        # res = indent_char * indent + self.expr1 + '\n'

        res = self.expr1.printTree(indent + 0)
        res += self.expr2.printTree(indent + 0)
        return res

    @addToClass(AstNode.Expr_3)
    def printTree(self, indent=0):
        res = indent_char * indent + self.expr1 + '\n'
        # res = self.expr1.printTree(indent + 0)
        res += self.expr2.printTree(indent + 1)
        return res
