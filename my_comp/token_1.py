from enum import Enum
from typing import Any

class TokenType(Enum):
    #special Token
    EOF = 'EOF'
    # EOF means End Of File
    ILLEGAL = 'ILLEGAL'
    
    #Data types 
    INT = 'INT'
    FLOAT ='FLOAT'
    
    
    #Arithmetics 
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MULTIPLY = 'MULTIPLY'
    DIVIDE = 'DIVIDE'
    POWER = 'POWER'
    MODULUS = 'MODULUS'
    
    #Symbols
    SEMICOLONS = 'SEMICOLONS'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    
class Token:
    def __init__(self, type:TokenType, literal: Any, line_number: int, position: int  ) -> None:
        self.type = type
        self.literal = literal
        self.line_number = line_number
        self.position = position
    
    def __str__(self) -> str:
        return f"Token[{self.type} : {self.literal} : Line {self.line_number} : Position {self.position}]"
    
    def __represent__(self) -> str:
        return str(self)