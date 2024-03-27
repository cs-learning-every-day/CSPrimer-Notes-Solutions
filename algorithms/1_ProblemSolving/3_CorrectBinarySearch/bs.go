package main
/*
- Implement BS without bugs
[ -5, -3, 0, 4, 20]

n = 4 -> 3
n = 5 -> -1 / False


Understand the problem:
- Given a list of values, search for the index at which a given value is contained, if at all
    - Use binary search, which assumes a sorted list and divides the list into two and then searches
      the subset
- Using Invariants
    - Assert that particular things are true during your algorithm to be sure it'll work

Plan:
- Invariants:
    - Assert that lower bound is less than or equal to upper bound
    - 

*/
import "fmt"

func main(){
    test := []int{1,2,3,4}
    if binarySearch(test, 2, 4) != 1{
        fmt.Println("FAILED!")
    }
    fmt.Println("PASSED!")



}

func binarySearch(nums []int, val int, length int) int {
    return binarySearchAttempt(nums, val, length)
}

func binarySearchAttempt(nums []int, val int, length int) int {
    l := 0
    r := length 
    if (l >= r){
        panic("FAILED b/c L >= R")
    }
    m := r - l / 2
    if (nums[m] == val){
        return 1
    }
    if (nums[m] > val){
        return binarySearch(nums[:m], val, r - m)
    }
    if (nums[m] < val){
        return binarySearch(nums[m+1:], val, m - l)
    }
    panic("FAILED")
}


func binarySearchSolution(){
    /*
    let lo, hi be 0 and len(nums)... then we know, if n
    is in nums, then it must be in [lo,hi)
    loop:
        if range is empty (what does this mean in terms of lo/hi)
            break
        mid = (lo + hi) / 2 # stilli n range [lo, hi)
        x = nums[mid]
        if x == n:
            return mid
        if n < x:
            hi = mid # Exclusive limit
        if n > x:
            lo = mid + 1 # You can also set to mid, that'll work, but its faster to do mid + 1
            # B/c its inclusive, we don't need to check mid again
    return None

    */


}
