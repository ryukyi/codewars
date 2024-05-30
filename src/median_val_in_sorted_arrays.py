"""
Task
You have a list arrays of N arrays of positive integers, each of which is sorted in ascending order.

Your taks is to return the median value all of the elements of the combined lists.

Example
arrays =[[1,2,3],[4,5,6],[7,8,9]] In this case the median is 5

arrays =[[1,2,3],[4,5],[100,101,102]] In this case the median is 4.5

Some of the arrays may be empty, but there will always be at least one non-empty array in the list

Tests
50 Small Tests: 5 arrays, each with up to 20 elements
50 Medium Tests: 10 arrays, each with up to 1,000 elements
50 Large Tests: Up to 15 arrays, each with up to 2,000,000 elements
"""

import heapq
from typing import List


class MedianFinder:
    def __init__(self):
        self.low = []  # Max heap (invert min-heap)
        self.high = []  # Min heap

    def add_num(self, num: int):
        # Add to max heap
        heapq.heappush(self.low, -num)
        # Only balance the heaps if necessary
        if self.high and (-self.low[0] > self.high[0]):
            heapq.heappush(self.high, -heapq.heappop(self.low))

    def balance_heaps(self):
        # Balance the heaps to ensure their sizes differ by no more than one
        while len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        while len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def find_median(self) -> float:
        # Ensure heaps are balanced before finding median
        self.balance_heaps()
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2.0


def median_from_n_arrays(arrays: List[List[int]]) -> float:
    median_finder = MedianFinder()
    for array in arrays:
        for number in array:
            median_finder.add_num(number)
    return median_finder.find_median()


if __name__ == "__main__":
    result = median_from_n_arrays([[1, 2, 3], [4, 5], [100, 101, 102]])
    print(result)
