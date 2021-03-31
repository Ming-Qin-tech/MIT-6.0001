try:
    a = int(input("input a number"))
    b = int(input("input a number"))
    print(a/b)
except:
    print("bug in user input")
else:
    print("none mistake")
finally:
    print("whatever")
