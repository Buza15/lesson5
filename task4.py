def decorator(fn):
    def inner():
        print ("First one")
        fn()
    return inner

@decorator
def check(both = "Second one"):
    print (both)

check()