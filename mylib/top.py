import sub 

def doSomethingTop():
    print("top callingsub:")
    sub.doSomethingSub()

def test():
    doSomethingTop()

if __name__ == "__main__":
    test()
