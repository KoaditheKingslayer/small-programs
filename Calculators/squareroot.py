# Completed on 7/19/2024 as part of: Scientific Computing with Python (beta) - FreeCodeCamp 
# Learn the Bisection Method by Finding the Square Root of a Number

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')
    else: # The Bisection Loop
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2 # Find the midpoint pf low and high 
            square_mid = mid**2 # Square the midpoint

            if abs(square_mid - square_target) < tolerance: # if the result is within the tolerance
                root = mid # set the root to the mid and end the loop ( square root found )
                break 
            elif square_mid < square_target: # if the result is less than the target
                low = mid # the low point becomes the result, narrowing in the range for the next loop
            else: # if the result is larger than the target
                high = mid # the high point becomes the result, narrowing in the range for the next loop

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root

def main():
    while True:
        N = int(input("\nWhat number do you want to estimate the square root of? "))
        square_root_bisection(N)
        
main()