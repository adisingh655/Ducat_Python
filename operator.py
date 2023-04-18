# operator  = +,-,/,//,**,or, is, not, in, etc...

#operands   ="a+b"; a,b are operands

# Arithmetic operators : +,-,/,*,**,//,%

a=10.0
b=20
print(a+b)  #30
print(a-b)  #-10
print(a/b)
print(10/2)
print(10+2)
print(10.0+2.0)
print(10//3)
print(20/3)
print(20//3)

print(2**3.0)
print(2*3)

print(20%3)


# Assignment operator

a=10
a=a*3  #30
a*=3    #90
a=a/3
a/=3
print(a)

b=10
c=b+20
c+=20

c=10
# c=c+20
c+=20
print(c)

# Comparison operator

# less then   <
# greater then >
# equal to  ==
# not equal to    !=
# greater then equal to >=
# less then equal to <=


print(2>1)    #True
print(2<1)    #False
print(2<4)    #True
print(2==2)   #True
print(2!=2)   #False
print(2>=2)   #True
print(2>=1)   

#python Logical operator:
# AND, OR, NOT

a=2
b=3
c=2

print(a==c and c!=b)
print(a==c and c==b and a==b)   #False

print(a==c and c==b and a!=b)   #False


print(a==c and c!=b and a!=b)   #True

print(not(a==c and c!=b and a!=b))  

print(1 is 1)     #True

print(1 is not 1)  #False

# membership operator

a="this is python"
print("python" in a)   #True
print("python" not in a)
print("Python" not in a)

print(~12)    #-13
print(bin(12))

print(12 | 13)
print(bin(12))
print(bin(13))


print(12 & 13)
print(bin(12))
print(bin(13))

# left shift and right shift

print(12<<2)    # Right shift
print(bin(12))

print(12>>2)   #3

k,l=2,3
l,k=2,3
k,l=k,l

a=1,2,3,4,
print(a)

k,l,m,n=a
print(k)
print(l)
print(m)
print(n)

