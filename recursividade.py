def fatorial(n):
    if (n == 1):
        return 1
    x = n-1
    y = fatorial(x)
    return (n * y)

print(fatorial(5))

def fibonacci(n):
    return n if n == 0 or n == 1 else fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))

def func(n):
    if (n == 0):
        return 0
    else:
        return (n%10 + func(int(n/10)))

print(func(9))

def printStr(nome):
    if ( nome == ''):
        return 'acabou'
    print(nome[0], end='')
    printStr(nome[1:])

print(printStr('ifpb'))

def printStrInvertida(nome):
    if ( nome == ''):
        return    
    printStrInvertida(nome[1:])
    print(nome[0], end='')

print(printStrInvertida('ifpb'))

def tamanhoStr(nome):
    if ( nome == ''):
        return 0    
    else: 
        return 1 + tamanhoStr(nome[1:])

print(tamanhoStr('ifpb'))

    
'''
Ou:

def fatorial(n):
    if (n == 1):
        return 1
    else:
        return (n* fatorial(n-1))


print(fatorial(5))

Ou ainda:

def fatorial(n):
    return 1 if n == 1 else n* fatorial(n-1)


print(fatorial(5))

 '''

