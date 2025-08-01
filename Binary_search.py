def binary_search(lst, n):
    S = sorted(lst) 
    low = 0 #first index
    high = len(S) - 1 #last index
    
   
    def search_recursive(low, high):
        if low > high:  
            return "not found"
        
        mid = (low + high) // 2  
        
        if S[mid] == n:  
            return mid  
        elif S[mid] > n:  # If the target is smaller, search the left half
            return search_recursive(low, mid - 1)
        else:  # If the target is larger, search the right half
            return search_recursive(mid + 1, high)
    
    # Start the recursive search
    return search_recursive(low, high)

lst = [12, 34, 54, 32, 11, 56, 89]
n = 89
Z = binary_search(lst, n)
print(Z)
