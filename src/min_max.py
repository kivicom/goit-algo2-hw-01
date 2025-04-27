def find_min_max(arr):
    """
    Find the minimum and maximum elements in an array using the divide and conquer approach.

    Args:
        arr (list): A list of numbers.

    Returns:
        tuple: A tuple containing the minimum and maximum values (min, max).

    Raises:
        ValueError: If the input array is empty.
    """
    # Check for empty array
    if not arr:
        raise ValueError("Array cannot be empty")
    
    # Base case: array with one element
    if len(arr) == 1:
        return arr[0], arr[0]
    
    # Base case: array with two elements
    if len(arr) == 2:
        return (min(arr[0], arr[1]), max(arr[0], arr[1]))
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively find min and max for each half
    left_min, left_max = find_min_max(left_half)
    right_min, right_max = find_min_max(right_half)
    
    # Combine results by comparing min and max values
    return (min(left_min, right_min), max(left_max, right_max))

# Test cases
if __name__ == "__main__":
    test_cases = [
        [4, 2, 7, 1, 9, 3],  # Normal array
        [1],                  # Single element
        [5, 5, 5],           # Repeated elements
        [2, 1]               # Two elements
    ]
    
    for arr in test_cases:
        result = find_min_max(arr)
        print(f"Array: {arr}, Minimum: {result[0]}, Maximum: {result[1]}")
