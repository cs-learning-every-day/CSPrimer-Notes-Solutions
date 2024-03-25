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
    1:  "I",
    2:  "II",
    3:  "III",
    4:  "IV",
    5:  "V",
    6:  "VI",
    7:  "VII",
    8:  "VIII",
    9:  "IX",
    10:  "X",
    20:  "XX",
    30:  "XXX",
    40:  "XL",
    50:  "L",
    60:  "LX",
    70:  "LXX",
    80:  "LXXX",
    90:  "XC",
    100:  "C",
    200:  "CC",
    300:  "CCC",
    400:  "CD",
    500:  "D",
    600:  "DC",
    700:  "DCC",
    800:  "DCCC",
    900:  "CM",
    1000:  "M",
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


func roman(num int) string {
    // Check how many Ms    
    mCount := num / 1000
    originalString := ""
    if (mCount != 0){
        originalString = originalString + strings.Repeat("M", mCount)
        num = num - mCount * 1000
    } 

    // Getting decimal places
    val := 1
    iD := num / val
    decimalPlaces := val
    for iD > 0 {
        val = val * 10
        iD = num / val
        if iD > 0 {
            decimalPlaces = decimalPlaces + 1
        }
    }
    decimalPlaces = decimalPlaces - 1
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
