
tree1 = [[21, 19], [[3, 5], 0]]
tree2 = [[12, 3], 6]
tree3 = [[26], [18, 3, 2], [8]]


# Part A1: Multiplication on tree leaves

def mul_tree(tree):
    """
    Recursively computes the product of all tree leaves.
    Returns an integer representing the product.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
    Outputs
       total: An int equal to the product of all leaves of the tree.

    """
    
    # Define the base case (product of leaves for an empty list == 1)
    total = 1
    
    # Loop over the elements in tree
    for t in tree:
        
        # If element is an int multiply the total by the int value
        if type(t) == int:
            total *= t
        
        # If element is a list do recursive operation (use mul_tree function inside itself)
        if type(t) == list:
            total *= mul_tree(t)
    return total
    
    pass

# Part A2: Arbitrary operations on tree leaves

def sumem(a,b):
    """
    Example operator function.
    Takes in two integers, returns their sum.
    """
    return a + b

def prod(a,b):
    """
    Example operator function.
    Takes in two integers, returns their product.
    """
    return a * b



def op_tree(tree, op, base_case):
    """
    Recursively runs a given operation on tree leaves.
    Return type depends on the specific operation.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
       op: A function that takes in two inputs and returns the
       result of a specific operation on them.
       base_case: What the operation should return as a result
       in the base case (i.e. when the tree is empty).
    """
    # Define the base case 
    total = base_case
    
    # Loop over the elements in tree
    for t in tree:
        
        # If element is an int update total by calling op on element and total
        if type(t) == int:
            total = op(t, total)
        
        # If element is a list call op in a recursive operation (use op_tree function inside itself)
        if type(t) == list:
            total = op(total, op_tree(t, op, base_case))   

            
    return total

    pass

# Part A3: Searching a tree

def search_div_three(a, b):
    """
    Operator function that searches for divisible-by-three values within its inputs.

    Inputs
        a, b: integers or booleans
    Outputs
        True if either input is equal to True or divisible-by-three, and False otherwise
    """
    
    # Check the type of a and b
    if type(a) == int and type(b) == int:
        
        # If both are int and either divisible by 3 (remainder of division by 3 is zero)
        return (a % 3 == 0) or (b % 3 == 0)
    
    # If a is bool, check type of b
    elif type(a) == bool:
        if type(b) == bool:
            return a or b
        else:
            return a or (b % 3 == 0)
    
    # If a is int and b is bool
    else:
        return (a % 3 == 0) or b
    
    
#    passx

if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below.
    pass
