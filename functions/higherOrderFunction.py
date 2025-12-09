
def toBeCalled():
    print("to be called...")

def demo(a):
    print(a)
    a()
    

# demo(10)
# demo("")
# demo(False)
# demo([])
# demo({})
demo(toBeCalled)
    