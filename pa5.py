'''
Shailesh Bolduc
DATA 120 Homework 5
'''

# PROBLEM 1
def gcd(a: int, b: int) -> int:
    '''
    Calculates the greatest common denominator of a and b using
    Euclid's Algorithm.
    '''

    # base cases
    if a == 0:
        return b
    if b == 0:
        return a
    
    return euclid_gcd(b, a % b)


# PROBLEM 2
def remove_pairs(path):
    """
    Optimize the path by removing U-turns and adjacent opposing directions.
    """
    opposite = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E'
    }

    if len(path) < 2:
        return path

    # check first two chars
    first_two = path[:2]
    if first_two[0] == opposite[first_two[1]]:
        # if they are opposite directions then remove them
        return remove_pairs(path[2:])
    else:
        return path[0] + remove_pairs(path[1:])
    # # check the last two characters
    # last_two = path[-2:]
    # if last_two[0] == opposite[last_two[1]]:
    #     # if they are opposite directions then remove them
    #     return optimize_path(path[:-2])
    # else:
    #     # else, continue with the rest
    #     optimized_rest = optimize_path(path[:-1])
    #     return optimized_rest + path[-1]


# PROBLEM 3
def bisection_root(func, x1, x2):
    '''
    Finds the root of a function using the Bisection Method.

    Args:
        func [function]: A function that accepts a single numeric argument and returns a numeric result.
        x1 [int]: The first endpoint of the interval.
        x2 [int]: The second endpoint of the interval.

    Returns:
        [int]: the root of the function

    Raises:
        [ValueError]: if initial values cannot possibly bracket a root
    '''
    moe = .0000001  # margin of error

    y1 = func(x1)
    y2 = func(x2)
    
    if y1 * y2 > 0:
        raise ValueError("Both y-values have the same sign. \
                         Can't bracket a root.")

    # midpoint
    x_mid = (x1 + x2) / 2
    y_mid = func(x_mid)
    
    # if y val is < .001, return the x
    if abs(y_mid) < moe:
        return x_mid
    
    # check to see which case is desirable. we want opposite signs of points
    if y1 * y_mid < 0:
        return bisection_root(func, x1, x_mid)
    else:
        return bisection_root(func, x_mid, x2)

    