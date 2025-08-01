def linear_search(list,n):
    for i in range (len(list)):
        if list[i]==n:
            return i
    else:
            return"not found"
list=[12,23,45,56,78,8,34]
n=78
z=linear_search(list,n)
print(z)


