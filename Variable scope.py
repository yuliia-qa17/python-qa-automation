var_1 = 10 #global variable
var_2 = 20 #global variable
print(var_1, var_2)
def summ():
    var_1 = 30 #local variable
    var_2 = 40 #local variable
    result = var_1 + var_2
    print(result)

def sub():
    var_1 = 50 #local variable
    var_2 = 40 #local variable
    result = var_1 - var_2
    print(result)
summ()
sub()