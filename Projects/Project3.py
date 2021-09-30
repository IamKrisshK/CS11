from PyInquirer import prompt
import examples
from prompt_toolkit.validation import Validator, ValidationError


class NumberValidator(Validator):

    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(message="Please enter a number: ",
                                  cursor_position=len(document.text))




questions = [
    {
        'type': 'list',
        'name': 'user_option',
        'message': 'Welcome to calculator',
        'choices': ["Addition","Subtraction","Multiplication", "Division", "Square Root", "Cube Root"]
    },

    {
        'type': "input",
        "name": "a",
        "message": "Enter the first number",
        "validate": NumberValidator,
        "filter": lambda val: int(val)
    },

    {
        'type': "input",
        "name": "b",
        "message": "Enter the second number",
        "validate": NumberValidator,
        "filter": lambda val: int(val)
    }


]
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y == 0 :
        print("The value od y can't be 0")

    else:
        return x/y

def sqrt(x,y):
    if x or y < 0:
        return x**(1/2)
        return y**(1/2)

        #for a complex answer

        return (abs(x))**(1/2)
        return (abs(y))**(1/2)
    else:
        return x**(1/2)
        return y**(1/2)

def curt(x,y):
    if x or y < 0:
        return x**(1/3)
        return y**(1/3)

        #for a complex answer:

        return (abs(x)**(1/3))
        return (abs(y)**(1/3))

    else:
        return x**(1/3)
        return y**(1/3)



def main():
    answers = prompt(questions)
    a = answers.get("a")
    b = answers.get("b")
    
    if answers.get("user_option") == 'Addition':
        print(add(a,b))

    elif answers.get("user_option") == 'Subtraction':
        print(sub(a,b))

    elif answers.get("user_option") == 'Multiplication':
        print(mul(a,b))

    elif answers.get("user_option") == 'Division':
        print(div(a,b))

    elif answers.get("user_option") == 'Square Root':
        print(sqrt(a,b))

    elif answers.get("user_option") == 'Cube Root':
        print(curt(a,b))


if __name__ == "__main__":
    main()