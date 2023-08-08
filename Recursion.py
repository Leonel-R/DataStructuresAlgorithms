def factorial_recursion(n):
    if n == 1:
        return 1
    return n * factorial_recursion(n-1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + n
    
#dynamic programming version of fibonacci sequence 
cache = [None]*(100)

def fibonacci2(n): 
    if n <= 1:
        return n
    
    # Check if the value exists
    if not cache[n]:
        # Save the result in cache
        cache[n] = fibonacci2(n-1) + fibonacci2(n-2)
    
    return cache[n]
    

print(fibonacci2(6))

#Towers of Hanoi puzzle

def hanoi(num_disks, from_rod, to_rod, aux_rod):
    if num_disks >= 1:
        hanoi(num_disks - 1, from_rod, aux_rod, to_rod)
        print("Moving disk", num_disks, "from rod", from_rod,"to rod",to_rod)
        hanoi(num_disks - 1, aux_rod, to_rod, from_rod)   

num_disks = 4
source_rod = 'A'
auxiliar_rod = 'B'
target_rod = 'C'

hanoi(num_disks, source_rod, target_rod, auxiliar_rod)