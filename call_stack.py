def functhree():
    print("three")
    
def functwo():
    functhree()
    print("two")

def funcone():
    functwo()
    print("one")
    
funcone()