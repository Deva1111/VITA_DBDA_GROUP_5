
num= 10
if(num>12):
    print("num is greater than 12.")

elif(num<10):

    print("10 se greater")    

else:
    print("rahudet tu")    


a = None
type(a)    


a=100
print(a)
print("The number is",a)
print("The datatype of a is",type(a))
a= 4.5
type(a)
print(a)


c = "hello"
type(c)

d = True
type(d)




num1=5.6
print(num1)
print(type(num1))
print(int(5.6))
print(num1)

num2='123'
print(num2)
print(type(num2))

num3=int(num2)
print(num3)
print(type(num3))

num4=25
print(num4)
print(type(num4))
num5=float(num4)
print(num5)
print(type(num5))


aa= 'a'
type(aa)
#  num6="123"+10        #   TypeError: can only concatenate str (not "int") to str
num6=int("123")+10
print(num6)
print(type(num6))

num7="123"+str(10)
print(num7)
print(type(num7))

num8=True
print(num8)
print(type(num8))

num9=int(num8)
print(num9)
print(type(num9))

num10=False
print(num10)
print(type(num10))

num11=float(num10)
print(num11)
print(type(num11))


num12=3.4
num13=complex(num12)
print(num13)
print(type(num13))

num14=5+4j
# num15=int(num14)      #  TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
num15=str(num14)
print(num15)
print(type(num15))

#  num16="458m"         # ValueError: complex() arg is a malformed string
# num16="j349"          # ValueError: complex() arg is a malformed string
num16="349j"            # not a problem
#num16="458"             # not a problem
num17=complex(num16)      
print(num17)
print(type(num17))

num18=True
num19=complex(num18)
print(num19)
print(type(num19))

num20=6+3.4j
num21=bool(num20)
print(num21)
print(type(num21))

num22=0+8j
num23=bool(num22)
print(num23)
print(type(num23))

# num24=4+0j    # True
num24=0+0j
num25=bool(num24)
print(num25)
print(type(num25))




num1= 5+3j
print(num1)
print(type(num1))

num2= 3.4 -5.6j
print(num2)
print(type(num2))

num3 = 5+7.8j
print(num3)
print(type(num3))


num4= "hello"+4j
print(num4)
print(type(num4)) 

#  How to access "real" and "imaginary" part of the object

print(num3)             # Complex number
print(num3.real)        # real part of the complex number are properties of that object
print(num3.imag)        # imaginary part of the complex number

# How to generate complex number using "complex()" function

num5 = complex(4,5.6)
print(num5)
print(type(num5))  


num6=complex()     # What if we don't pass any number?
print(num6)
print(type(num6))

num7=complex(5.6)  # what if we pass only one argument?
print(num7)
print(type(num7))

num8=complex(0,5.6)  # what if we pass first argument as 0 ?
print(num8)
print(type(num8))

num9=complex("123")
print(num9)
print(type(num9))

num10=complex("A123")    ValueError: complex() arg is a malformed string   


# num10=complex("23"+8)      # TypeError: can only concatenate str (not "int") to str

# num10=complex(5,"34")     # TypeError: complex() second arg can't be a string

# num10=complex("123","6.8")  # TypeError: complex() can't take second arg if first is a string


a=65
b=20
print("Addition is", a+b)
print("Subtraction is", a-b)
print("Multiplication is", a*b)
print("Division is", a/b)
print("Remainder is", a%b)
print("Floor Division is", a//b)

a= 2
b= 3
a=b
print(a)
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a%=b
print(a)
a//=b
print(a)



a=65
b=20

if a==b:
    print("a and b are equal")
if a!=b:
    print("a is not equal to b")
if a>b:
    print("a is greater than b")
if a<b:
    print("a is less than b")
if a>=b:
    print("a is greater than equal to b")
if a<=b:
    print("a is less than equal to b")



In Python, to write an empty class pass statement is used.
 pass is a special statement in Python that does nothing.
It only works as a dummy statement.
However, objects of an empty class can also be created.
"""

class MyClass:
    pass


m1=MyClass()
m2=MyClass()
print(m1 is m2) #is m1 and m2 reffering to same object
print(m1 is not m2)

m2=m1
print(m1 is m2) #is m1 and m2 reffering to same object
print(m1 is not m2)



a=6
b=2

if a>10 and b<5:
    print("a is greater than 10 and b is less than 3")
if a>10 or b<5:
    print("either a is greater than 10 or b is less than 5")
print(not a>b)
print(not a<b)


num=5
print(num*2)
print(num**2)  # square of 5


name=input("Enter your name")
print("Name entered is\t",name)
age=int(input("Enter your age"))
print("Age entered is\t",age)
# age+=10  #  TypeError: can only concatenate str (not "int") to str
#age= int(age)
age+=10
print("Age after 10 years will be\t",age)




a=0
if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")


num=3
if num > 0:
    if num < 10:
        print("greater than 0 but less than 10")
    else:
        print("greater than 0 and equal to or more than 10")
elif num < 0:
    print("it is negative")
else:
    print("it is zero")    


 # a=7
a=3
match a:
        case 5:
                print("it is 5")
        case 7:
                print("it is 7")
        case _:  #default one
                print("not a desired number")


var=4.5
match var:
    case 3.4: 
            print("it is 3.4")
    case 4.5:
            print("it is 4.5")
    case _: 
            print("not a valid number")

var1=True
match var1:
    case True:
            print("it's true")
    case False:
            print("it's false")
    case _:
            print("invalid condition")

   

x, y = 8, 5
print("Before Swapping", x, y)

#First right gets assigned to first left, second right gets assigned to second left, at the same time. 
x, y = y, x     
x,y=5,8
print("After Swapping", x, y)



#LOOPS


i=1
while(i<10):
    print(i)
    i+=1



i=1
while(1):
    if(i==6):
        break
    print(i)
    i+=1

for i in range(1,10):
    print(i)


for i in range(1 , 10):

    if(i==6):
      
         continue
    print(i)    


for i in range(2,10):
      if(i==3):
            continue
print(i)


for i in range(1,3):
       for j in range(1,3):
           print(str(i)+"\t"+str(j))


for i in range(ord('A'), ord('K')+1): # ord = converts char to int
    print(chr(i))  #chr = convert int  to character


ai = 22
print("positive") if(ai>0) else print("negative")    


while True:
      i = int(input("Enter number: "))
      if (i==22):
            break


i = 1
for _ in iter(int, True):
    #if i == 700:
        #break
    print(i)
    i += 1


for i  in range(5): #by default its start with zero
      print("hello")


for i in range(0,5):
      if i ==2:
            break
      print(i)
else:
      print("done")      

for i in range(2,37):
      if i    



      
