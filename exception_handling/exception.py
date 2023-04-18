
# try:
#     a=10
#     b=0
#     print(a/b)
# except:
#     print("number is not divisible by zero")

# print("hello")


# try:
#     a="krishna"
#     b=10
#     print(a/b)
# except:
#     print("number is not divisible by zero")

# print("hello")


# a="krishna"
# b=10
# print(a/b)


# try:
#     a="10"
#     b=0
#     print(a/b)

# except ZeroDivisionError as e :
#     print("Number not divisible by 0",e)
# except TypeError as e:
#     print("String is not divisible by int",e)
# except ValueError as e:
#     print("string is not convertible into int",e)

# except Exception:
#     print("Out of service")

# finally:
#     print("thankyou to banking with us")


try:
    a=10
    b=10
    print(a/b)
    raise 
        
except ZeroDivisionError as e :
    print("Number not divisible by 0",e)
except TypeError as e:
    print("String is not divisible by int",e)
except ValueError as e:
    print("string is not convertible into int",e)
except Exception:
    print("Out of service")

finally:
    print("thankyou to banking with us")
