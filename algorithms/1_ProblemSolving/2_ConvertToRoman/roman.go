/*
In this problem, you will write a short function to convert an integer to its Roman numeral form. 
If you start coding without a plan, it's likely that you will end up with an unnecessarily complicated approach!


The Problem:
- Input
    - Integer
- Output:
    - String
- Parameters
    - Roman Numerals
        - M -> 1000
        - D -> 500
        - C -> 100
        - L -> 50
        - X -> 10
        - V -> 5
        - I -> 1

Plan:
- For each decimal digit, highest to lowest, convert to Roman
- Thousands:
    - X // 1000 = y
    - y * M
- Hundreds:
    - use a map

Plan:
- 
*/


package main

import (
    "fmt"
    "strconv"
    "math"
    "strings"
)

var myMap = map[int]string{
    1000:  "M",
    900:  "CM",
    800:  "DCCC",
    700:  "DCC",
    600:  "DC",
    500:  "D",
    400:  "CD",
    300:  "CCC",
    200:  "CC",
    100:  "C",
    90:  "XC",
    80:  "LXXX",
    70:  "LXX",
    60:  "LX",
    50:  "L",
    40:  "XL",
    30:  "XXX",
    20:  "XX",
    10:  "X",
    9:  "IX",
    8:  "VIII",
    7:  "VII",
    6:  "VI",
    5:  "V",
    4:  "IV",
    3:  "III",
    2:  "II",
    1:  "I",
}


var answers = map[int]string{
    39: "XXXIX",
    246: "CCXLVI",
    789: "DCCLXXXIX",
    2421: "MMCDXXI",
    160: "CLX",
    207: "CCVII",
    1009: "MIX",
    1066: "MLXVI",
}


func main() {
    for k,v := range answers {
        res := roman(k)
        if res != v {
            fmt.Println(res)
            fmt.Println(v)
            panic("FAILED!")
        }
    }
    fmt.Println("Done!")
}

func getPow(base int, pow int) int {
    return int(math.Pow(float64(base), float64(pow)))
}


func romanAttempt(num int) string {
    // check how many ms    
    mcount := num / 1000
    originalString := ""
    if (mcount != 0){
        originalString = originalString + strings.Repeat("M", mcount)
        num = num - mcount * 1000
    } 

    // Getting decimal places
    decimalPlaces := 0
    for num / getPow(10, decimalPlaces + 1) > 0 {
        decimalPlaces = decimalPlaces + 1
    }
    numStr := strconv.Itoa(num)
    for _, char := range numStr {
        x, err := strconv.Atoi(string(char))
        if err != nil {
            fmt.Println("Error:", err)
            return "error"
        }
        y := x * int(math.Pow(10, float64(decimalPlaces)))
        decimalPlaces = decimalPlaces - 1
        originalString = originalString + myMap[y]
    }

    return originalString
}

// RomanNumeral struct represents a Roman numeral with its integer value and string representation
type RomanNumeral struct {
    Value  int
    Symbol string
}


func roman(num int) string{
    return romanSolution(num)
}


func romanSolution(num int) string{
    /*
    Problem:
    f(n int) -> roman numeral string
    - Is it solvable? Yes

    Plan:
    - Solving the auxiliary problem of ignoring the subtractive notation cases
        - 32 -> XXXII
    - Solving the problem recursively:
        - Solving f(32) = f(10) + f(22) = f(10) + f(10) + f(12) = f(10) + f(10) + f(2)
    - How do we extend to the subtractive notation cases?
        - f(39) = f(10) + f(29) = f(10) + f(20) + f(9) = f(10) + f(10) + f(10) + f(9)
        - f(789) = f(700) + f(89) = f(700) + f(80) + f(9) = f(500) f(200) + f(50) f(30) + f(9) = D CC L XXX IX
    */
    // List of Roman numerals and their integer values
    var RomanNumerals = []RomanNumeral{
        {1000, "M"},
        {900, "CM"},
        {500, "D"},
        {400, "CD"},
        {100, "C"},
        {90, "XC"},
        {50, "L"},
        {40, "XL"},
        {10, "X"},
        {9, "IX"},
        {5, "V"},
        {4, "IV"},
        {1, "I"},
    }

    /*
    ITERATIVE
    string := ""
    for _, numeral := range RomanNumerals {
         for (num - numeral.Value >= 0) {
            num = num -  numeral.Value
            string = string + numeral.Symbol
        }
    }
    */
    // RECURSIVE
    for _, numeral := range RomanNumerals {
        if numeral.Value <= num {
            return numeral.Symbol + romanSolution(num-numeral.Value)
        }

    }
    return ""


}


