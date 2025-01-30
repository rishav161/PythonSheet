# Given a string s containing just the characters (, ), {, }, [ and ], determine if the input string is valid.

def valid_parentheses(s):
    stack=[]
    mapping={')':'(','}':'{',']':'['}

    for c in s:
        if c in mapping:
            top_ele=stack.pop() if stack else '#'

            if mapping[c]!=top_ele:
                return False
        else:
            stack.append(c)

    return not stack

s = "()[]{}"
print(valid_parentheses(s))