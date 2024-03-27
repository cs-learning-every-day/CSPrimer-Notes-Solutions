/*
* Chocolate Bar
* - How would you given M x N chocolate bar into 1 x 1 pieces?
*
* Understand the problem
* What are the inputs? 
*   - Rectangle size
*   - Divisions are units
* What are the outputs?
*   - How many breaks are you going to make
*   - Minimum numbers of steps
* - Thinking
*   - Chocolate bar is composed of many smaller chocolate bars  
*   - Therefore a chocolate bar that has been split will create 2 new chocolate bars, of size
*   (m // 2,n) or (m, n//2)
*   - If we want to preserve unit pieces, we can't break a chocolate bar across the dimension where
*   x % 2 != 0
*       - In this case, we 
*   
* Consider a 4 x 4 chocolate bar
* - What is the worst way to break it up?
*   - 3 breaks to get 4 1 x 4 bars
*   - 3 breaks per each bar -> 12 breaks
*   - Total 15 breaks
* - What is the best way?
*   - 1 Break -> 2 2 x 4
*   - 2 Breaks -> 4 2 x 2
*   - 4 breaks -> 8 2 x 1
*   - 8 breaks -> 16 1 x 1
*   - Total 15 Breaks
* - Seems that for chocolate bars m x n there is no best way
*   - Its just (m x m) - 1
* - What about 4 x 5?
* - Worst way?
*   - 4 breaks to get 5 1 x 4
*   - 3 breaks per each bar -> 15 breaks
*   - 19 breaks
* - Best Way?
*   - 3 -> 4 1x5
*   - 2 -> 4 2x2
*   - 4 -> 
* 
* For some m & n:
*   Check if it is a base case (1x1, 2x1 or 1x2)
*   Else, break the chocolate bar into two pieces, choosing the longest side
*
* 
*/
fn main() {
    let test1: i32 = number_of_breaks(1,1);
    assert!(test1 == 0);
    println!("{}", test1);
    let test2: i32 = number_of_breaks(5,4);
    println!("{}", test2);
    let test3: i32 = number_of_breaks(4,4);
    println!("{}", test3);

}


fn number_of_breaks(m: i32, n: i32) -> i32 {
    return number_of_breaks_sub(m,n)
}


fn number_of_breaks_sub(m: i32, n: i32) -> i32 {
    if m == 1{
        return n-1;
    }
    return 1 + number_of_breaks(m / 2, n) + number_of_breaks(m - m/2, n);
}
