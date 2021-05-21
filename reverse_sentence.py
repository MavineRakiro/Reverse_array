"""Write a function reverseSentence(A) that takes in an array of characters
, A, and reverses the the "words" (not individual characters).

Example:

A = ['t','h','i','s',' ','i','s',' ','g','o','o','d']
reverseSentence(A) A // ['g','o','o','d',' ','i','s',' ','t','h','i','s']
"""

A = ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'g', 'o', 'o', 'd']


def reverseSentence(A):
    a = ''.join(A).split()
    b = a[::-1]
    c = ' '.join(b)
    return list(c)


print(reverseSentence(A))