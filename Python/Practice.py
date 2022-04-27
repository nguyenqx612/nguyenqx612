import threading

def function1():
    for x in range(1000):
        print("One")
def function2():
    for x in range(1000):
        print("Two")

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t1.run()
t2.run()