# Import Lexer
from tools.lexer import Lexer

# Import Parser
from tools.parser import Parser

# Merge lexer and parser
def runtext(text : str) -> None:
    """Runs the lexer and parser together to run code.

    Args:
        text (str): The code to run
    """
    tokens = Lexer(text)
    Parser(tokens)

# Run if script is ran by console directly
if __name__ == "__main__":
    while True:
        text = str(input("S >>> "))
        runtext(text)