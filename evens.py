# def even_number_of_evens(numbers):
#     """
#     Should Raise a TypeError if a list in not passed into the function
#     error message: "A list was not passed into the function"
#     if the list is empty it will return False
#     if the number of even numbers is odd - return False
#     if the numner of even numbers is even - return True
#     """

#     if isinstance(numbers, list):
#         if numbers == []:
#             return False
#         else:
#             evens = 0

#         for n in numbers:
#             if n % 2 == 0:
#                 evens += 1
#         if evens:
#             return evens % 2 == 0
#         else:
#             return False

#     else:
#         raise TypeError("A list was not passed into the function")

# if __name__ == "__main__":
#     print(even_number_of_evens(5))



def even_number_of_evens(numbers):
    """
    Should raise a TypeError if a list is not passed into the function.
    Error message: "A list was not passed into the function".
    If the list is empty, it returns False.
    If the number of even numbers is odd, it returns False.
    If the number of even numbers is even, it returns True.
    """
    if not isinstance(numbers, list):
        raise TypeError("A list was not passed into the function")
    
    if not numbers:  # Check if list is empty
        return False
    
    evens = sum(1 for n in numbers if n % 2 == 0)  # Count even numbers in the list
    
    return evens > 0 and evens % 2 == 0  # Return True if there is at least one even number and the count is even


if __name__ == "__main__":
    print(even_number_of_evens([2, 4, 6]))  # Example usage
    print(even_number_of_evens([2, 3, 6]))  # Example usage
    print(even_number_of_evens([]))  # Example usage
    print(even_number_of_evens(5))  # Example usage, should raise TypeError
