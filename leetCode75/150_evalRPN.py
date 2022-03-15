""" Evaluate Reverse Polish Notation Leetcode 150
    Evaluate the value of an arithmetic expression in Reverse Polish Notation

    Valid ops are +,-,/,*
    Division between two integers truncate towards zero
    Its guranteed that the RPN expression is always valid

    ["2","1","+","3","*"] gives us 9
    2+1 3
        3 * 3
            9
"""


def evalRPN(tokens):
    stack=[]
    for c in tokens:
        if c=="+":
            a,b=stack.pop(),stack.pop()
            stack.append(a+b)
        elif c=="*":     
            a,b=stack.pop(),stack.pop()
            stack.append(a*b)
        elif c=="-":          
            a,b=stack.pop(),stack.pop()
            stack.append(b-a)
        elif c=="/": 
            a,b=stack.pop(),stack.pop()
            stack.append(int(b/a))  # this ensures that we actually truncate stuff
        else:
            stack.append(int(c))
    return stack[0]

print(evalRPN(["2","1","+","3","*"]))