def add(x,y):
  return x+y
def sub(x,y):
   return x-y
def mul(x,y):
   return x*y
def div(x,y):
   return x/y
value1= int(input("enter the value of x"))
value2=int(input("enter the value of y"))
print("select operation")
print("1.add")
print("2.substract")
print("3.multiplication")
print("4.division")
choice=input("enter choice (1/2/3/4)")
if choice =='1':
 print(value1, "+", value2, "=", add(value1, value2))
elif choice=='2':
 print(value1, "-", value2, "=", sub(value1, value2))
elif choice=='3':
 print(value1, "*", value2, "=", mul(value1, value2))
elif choice =='4':
    print(value1, "/", value2, "=", div(value1, value2))
else :
 print("invalid syntax") 