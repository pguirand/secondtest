print("hello")
print("BOnjour, My name is Pierre")

def display_lines(n=10):
    for i in range(n):
        print("-"*i)

def addition(a=5, b=10):
    return a+b

def masterb():
    print("In master branch")

display_lines()
print(addition())
masterb()
