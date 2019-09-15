# python3
#
# from collections import namedtuple
#
# AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
#
#
# def assign_jobs(n_workers, jobs):
#     # TODO: replace this code with a faster algorithm.
#     result = []
#     next_free_time = [0] * n_workers
#     for job in jobs:
#         next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
#         result.append(AssignedJob(next_worker, next_free_time[next_worker]))
#         next_free_time[next_worker] += job
#
#     return result
#
#
# def main():
#     n_workers, n_jobs = map(int, input().split())
#     jobs = list(map(int, input().split()))
#     assert len(jobs) == n_jobs
#
#     assigned_jobs = assign_jobs(n_workers, jobs)
#
#     for job in assigned_jobs:
#         print(job.worker, job.started_at)
#
#
# if __name__ == "__main__":
#     main()

# class MinHeap:
#
#     def __init__(self, n_workers):
#         self._data = []
#         self.n = n_workers
#         for i in range(n_workers):
#             self._data.append((i, 0))
#
#     def Parent(self, i):
#         return self._data[int((i-1)/2)]
#
#     def LeftChild(self, i):
#         return 2*i + 1
#
#     def RightChild(self, i):
#         return 2*i + 2
#
#     def



class MinHeap:
    def __init__(self, num_workers):
        # each worker contains (rank(index), next_free_time)
        self._data = []
        self.n = num_workers
        for i in range(num_workers):
            self._data.append((i, 0))

    def Parent(self, i):
        return self._data[int((i-1)/2)]

    def LeftChild(self, i):
        return 2 * i + 1

    def RightChild(self, i):
        return 2 * i + 2

    def CompareWorker(self, worker1, worker2):
        if worker1[1] != worker2[1]:
            return worker1[1] < worker2[1]
        else:
            return worker1[0] < worker2[0]

    def SiftUp(self, i):
        while i > 0 and self.CompareWorker(self._data[i], self._data[self.Parent(i)]):
            self._data[i], self._data[self.Parent(i)] = self._data[self.Parent(i)], self._data[i]
            i = self.Parent(i)

    def SiftDown(self, i):
        minIndex = i
        left = self.LeftChild(i)
        if left < self.n and self.CompareWorker(self._data[left], self._data[minIndex]):
            minIndex = left

        right = self.RightChild(i)
        if right < self.n and self.CompareWorker(self._data[right], self._data[minIndex]):
            minIndex = right
        if i != minIndex:
            self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
            self.SiftDown(minIndex)

    def ChangePriority(self, index, priority):
        old_p = self._data[index][1]
        self._data[index] = (self._data[index][0], priority)
        if priority < old_p:
            self.SiftUp(index)
        else:
            self.SiftDown(index)

        self.SiftDown(index)


class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        min_heap = MinHeap(self.num_workers)
        for i in range(len(self.jobs)):
            self.assigned_workers[i] = min_heap._data[0][0]
            self.start_times[i] = min_heap._data[0][1]
            min_heap.ChangePriority(0, min_heap._data[0][1] + self.jobs[i])


    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
    
    
