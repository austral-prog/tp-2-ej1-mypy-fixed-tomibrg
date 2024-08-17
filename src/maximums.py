def max_of_two(x:int, y:int) -> int:
    """Given x and y, that are 2 numbers, return the biggest number."""
    biggest: int = x
    if x >= y:
        return biggest
    else:
        return y

# Replace the "ANSWER HERE" for your answer
def max_of_three(x: int, y: int, z: int) -> int:
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    biggest_of_two: int = max_of_two(x,y)
    if biggest_of_two >= z:
        return biggest_of_two
    else:
        return z
    

print(max_of_two(5,4)) # Retorna: 5

print(max_of_two(-2,-3)) # Retorna: -2

print(max_of_two(0,0)) # Retorna: 0

print(max_of_three(5,4,7)) # Retorna: 7

print(max_of_three(-2,-3,-1)) # Retorna: -1

print(max_of_three(0,0,0)) # Retorna: 0