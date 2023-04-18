# string is immutable we cant change a string beacuse no methods
#and function available in python to change a string 

a="krishna"
print(a)

a="kumar"
print(a)

print(a.capitalize())  #Kumar
print(a.upper())       #KUMAR

print(a)

print(a.center(11))
print(a.count('k'))   #count() method help to count specific character into a string

print(a.isalpha())
print(a.isnumeric())
print(a.encode())
print(a.endswith('r'))
print(a.expandtabs(16))

class ABC:
    def new(self,a,space):
        str1=""
        for i in a:
            str1+=i+space
        return str1

a=ABC()
print(a.new("Kumar","India"))
