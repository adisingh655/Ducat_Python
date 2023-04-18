#string
# string's constructor is str()
#string's literal is " ",' ',""" """,''' '''.
# string is a set of sequence of character
# string support indexing
#string support slicing
#string is immutable.

a="Global"
print(a)
b='Global'
print(b)
c="""Global"""
print(c)
d='''Global'''
print(d)

#creating empty string using either string literal or constructor
e=str()
print("e",e,type(e),id(e))

#literal for empty string
f=''
print(f,id(f))
g=""
print(g,id(g))

h=""""""
print(h,id(h))

i=''''''
print(i,id(i))

#Indexing

j="GLOBAL"
print(j[2])  #'O'
print(j[3])  #'B'
print("CHIPS"[3])

#Negative Indexing
print(j[0])
print(j[-6])
print(j[3:])

print(j[3::1])

a="GLOBAL"
print("Positive Indexing :",type(a[0]),a[0])
print("Negative Indexing :",type(a[-6]),a[-6])

#Slicing
a="GLOBAL"

b=a[10000:50000]
print(b,end="\n")   #empty

c=a[1:6:1]
print(c)     #LOBAL


d=a[1:6]
print(d)


e=a[-5:-1:1]
print(e)


f=a[-5:-1:-1]
print(f)       #empty

g=a[0:6:1]
print(g)    #global

h=a[::1]
print(h)

i=a[::]
print(i)
j=a[:]
print(j)

k=a[-5:-1:1]
print(k)

l=a[-6::1]
print(l)

m=a[-1:-7:-1]
print(m)    #LABOLG

n=a[:-7:-1] #LABOLG
print("n",n)

o=a[-1::-1] #LABOLG
print("o",o)

p=a[::-1]
print("p",p)
a="krishna"
b="kumar"
print(a+b)   # concatination 

