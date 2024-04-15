"""
1. basic mergesort with slicing/copying as needed
2. refactor to use only N additional space, no extra list copies

"""

def mergesort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    return merge(mergesort(nums[:mid]), mergesort(nums[mid:]))


def merge(xs: list[int], ys: list[int]) -> list[int]:
    res = []
    xi, yi = 0, 0
    while True:
        if xi == len(xs):
            return res + ys[yi:]
        if yi == len(ys):
            return res + xs[xi:]
        x, y = xs[xi], ys[yi]
        if x < y:
            res.append(x)
            xi += 1
        else:
            res.append(y)
            yi += 1



if __name__ == '__main__':
    nums = [4, 8, 2, 1, 3, 7, 2, -1, 5]
    expected = sorted(nums)
    actual = mergesort(nums)
    assert actual == expected, actual
    print('done')

