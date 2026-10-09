"""
Introduction
You have already seen that when you change the input value to a function, 
you often get a different output. For instance, consider an add_five() 
function that just adds five to any number and returns the result. 
Then add_five(7) will return an output of 12 (=7+5), and add_five(8) 
will return an output of 13 (=8+5). Note that no matter what the input is, 
the action that the function performs is always the same: it always adds 
five.

But you might instead need a function that performs an action that depends 
on the input. For instance, you might need a function add_three_or_eight() 
that adds three if the input is less than 10, and adds eight if the input 
is 10 or more. Then add_three_or_eight(1) will return 4 (= 1+3), but 
add_three_or_eight(11) will return 19 (=11+8). In this case, the action 
that the function performs varies with the input.

In this lesson, you will learn how to use conditions and conditional 
statements to modify how your functions run.

Conditions
In programming, conditions are statements that are either True or False. 
There are many different ways to write conditions in Python, but some of 
the most common ways of writing conditions just compare two different 
values. For instance, you can check if 2 is greater than 3.

"""

print(2 > 3)
    # Output: False
    
var_one = 1
var_two = 2

print(var_one < 1)
print(var_two >= var_one)

# Output: False
# Output: True

'''
Symbol	Meaning
==	equals
!=	does not equal
<	less than
<=	less than or equal to
>	greater than
>=	greater than or equal to
var_one==1 checks if the value of var_one is 1, but
var_one=1 sets the value of var_one to 1.

'''

def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature."
    # Update value of message only if temperature greater than 38
    if temp > 38:
        message = "Fever!"
    return message

print(evaluate_temp(37))
# Output: Normal temperature.

print(evaluate_temp(39))
# Output: Fever!

'''
The first level of indentation is because we 
always need to indent the code block inside a 
function.
The second level of indentation is because we also 
need to indent the code block belonging to the "if" 
statement. (As you'll see, we'll also need to indent 
the code blocks for "elif" and "else" statements.)
Note that because the return statement is not 
indented under the "if" statement, it is always 
executed, whether temp > 38 is True or False.

'''

def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "Fever!"
    else:
        message = "Normal temperature."
    return message

print(evaluate_temp_with_else(37))
# Output: Normal temperature.

def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Hypothermia!"
    return message

print(evaluate_temp_with_elif(36))
print(evaluate_temp_with_elif(39))
print(evaluate_temp_with_elif(34))


def get_taxes(earnings):
    if earnings < 12000:
        tax_owed = .25 * earnings
    else:
        tax_owed = .30 * earnings
    return tax_owed

ana_taxes = get_taxes(9000)
bob_taxes = get_taxes(15000)

print(ana_taxes) # 2250.0
print(bob_taxes) # 4500.0

"""
In each case, we call the get_taxes() function and use the value that is returned to set
 the value of a variable.

For ana_taxes, we calculate taxes owed by a person who earns 9,000. In this case, 
we call the get_taxes() function with earnings set to 9000. Thus, earnings < 12000 is True,
 and tax_owed is set to .25 * 9000. Then we return the value of tax_owed.
For bob_taxes, we calculate taxes owed by a person who earns 15,000. In this case, 
we call the get_taxes() function with earnings set to 15000. Thus, earnings < 12000 is False, 
and tax_owed is set to .30 * 15000. Then we return the value of tax_owed.
Before we move on to another example - remember the add_three_or_eight() function from the 
introduction? It accepts a number as input and adds three if the input is less than 10, 
and otherwise adds eight. Can you figure out how you would write this function?
 Once you have an answer, click on the "Show hidden code" button below to see the solution.

"""

# Example - Multiple "elif" statements
def get_dose(weight):
    # Dosage is 1.25 ml for anyone under 5.2 kg
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    # Dosage is 10ml for anyone 21.2 kg or more
    else:
        dose = 10
    return dose

"""
The next code cell runs the function. Make sure that the output makes sense to you!

In this case, the "if" statement was False, and all of the "elif" statements evaluate to
 False, until we get to weight < 15.9, which is True, and dose is set to 5.
Once an "elif" statement evaluates to True and the code block is run, the function skips 
over all remaining "elif" and "else" statements. After skipping these, all that is left 
is the return statement, which returns the value of dose.
The order of the elif statements does matter here! Re-ordering the statements will return 
a very different result.

"""
print(get_dose(12))



