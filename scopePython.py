x = 89
def func1():
    x = 20                                  # this is a local variable thus it won't change the value in the original x
    def func2():
        global x                            # here we are like cloning the original variable x (in technical term it is known as using a variable outside it's current scope)
        x = 88                              # changing the cloned variable x (modifying the variable(x) outside it's current scope)
    print('Before Calling func2()', x)      # here x contains 20, because it is a local variable which is being printed
    func2()                                 # now we are calling func2() but still x in func1() is a local variable thus it won't reflect changes to x of func1
    print('After Calling func2()', x)       # that's why it printed 20 as value of x here which is the value of local variable x of func1()

func1()                                     # calling func1() which will eventually call func2(),
                                            # now func2() will chage the value of original variable x
print(x)                                    # it printed 88 because in line 6
                                            # the value was changed to 88 instead of 89 thus the value of original variable x is 88