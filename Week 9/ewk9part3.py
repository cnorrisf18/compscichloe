
# 3 6 +
stack=[]
stack.append(3)
stack.append(6)
x=stack.pop()
y=stack.pop()
stack.append(y+x)
print(stack)

#3 1 + 2 -

newstack=[]
newstack.append(3)
newstack.append(1)
x=newstack.pop()
y=newstack.pop()
newstack.append(y+x)
newstack.append(2)
z=newstack.pop()
w=newstack.pop()
newstack.append(w-z)
print(newstack)





def postFix(str):

    listofcommands=str.split(" ")
    stacktosolve=[]
    for char in listofcommands:
        if ord(char) > 47 and ord(char) < 58:
            stacktosolve.append(int(char))
        elif char == '+':
            x=stacktosolve.pop()
            y=stacktosolve.pop()
            stacktosolve.append(y+x)
        elif char == '-':
            x=stacktosolve.pop()
            y=stacktosolve.pop()
            stacktosolve.append(y-x)
        elif char == '*':
            x=stacktosolve.pop()
            y=stacktosolve.pop()
            stacktosolve.append(y*x)
        elif char == '/':
            x=stacktosolve.pop()
            y=stacktosolve.pop()
            stacktosolve.append(y/x)
    return stacktosolve


to_solve=open(r'C:\Users\chloe\PycharmProjects\CompSci\Week 9\expressions.txt', 'r')
solved=open(r'C:\Users\chloe\PycharmProjects\CompSci\Week 9\expressionssolved.txt', 'w')


to_solve_read=to_solve.read()
to_solve_list=to_solve_read.split("\n")
for line in to_solve_list:
    solution=str(postFix(line))
    solved.write(solution)
    solved.write('\n')

to_solve.close()
solved.close()
