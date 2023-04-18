# def sub():
#     a=2
#     b=3
#     if a<b:
#         a,b=b,a
#     print(a-b)
def super(sub):
    def inner(a,b):
        if a<b:
            a,b=b,a
        sub(a,b)
    return inner

def sub(a,b):
    print(a-b)

val=super(sub)
val(2,3)


def div(a,b):
    print(a/b)

div(2,3)
print(3/2)