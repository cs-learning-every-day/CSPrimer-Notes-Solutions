/*
* Thinking in terms of complexity classes gives you an idea of room for improvement
* You can also have improvement within complexity class
* Intuititions: You can't get better than linear time when you're dealing with something that looks
* at all elements of an array
* If you've got a log(n) case, you'll need to rely on a trick to get it down to constant time
* Same for nlogn -> n
*
* Find the sum of all numbers that are divisible by either 3 or 5. Count cases where they are
* divisible by 3 and 5 just once
* For n=1,...,15:
*   - 3,5,6,9,10,12,15
*
* Best possible fizzbuzz approach is linear time - you need to print fizz buzz each time
*
* Is there a log n approach to this? Perhaps Divide and Conquer
* Is there a constant time approach to this? Yes
*   - There must be a relation between them
*/


fn main() {
    let res1 = fizzbuzz(15);
    println!("{}", res1);
    assert!(res1 == 60);
    let res2 = fizzbuzz(10);
    println!("{}", res2);
    assert!(res2 == 33);
    println!("OK");

}


fn fizzbuzz(n: i32) -> i32{
    return fizzbuzz_math(n);
}

fn fizzbuzz_linear(n: i32) -> i32{
    /*
    * Plan:
    * acc = 0
    * for each x_i=1,:,..n:
    *   if x %3 == 0 or x% 5 == 0:
    *     acc += x
    * return acc
    */
    let mut acc = 0;
    for i in 1..n+1{
        if (i % 3 == 0) || (i % 5 == 0){
            acc += i;
        }
    }
    return acc;
}


fn fizzbuzz_sublinear(n: i32) -> i32{
    /*
    * Count the sum of times 3 fits into n + the times 5 fits into n, minus the times 15 fits
* into n
    * Case 15:
    *   - Sum of divisible by 3 -> 45
    *   - Sum of divisible by 5 -> 30
    *   - Sum of divisible by 15 -> 15
    * Plan:
    * acc = 0;
    * - For i in {1,n // 15+1}:
    *    acc += 15 * n;
    * - For i in {1, n // 5};
    *    res1 = 5 * i;
    *    if res % 15 != 0;
    *       acc +=  res1
    * - For i in {1, n // 3};
    *    res2 = 3 * i;
    *    if res % 15 != 0;
    *       acc += res2;
    */
    let mut acc = 0;
    let divisible_by_15: i32 = n / 15;
    for i in 1..divisible_by_15+1 {
        acc += 15 * i;
    }
    let divisible_by_3: i32 = n / 3;
    for i in 1..divisible_by_3+1 {
        let res1 = 3 * i;
        if res1 % 15 != 0 {
            acc += res1;
        }
    }
    let divisible_by_5: i32 = n / 5;
    for i in 1..divisible_by_5+1 {
        let res2 = 5 * i;
        if res2 % 15 != 0 {
            acc += res2;
        }
    }
    return acc;
}


fn fizzbuzz_const(n: i32) -> i32{
    /*
    * Understand:
    * # of times 3 comes up in 15 -> 5
    * # of times 5 comes up in 15 -> 3
    * # of times 15 comes up in 15 -> 1
    * # of times they all come up -> 7
    *
    * You can think of it being:
    *   how many times does 15 come into it? * 7
    *   + how many times does 3 go into remainder
    *   + how many times does 5 go into remainder
    *
    * Plan:
    *   res_15 = n % 15;
    *   return 7 * n / 15 + res_15 % 3 + res_15 % 5;
    *
    * Examples:
    *   15: 7 * 15 / 15 + 0 ^% 3 + 0 % 5 -> 7
    *   20: 7 * 20 / 15 + 5 % 3 + 5 % 5 
    *       7 + 1 + 1 -> 9
    */
    let res_15 = n % 15;

    let div_3 = res_15 / 3;
    let mut total_3 = 0;
    match div_3 {
        0 => total_3 = 0,
        1 => total_3 += 3,
        2 => total_3 += 9,
        3 => total_3 += 18,
        4 => total_3 += 30,
        _ => println!("ERROR: {}", div_3)
    }
    let mut total_5 = 0;    
    let div_5 = res_15 / 5;
    match div_5 {
        0 => total_5 = 0,
        1 => total_5 += 5,
        2 => total_5 += 15,
        _ => println!("ERROR")
    }
    return 60*(n / 15) + total_3 + total_5;
}

fn fizzbuzz_math(n: i32) -> i32{
    let sum_15 = sum_of_arithmetic_sequence(0, 15, (n / 15) + 1);
    let sum_5 = sum_of_arithmetic_sequence(0, 5, (n / 5) + 1);
    let sum_3 = sum_of_arithmetic_sequence(0, 3, (n / 3) + 1);
    return sum_3 + sum_5 - sum_15;

}


fn sum_of_arithmetic_sequence(a: i32, d: i32, n: i32) -> i32 {
    return (n *(2*a + (n - 1) * d)) / 2

}


