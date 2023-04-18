#float datatype:
#int=[0,1,2,3,4,5,6,7,8,9]
#float=[0.0,1.0,2.0,3.,4.,5.,6.,7.,8.,9.]

# float constructor is float()
# float literal is 0.0

a=10.0     #1gb
print(a)

print(type(a))
print(id(a))   #2225712353680


b=10.0     
print(id(b),"b")

d=22
e=22

print(id(d),"d")
print(id(e),"e")




f=10002344567
g=1000

print(id(f),"f")
print(id(g),"g")

k=10.0
print("k",k,type(k),id(k))
l=int(k)  #k=10.0
print("l",l,type(l),id(l))  #l=10

m=10.99
print("m",m,type(m),id(m))

#conversion float to int
n=int(m)  #m=10.99
print("m",n,type(n),id(n))

#What is casting? ==>

o="krishna"
p=int(o)


