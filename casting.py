#str()--> string 
#int()--> Integer
#float()--> float
#list()--> list
#tuple() --> tuple
#set()  --> set
#dict()  --> dictionary
#bool() --> boolean
#complex()--> complex 


a=1
print("a",a,type(a))
b=str(a)             #str() convert integer to string
print("b",b, type(b))  #1 <class 'str'>

c=float(a)   #1.0
print(c)

d=10.0
print(int(d))

# c="krishna"
# print(float(c))     #error

d="10k"
e=d[0:2]     #"10"
print("e",e,type(e))
f=int(e)
print("f",f,type(f))


d="10k"
print(type(int(d[0:2])))   #<class 'int'>
print(int(d[0:2]))   #10


d="10k"
print(type(int(d[0:2])),int(d[0:2]))   #<class 'int'> 10



e="10.0"
f=float(e)   #10.0
print(f)
g=int(f)     #10
print(g)


e="10.0"
print(int(float(e)))

# Casting of collection

a=[1,"krishna",1.01]
print("a",a,id(a))
d=tuple(a)
print("d",d,id(d))

e=set(d)     #{1, 'krishna', 1.01}
print(e)

print(id(1))
print(id(1.0))

f=list(e)
print(f)

# g=tuple(f)
print(tuple(f))

a=1
print(complex(a))

a=10,20
print(a)    #(10,20)


c,d=10,20
print("c",c)    #10
print("d",d)    #20
d,c=10,20
# c,d=20,10
print("c",c)    #20
print("d",d)    #10

# swap two variable using third variable temp

l=10
m=20

temp=l+m   #30
l=temp-l   #30-10
m=temp-m   #30-20

print("L",l)
print("m",m)














