'''
FreeCodeCamp's Scientific Computing with Python - Arithmetic Formatter

Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. 

The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

Author: RaShunda Williams
Completed: 06-17-23
'''

def arithmetic_arranger(problems, show_answers=False):
    # initializes variables
    arranged_problems = ""
    first_line = ""
    second_line = ""
    dash_line = ""
    result_line = ""

    # iterates through the problems list
    for problem in problems:
        operand1, operator, operand2 = problem.split() # splits each problem into seperate components
    
        # too many problems
        if len(problems) > 5:
            return "Error: Too many problems."

        # checks to see if both operands contain only digits.
        if not operand1.isnumeric() or not operand2.isnumeric():
            return "Error: Numbers must only contain digits."

        #  max of four digits
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Operator check
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # determines the max length between operand1 and operand2 to align the digits properly
        max_length = max(len(operand1), len(operand2))
        result = str(eval(problem))
        
        # operand1 with the maximum length plus 2space
        first_line += operand1.rjust(max_length + 2)
        
        # concat the operator, a space, and right-justifying operand2 with the maximum length
        second_line += operator + " " + operand2.rjust(max_length)

        # dash line by adding "-" equal to the length of the max operand plus 2space
        dash_line += "-" * (max_length + 2)

        #result with the maximum length plus 2space 
        result_line += result.rjust(max_length + 2)

        #  four spaces are added to separate the lines
        if problem != problems[-1]:
            # Define the number of spaces for separation
            separation_spaces = " " * 4

            # Create a list of lines to update
            lines = [first_line, second_line, dash_line, result_line]

            # Add separation spaces to each line
            for i in range(len(lines)):
                lines[i] += separation_spaces

            # Assign the updated lines back to their respective variables
            first_line, second_line, dash_line, result_line = lines

    arranged_problems = first_line + "\n" + second_line + "\n" + dash_line

    # show answers if true
    if show_answers:
        arranged_problems += "\n" + result_line

    return arranged_problems