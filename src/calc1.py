'''
Token Types

EOF(End-of-file)

Inspired from : https://ruslanspivak.com/lsbasi-part1/

'''

INTEGER, PLUS, EOF = 'INTEGER','PLUS','EOF'

class Token(object):
    def __init__(self, type, value):
        #Token type: INTEGER, PLUS or EOF
        self.type = type
        #token value : 0,1,2,3...9, '+', or None
        self.value = value

    def __str__(self):
        '''String representation of the class instance
        
        Examples:
        Token(INTEGER, 3)
        Token(Plus '+')
        '''

        return 'Token({type},{value})'.format(
                type = self.type,
                value = repr(self.value)
                )
    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        # client string input eg. "3+5"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        '''This is a lexical analyzer or tokenizer.
        This method is responsible for breaking a sentence 
        apart into tokens. One token at a time.
        '''
        text = self.text

        '''Is self.pos index past the end of the self.text ?
        If so, then return EOF token because there is no more
        input left to convert into tokens.'''

        if self.pos > len(text) -1:
            return Token(EOF, None)

        '''Get a character at the position self.pos and decide what token to create based on the single character'''
        current_char = text[self.pos]

        '''
        If the character is a digit then convert it to integer, create an INTEGER token, increment self.pos, index to point to the next character after the digit, and return the integer token'''

        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        '''Compare the current token type with the passed token
        type and if they match then "eat" the current token
        and assign the next token to the self.current_token, 
        otherwise raise an exception.'''

        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        '''expr -> INTEGER PLUS INTEGER
        # set current token to the first token taken from the input

        '''
        self.current_token = self.get_next_token()

        # We expect the current token to be a single-digit integer
        left = self.current_token
        self.eat(INTEGER)

        # We expect the current token to be a '+' token 
        op = self.current_token
        self.eat(INTEGER)

        result = left.value + right.value
        return result

def main():
    while True:
        try:
            text = raw_input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()
