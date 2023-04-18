a=10    # global variable / global scope
print(a)

def krishna():
    print(a)
krishna()


def kumar():
    b=20    #local variable/local scope
    print(b)

kumar()

# print(b)

def prajapti():
    global c
    c=30   #converting local to global
    print(c)

prajapti()

print(c)



d=100

def value(arg):
    print(arg)
value(d)
