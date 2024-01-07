#quiz game
print("let's play quiz")
for i in range(10):
    print("\n")
ans=input().lower()
if ans=='yes':
    print("let's start")
else:
    quit()
name=input("enter name")
print("hello"+" "+name+" "+"let's play")
q=['cpu','pc','sbi']
a1=["central processing unit","police constable",'state bank of india']
c=0
for i in range(3):
    print("what is"+" "+q[i]+" "+"stands for?")
    a=input().lower()
    if a==a1[i]:
        c+=1
    else:
        print("OOPS wrong")
    if c==3:
        print("you have completed the quiz")
print("your score is",c)
