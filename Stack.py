stack=[]
def push():
    element=input("enter the number")
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print("the list is empty")
    else:
        e=stack.pop()
        print("the element poped out of the list is ",e)
        print(stack)

while True:
    print("choose 1 to push , 2 to pop and 3 to quit")
    choose = int(input())
    if choose==1:

        push()
    elif choose ==2:
        pop()
    elif choose==3:
        quit()
    else:
        print("choose the correct number")