# Algorithms
Programming exercises from the Algorithms (Stanford) specialisation on Coursera

## Notes

Linearity of expectation - The expected value of a sum of random variables is equal to the
sum of expectations. Example: if we would like to calculate the expectation of the sum of
two dice we could compute the probability of and sum of all combinations (36)
alternatively we could sum the expectation of each single dice. The expectation of a single
dice is 3.5 (sum of 1 to 6 / 6). The expectation of the sum of two dice is 3.5 + 3.5 = 7

Independence: true if Pr[X and Y] = Pr[X] * Pr[Y]

or Pr[X|Y] = P[X]

If random variables are independent then:

E[A * B] = E[A] * E[B]

Sample space anything that can happen
## Programming Assignment 1 - Karatsuba Integer Multiplication

run ex1_karatsuba.py

## Programming Assignment 2 - Find Inversions

run ex2_inversions.py

## Programming Assignment 3 - Quick Sort

run ex3_quick_sort.py

## Programming Assignment 4 - Karger Min Cut

run ex4_random_contraction.py

## Programming Assignment 2-1 Graph search

run graph_search_iterative.py

Note: due to large file size SCC.txt is not committed to
git hub this file can be gained from the programming assignment instructions on coursera

Breadth first search (BFS) - queue
Depth first search (DFS) - stack
Strongly connected component (SCC)

Topological ordering use DFS

Directed, acyclic - no cycles

Sink vertex - no outgoing arc

## Programming Assignment 2-2 shortest path using Dijkstras algorithm and heap implementation

run dijkstra.py

## Programming Assignment 2-3 Maintaining Medians using heaps

run maintaining_medians.py

## Programming Assignment 2-4 2 Sum
