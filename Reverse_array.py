"""
Write a function reverseArray(A) that takes in an array A
 and reverses it, without using another array or collection
 data structure; in-place.
Example:
A = [10, 5, 6, 9] reverseArray(A) A // [9, 6, 5, 10]
"""
A = [10, 5, 6, 9]

def reverseArray(A):
    return [list for list in A[::-1]]
print(reverseArray(A))

"""def reverseArray(A):
    return [list for list in reversed(A)]

print(reverseArray(A))"""