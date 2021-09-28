# -*- coding: utf-8 -*-
"""7-Sricharan-Yedu-Thirnathi.ipynb
"""

def integrity_of_parenthesis(string):
    opening_brackets = ['(','{','[']
    closing_brackets = [')','}',']']
    stack = []
 
    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return "Not OK"
            top_element = stack.pop()
            if not integrity(top_element, char):
                return "Not OK"  
    if len(stack) != 0:
        return "Not OK"
    else:
      return "Ok"

def integrity(opening, closing):
    if opening == '(' and closing == ')':
        return "Ok"
    if opening == '[' and closing == ']':
        return "Ok"
    if opening == '{' and closing == '}':
        return "Ok"
    else:
      return "Not Ok"
 
print(integrity_of_parenthesis("[])}"))
print(integrity_of_parenthesis("{[()]}"))
print(integrity_of_parenthesis("{[[]]{()}}"))
print(integrity_of_parenthesis("[{}"))
print(integrity_of_parenthesis(""))
