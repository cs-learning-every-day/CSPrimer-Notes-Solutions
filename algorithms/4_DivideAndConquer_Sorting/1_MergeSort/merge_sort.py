"""
- Naive sorting approaches in real life lead to bubble sort
- The more you try to sort cards, the more you come to the conclusion the problem is fundamentally O(n^2)

Naive Sorting (Selection Sort):
4 8 2 1 3 9 7
1 8 2 4 3 9 7
1 2 8 4 3 9 7
1 2 3 4 8 9 7
1 2 3 4 7 9 8
1 2 3 4 7 8 9

- Each scan requires O(n)

- In the worst case you assume n scans

- O(n^2) (In a good case its O(n^2)/2, but constant factor drops)


Insertion Sort:
4 8 2 1 3 9 7
4 2 8 1 3 9 7
2 4 8 1 3 9 7
2 4 1 8 3 9 7
2 1 4 8 3 9 7
1 2 4 8 3 9 7
1 2 4 3 8 9 7
1 2 3 4 8 9 7
1 2 3 4 8 7 9
1 2 3 4 7 8 9

- Also O(n^2)

- There are O(nlogn) sorting algorithms

Merge Sort:
- Break down the array recursively into single components
- Then merge components into arrays
- Then merge those
- If we have less than n merges, it takes less than O(n^2)
  - Generally we expect logn merges
- Doing merge sort without O(N) space is quite difficult
  - Part of the motivation for quick sort

Stretch Goal:
  - Get merge sort implementation where it only uses on additional array of size n for working memory
"""
import random


def merge_sort(arr: list[int]) -> list[int]:
    """
    Understand:
      - We are trying to break down the problem into the smallest parts, and then merge to gether the remaining pieces

    Plan:
      - arr_len = len(arr)
      - if arr_len == 1:
          return arr
      - arr_first_part = merge_sort(arr[:arr_len//2])
      - arr_second_part = merge_sort(arr[arr_len//2:])
      - sorted_arr = []
      - sorted = False
      - while not sorted:
          if arr_first_part and arr_second_part:
            arr_first_part_0 = arr_first_part[0]
            arr_second_part_0 = arr_second_part[0]
            if arr_first_part_0 < arr_second_part_0:
              sorted_arr.append(arr_first_part_0)
              arr_first_part.pop(index=0)
            else:
              sorted_arr.append(arr_second_part_0)
              arr_second_part.pop(index=0)
          elif arr_first_part:
            sorted_arr.extend(arr_first_part)
            arr_first_part = []
          elif arr_second_part:
            sorted_arr.extend(arr_second_part)
            arr_second_part = []
          else:
            sorted = True
        return sorted_arr
    """
    arr_len = len(arr)
    if arr_len == 1:
        return arr
    return merge(
      merge_sort(arr[:arr_len//2]),
      merge_sort(arr[arr_len//2:])
    )


def merge(arr_1: list[int], arr_2: list[int]) -> list[int]:
    sorted_arr = []
    while True:
        if arr_1 and arr_2:
            arr_10 = arr_1[0]
            arr_20 = arr_2[0]
            if arr_10 < arr_20:
                sorted_arr.append(arr_10)
                arr_1.pop(0)
            else:
                sorted_arr.append(arr_20)
                arr_2.pop(0)
            continue
        if arr_1:
            sorted_arr.extend(arr_1)
            arr_1 = []
        elif arr_2:
            sorted_arr.extend(arr_2)
            arr_2 = []
        return sorted_arr


random_ints = [random.randint(0,5000) for _ in range(100_000)]

TEST_CASES = [
  ([2,1], [1,2]),
  ([1,2], [1,2]),
  ([3,1,2], [1,2,3]),
  ([3,1,4,2], [1,2,3,4]),
  (random_ints, sorted(random_ints))
]

from tqdm import tqdm

if __name__ == '__main__':
  for case, expected_result in tqdm(TEST_CASES):
    try:
      result = merge_sort(case)
      assert result == expected_result
    except AssertionError:
      print(f"Case: {case}")
      print(f"Expected Result: {result}")
      print(f"Result: {result}")
      raise

  print('done')

  
