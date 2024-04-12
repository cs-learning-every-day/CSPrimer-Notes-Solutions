/*
* Programming languages are evaluated inside out
* Example:
*   f([[g(), 4], ["foo"])
* - Steps:
*   - g() -> x
*   - [x, 4] -> y
*   - ["foo"] -> z
*   - [x, z) -> SyntaxError!
*
* CalcLang:
* 1 + (1 - 1) -> 1 + 0  -> 1
* - Infix operator
*   - Function operator is between two operators
* - Assume integers
* - You can handle whatever operators you want
* - Stretch Goal
*   - Handling implicit parentheses (i.e order of operations)
*   - Floating points
*
* Objective:
* - Scan the string once
*   - Ideal one character at the time
* - Should be able to evaluate fully parenthesized strings like:
*   - (3 + (3 - 1))
*
* Understand:
* - Auxiliary Problems
*   - (3) -> 3
*       - Enter the paren, add to stack
*       - Add 3 to stack
*       - Once you hit the closing paren, you know its the end of an expression
*         - Pop values off of the stack and save these temporarily until you hit an opening
*         parenthesis 
*         - Evaluate the expression
*   - (3 - 1) -> 2
*       - Enter the paren,a dd to stack
*       - Add 3 to stack
*       - Add - to stack
*       - Add 1 to stack
*       - Hit closing paren, pop everything off the stack until you hit (
*           - Evaluate the expression
*   - (3 - (3 - 3) -> SyntaxError
*       - You evaluate 3 - 3, leaving (3 - 3
*       - This cannot be evaluated, so throw error
* Plan:
* - Create a stack 
* - For each character in the string:
*    if stack is empty and character is not ( -> raise Error
*    if character is not ): 
*      add to stack
*    else:
*      expression_stack = new_stack
*      while new_stack.peek() != '(':
*         expression_stack.push(stack.pop())
*      operand_2 = new_stack.pop()
*      operator = new_stack.pop()
*      operand_1 = new_stack.pop()
*      if operator == '+':
*        stack.push(operand_1 + operand_2)
*      else if operator == '-':
*        stack.push(operand_1 - operand_2)
*      else:
*        raise InvalidOperatorError
*      stack.push(character)
* - if not stack.length == 3: # b/c we expect some expression (x) at the end
*   raise InvalidComputationError
* - open_paren = stack.pop()
* - return stack.pop().as_int
*      
*
*     
*
*
*/
use std::collections::HashMap;

fn main() {
    // VALID TEST CASES
    let valid_cases: HashMap<&str, u32> = HashMap::from([
        ("(3+1)", 4), 
        ("(3-1)", 2), 
        ("((1 - (1 - 1))", 1), 
        ("(3+(3-1))", 5),
        ("(4+(3+(3-1)))", 9)
    ]);

    for (expression, expected_result) in valid_cases.into_iter(){
        println!("Expression: {}", expression);
        println!("Expected Result: {}", expected_result);
        let result = calculator(expression);
        println!("Result: {}", result);
        assert!(result == expected_result); 
        println!("Passed");
    }

    println!("Done");
}

fn calculator(expression: &str) -> u32{
    let mut stack: Vec<char> = Vec::new();
    for c in expression.chars(){
       println!("Stack: {:?}", stack);
        if c != '(' &&  c != ')' && c != ' '{
            stack.push(c);
            continue;
        }
        if c == ')'{
            let operand_1 = stack.pop().unwrap();
            let operator = stack.pop().unwrap();
            let operand_2 = stack.pop().unwrap();
            if operator == '+'{
                stack.push(
                    char::from_digit(
                        operand_1.to_digit(10).unwrap() + operand_2.to_digit(10).unwrap(),
                        10
                    ).unwrap()
                );
            }
            else if operator == '-' {
                stack.push(
                    char::from_digit(
                        operand_2.to_digit(10).unwrap() - operand_1.to_digit(10).unwrap(),
                        10
                    ).unwrap()
                );
            }
            else {
                panic!("Invalid Operator: {}", operator);
            }
        }
    }

    return stack.pop().unwrap().to_digit(10).unwrap();


}
