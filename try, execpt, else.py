'''
#try and except is like IF else
try:
    x = int(input("what's x?"))
    print(f"X is {x}")
except ValueError:
    print("x is not an integer")


# we add ELSE
try:
    x = int(input("what's x?"))
except ValueError:
    print("x is not an integer")
    
else:
    print(f"X is {x}")

while True:
    try:
        x = int(input("what's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break 

print(f"X is {x}")
'''

while True:
    try:
        x = int(input("what's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break 

print(f"X is {x}")
