# Task 1.

# The key operations in the simple_sort function are:
# Outer Loop: 
# The outer loop iterates n times, where n is the length of the input array arr.
# Inner Loop: 
# The inner loop iterates (n-i-1) times for each iteration of the outer loop.

# Task 2.

# In the worst case, the outer loop will execute n times, and for each iteration of the outer loop, the inner loop will execute (n-i-1) times, where i is the current iteration of the outer loop.
# which is approximately O(n^2)
# The Big O complexity of the simple_sort algorithm is O(n^2), which means that as the input size n increases, the runtime of the algorithm grows quadratically.

# Task 3.

# Optimized Bubble Sort:
# One optimization to the Bubble Sort algorithm is to introduce an additional flag variable that keeps track of whether any swaps were performed in the current iteration of the outer loop.

# Merge Sort:
# Merge Sort has a time complexity of O(n log n) in the average and worst cases, making it more efficient than the simple_sort algorithm for large input sizes.

# Quicksort:
# Quicksort has an average-case time complexity of O(n log n) but can degrade to O(n^2) in the worst case when the input is already sorted or reverse sorted.








