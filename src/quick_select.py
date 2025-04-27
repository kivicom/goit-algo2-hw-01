def quick_select(arr, k):
    """
    Find the k-th smallest element in an unsorted array using Quick Select algorithm.

    Args:
        arr (list): A list of numbers.
        k (int): The position (1-based) of the desired smallest element.

    Returns:
        int or float: The k-th smallest element in the array.

    Raises:
        ValueError: If k is out of bounds or the array is empty.
    """
    # Validate input
    if not arr:
        raise ValueError("Array cannot be empty")
    if k < 1 or k > len(arr):
        raise ValueError("k is out of bounds")
    
    # Convert k to 0-based index
    k = k - 1
    
    def partition(left, right, pivot_index):
        """
        Partition the array around a pivot and return the pivot's final position.

        Args:
            left (int): Left boundary of the subarray.
            right (int): Right boundary of the subarray.
            pivot_index (int): Index of the pivot element.

        Returns:
            int: Final position of the pivot.
        """
        pivot_value = arr[pivot_index]
        # Move pivot to the end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left
        
        # Partition elements
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        
        # Move pivot to its final position
        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index
    
    def select(left, right):
        """
        Recursively find the k-th smallest element in the subarray.

        Args:
            left (int): Left boundary of the subarray.
            right (int): Right boundary of the subarray.

        Returns:
            int or float: The k-th smallest element.
        """
        # Base case: single element
        if left == right:
            return arr[left]
        
        # Choose pivot (last element for simplicity)
        pivot_index = right
        pivot_index = partition(left, right, pivot_index)
        
        # If pivot is the k-th element
        if k == pivot_index:
            return arr[k]
        # If k is in the left partition
        elif k < pivot_index:
            return select(left, pivot_index - 1)
        # If k is in the right partition
        else:
            return select(pivot_index + 1, right)
    
    return select(0, len(arr) - 1)

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([4, 2, 7, 1, 9, 3], 3),  # Normal array, k=3
        ([1], 1),                  # Single element, k=1
        ([5, 5, 5], 2),           # Repeated elements, k=2
        ([2, 1], 1),              # Two elements, k=1
    ]
    
    for arr, k in test_cases:
        # Create a copy to avoid modifying the original array
        arr_copy = arr.copy()
        result = quick_select(arr_copy, k)
        print(f"Array: {arr}, k: {k}, k-th smallest: {result}")
