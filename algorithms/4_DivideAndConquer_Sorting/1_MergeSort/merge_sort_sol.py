"""
1. basic mergesort with slicing/copying as needed
2. refactor to use only N additional space, no extra list copies

"""


class MergeSort:
    def __init__(self, nums):
        self._working = [0] * len(nums)
        self.nums = nums

    def run(self):
        self._sort(0, len(self.nums))

    def _sort(self, left, right) -> None:
        """
        Sort the range in nums defined by [left, right)
        """
        if right - left <= 1:
            return
        mid = (right + left) // 2
        self._sort(left, mid)
        self._sort(mid, right)
        self._merge(left, right, mid)

    def _merge(self, left, right, mid) -> None:
        """
        Idea:
        left + xi -> li
        mid + yi -> ri
        left + xi + yi -> i
        """
        for i in range(left, right):
            self._working[i] = nums[i]
        li, ri = left, mid
        for i in range(left, right):
            # If we have hit the right index, copy remaining left values of working memory into nums
            # Otherwise, if we haven't yet hid the middle bound, and the value at our index is 
            # smaller than the right index (i.e. indexed value in left half is smaller than indexed value in right)
            # Take the left value
            if (
                (ri == right) or
                (li != mid and self._working[li] < self._working[ri])
            ):
                nums[i] = self._working[li]
                li += 1
            # We choose this when there are right values remaining OR
            # When the left has hid its end OR
            # When the right value is smaller or equal to the left at our chosen index
            else:
                nums[i] = self._working[ri]
                ri += 1


if __name__ == "__main__":
    nums = [4, 8, 2, 1, 3, 7, 2, -1, 5]
    expected = sorted(nums)
    MergeSort(nums).run()  # tidy up the signature
    assert nums == expected, nums
    print("done")
