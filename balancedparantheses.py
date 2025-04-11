def is_balanced(expression):
    stack = []
    matching_brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            if stack[-1] == matching_brackets[char]:
                stack.pop()
            else:
                return False
            
    return len(stack)==0



print(is_balanced("(a+b)"))            
print(is_balanced("({[]})"))         
print(is_balanced("{[()]}"))         
print(is_balanced("{[(])}"))         
print(is_balanced("((()))"))        
print(is_balanced("{[(])}"))         
print(is_balanced("(()"))            
print(is_balanced("())"))           
