# List constructor is list()
# List literal is []
# List is a "set of sequence of character".
# List support indexing
# List support slicing
# List is mutable

a=list()
print(a,type(a),id(a))  # [] <class list> 1254778668096

b=[]
print("b",b,type(b),id(b))


c=[]
print("c",c,type(c),id(c))

d=[]

print("d",d,type(d),id(d))  #d [] <class 'list'> 2752479868160

e=d        # in this senerio id must be same
print("e",e,type(e),id(e))    #e [] <class 'list'> 2752479868160

f=[1,"krishna",10.02]
print(f)

#indexing 
print(f[0])
print(f[1])

print(f[0:2])

g=["soap","detergent",["concrete","sand","rod"],"vegetable","flour"]
print(g)
h=g[2]       #['concrete', 'sand', 'rod']
print(g[2][0])     #['concrete', 'sand', 'rod']


i=[1,2,3,4,[2,3,1,[3,5,342],3,23],54]
print("i",i)
j=i[4]   #[2,3,1,[3,5,342],3,23]
print("j", j)
k=j[3]      #[3,5,342]
print("k",k)    
l=k[2]
print("l", l)

print("342",i[4][3][1:])

i=[1,2,3,4,[2,3,1,[3,5,342],3,23],54]
print("i",i)
j=i[4]   #[2,3,1,[3,5,342],3,23]
print("j", j)
k=j[3]      #[3,5,342]
print("k",k)    
l=k[1:]
print("l", l)  #[5,342]

print([1,2,3,4,[2,3,1,[3,5,342],3,23],54][4][3][1:])

#mutability

m=[1,2,3,4,5,6]

print(m)

print(help(m))
print(dir(m))

#'append', 'clear', 'copy', 'count', 'extend',
#'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

n=[]
print(n.append(2))  #None 
print(n)        #[2]

o="krishna"
z=o.upper()    #KRISHNA
print(z)

p=[2,3,1,3,45,5]
print(p.clear())
print(p)   #[]

q=[1,2,3,4,5]
r=q
print("q",q,id(q))
print("r",r,id(r))

r.append(1000000000)
print("q",q,id(q))
print("r",r,id(r))


a=[1,2,3,4]
b=[2,3,4,5]
print(a+b)
# print(a*b)

# python array
import array

a=array.array("I",[1,2,3,4,5])
print(a)












