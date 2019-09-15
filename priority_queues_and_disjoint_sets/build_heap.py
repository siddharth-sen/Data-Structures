# python3


# def build_heap_naive(data):
#     """Build a heap from ``data`` inplace.
#
#     Returns a sequence of swaps performed by the algorithm.
#     """
#     # The following naive implementation just sorts the given sequence
#     # using selection sort algorithm and saves the resulting sequence
#     # of swaps. This turns the given array into a heap, but in the worst
#     # case gives a quadratic number of swaps.
#     #
#     # TODO: replace by a more efficient implementation
#
#     swaps = []
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] > data[j]:
#                 swaps.append((i, j))
#                 data[i], data[j] = data[j], data[i]
#     return swaps

# def main():
#     n = int(input())
#     data = list(map(int, input().split()))
#     assert len(data) == n
#
#     swaps = build_heap(data)
#
#     print(len(swaps))
#     for i, j in swaps:
#         print(i, j)

class BuildHeap:
    def __init__(self):
        self._swaps = []
        self._data = []

    def Read(self):
        n = int(input())
        self._data = [-1]
        self._data += [int(s) for s in input().split()]
        assert n == len(self._data) - 1

    def Write(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def SiftDown(self, i):
        min_i = i
        left = 2 * i
        right = 2 * i + 1

        if left <= len(self._data) - 1 and self._data[left] < self._data[min_i]:
            min_i = left
        if right <= len(self._data) - 1 and self._data[right] < self._data[min_i]:
            min_i = right

        if i != min_i:
            self._swaps.append((i - 1, min_i - 1))
            self._data[i], self._data[min_i] = self._data[min_i], self._data[i]
            self.SiftDown(min_i)

    def Swapper(self):
        for i in range((len(self._data) - 1) // 2, 0, -1):
            self.SiftDown(i)

    def Solve(self):
        self.Read()
        self.Swapper()
        self.Write()


if __name__ == '__main__':
    heap = BuildHeap()
    heap.Solve()

