#sr6bf Sarah Raza

Value = 0 #current value stored
recent_op = "" #str of most recent operation
recent_arg = 0 #most recent argument used with last operation
last_calc = "0" #series of operations performed in current calculation

def get_value():
    '''
    :return: This function returns the int representing the current value stored in the calculator.
    '''

    return Value

def clear(x = 0):
    '''
    :param x: This function takes in an optional int argument that defaults to 0
    :return: Sets the second and third global variables to their initial values and sets the
    first and fourth global variables to the argument's int value str representation. At
    the end, it returns the current int value.
    '''

    global Value
    Value = x
    global recent_op
    recent_op = ""
    global recent_arg
    recent_arg= 0
    global last_calc
    last_calc = str(x)
    return Value

def step(operator, argument):
    '''
    :param operator: Takes in an arithmetic operator
    :param argument  A single calculation is enacted by updating the calculator's global variables to
    reflect the operation involved, and then returns the calculator's current int value.
    '''

    global recent_op
    recent_op = operator
    global recent_arg
    recent_arg = argument
    global last_calc
    global Value
    if operator == '+':
        last_calc = "(" + last_calc + ")" + "+" + str(argument)
        Value += argument
    if operator == '-':
        last_calc = "(" + last_calc + ")" + "-" + str(argument)
        Value -= argument
    if operator == '*':
        last_calc = "(" + last_calc + ")" + "*" + str(argument)
        Value *= argument
    if operator == '//':
        last_calc = "(" + last_calc+ ")" + "//" + str(argument)
        Value //= argument
    return Value

def repeat():
    '''
    :return: This function repeats the last calculation step and returns the calculator's current int value.
    If no previous operation has been recorded, the function just returns the current int value.
    '''

    global last_calc
    global recent_op
    global Value
    return step(recent_op, recent_arg)

def get_expr():
    '''
    :return: Returns a str representing the current expression
    '''
    return last_calc
