# Hàm Matrix
def Matrix(column,row):
    matrix = []
    for _ in range(column):#(row)
        list1 = []
        for _ in range(row):#(column)
            list1.append(0)
        matrix.append(list1)
    return matrix

#Hàm Fibonacci số thứ n trong dãy
def Fibonacci(n):
    number1 = 0
    number2 = 1
    if n == 1 or n==2:
        return n-1
    for _ in range(n-2):
        sum = number1 + number2
        number2 = sum
        number1 = number2
    return sum

def Fibonaccii(n):
    if n == 1 or n==2:
        return n-1
    else:
        return Fibonaccii(n-1) + Fibonaccii(n-2)


#Hàm giai thừa
def Factorial(n):
    result1 = 1
    if n == 0:
        return 1
    for i in range(1,n+1):
        result = result1 * i
        result1 = result
    return result

def Factoriall(n):
    if n == 0:
        return 1
    return n * Factoriall(n-1)


