# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3


def most_frequent(numbers):
    # Your code here
    return max(set(numbers), key=numbers.count)
Numbers = [1, 2, 3, 4, 5, 2, 3]
print(most_frequent(Numbers))

"""
Time and Space Analysis for problem 1:
- Best-case: 2
- Worst-case: 5 
- Average-case: 2
- Space complexity: 7

- Why this approach?
The reason this approach is beneficial since it can find what's the most frequent number that is shown
on the lists. 
- Could it be optimized?
Yes, it can be optimized but it'll require some additional coding in order for the function to be 
optimized.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    # Your code here
    nums = [4, 5, 4, 6, 5, 7]
    seen = []

    for nums in Numbers:
        if nums not in seen:
            Numbers.append(nums)
        print(seen)


"""
Time and Space Analysis for problem 2:
- Best-case:  4
- Worst-case: 6
- Average-case: 4
- Space complexity: 7
- Why this approach?
So this approach on remove some duplicates that is shown in the list
and can shorten the list until there are no duplicates.
- Could it be optimized?
Yes, It's possible. 
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    # Your code here
    result = ([1, 2, 3, 4])
    for item in nums:
        if item == target:
            result.append(item * 2)
        return result
    return None


"""
Time and Space Analysis for problem 3:
- Best-case:
- Worst-case:
- Average-case:
- Space complexity:
- Why this approach?
- Could it be optimized?
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    # Your code here
    pass


"""
Time and Space Analysis for problem 4:
- When do resizes happen?
Resize can happen if the list is too much.
- What is the worst-case for a single append?

- What is the amortized time per append overall?

- Space complexity:
- Why does doubling reduce the cost overall?
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total():
    # Your code here
    nums = [1, 2, 3, 4]
    return nums


res = running_total()
print(res)

"""
Time and Space Analysis for problem 5:
- Best-case: 2
- Worst-case: 3
- Average-case: 4
- Space complexity: 1

- Why this approach?
This approach is beneficial since it can sum up some numbers in the list and can print out
the full total of the number that is added together.
- Could it be optimized?
Yes, it can be optimized.
"""
