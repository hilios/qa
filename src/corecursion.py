"""Tree traversal problems

- DFS: Depth-firt search
- BFS: Breadth-first search
"""

# Recursion will first find the last iteration, and then execute all bottom
# to the top.
#
# This is know as Depth-firt search (DFS), this method allocate all memory and
# then remove after the calculation is done for that iteration, following a
# stack (LIFO) distribution.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# In the other hand, we have the Corecursion, that opposite to the former always
# start the iteration from the first node, and then proceed to the next one,
# until reachs a end (or not).
#
# This is the Breadth-first search (BFS), where we allocate the necessary memory
# for the calculation, and after is done, we release it, this follows a queue
# (FIFO) distribution.
#
# An analogy to this paradigm is infite thread that will be execute in a
# organized manner until reachs it's end, and as infite loope maybe doens't.
def factorials():
    n, f = 0, 1
    while True:
        yield f
        n, f = n + 1, f * (n + 1)


def n_factorials(k):
  n, f = 0, 1
  while n <= k:
    yield f
    n, f = n + 1, f * (n + 1)

def nth_factorial(k):
    n, f = 0, 1
    while n < k:
        n, f = n + 1, f * (n + 1)
    yield f

print 'iterate n factorials until reach 120 = 5!'

for i in factorials():
  if i > 120:
    break
  else:
    print(i)


five_factorials = n_factorials(5)

print 'n_factorials(5)'

# Print all factorial up to 5
for f in five_factorials:
  print f

print 'n_factorials(5) second run'

# Never executed because generators are run only once
for f in five_factorials:
  print f

print 'nth_factorial(5)'

print nth_factorial(5).next()
