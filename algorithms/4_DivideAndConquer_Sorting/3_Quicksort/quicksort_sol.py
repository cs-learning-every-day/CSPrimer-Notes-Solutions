
def qsort(nums: list[int], lo, hi) -> None:
    # sort nums from [lo, hi] incusive
    # partition using Lomuto scheme
    # recurse on lower and higher side

    m = lo
    t = nums[lo]
    for i in range(lo+1, hi+1):
        if t < nums[i]:
            m += 1
            nums[i], nums[m] = nums[m], nums[i]
    nums[lo], nums[m] = nums[m], nums[lo]
    qsort(nums, lo, m - 1)
    qsort(nums, m + 1, hi)


if __name__ == '__main__':
    nums = [5, 3, 8, 6, 2, 7, 1, 4]
    qsort(nums, 0, len(nums) - 1)
    assert nums == sorted(nums)
