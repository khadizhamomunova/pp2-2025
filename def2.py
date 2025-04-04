def evens(n):
    i = 0  
    while i != n:
        if i % 2 == 0:
            yield i
        i += 1  

n = int(input("Введите число до которого нужно определить четность: "))
mylist = list(evens(n))
print(mylist)
