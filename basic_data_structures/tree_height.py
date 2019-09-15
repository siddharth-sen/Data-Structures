# python3

import sys
import threading


def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def path_length(parent, cache, node):
    if parent[node] == -1:
        return 1

    if cache[node]:
        return cache[node]

    cache[node] = 1 + path_length(parent, cache, parent[node])
    return cache[node]


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    cache = [None]*n
    # print(compute_height(n, parents))
    print(max([path_length(parents, cache, i) for i in range(n)]))



# In Python, the default limit on recursion depth is rather low,
# so it is raised here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()




