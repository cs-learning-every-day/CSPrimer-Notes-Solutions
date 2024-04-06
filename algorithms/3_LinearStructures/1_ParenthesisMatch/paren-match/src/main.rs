/*
* 
* Stacks:
* - If we want to work in the order of things most recently visited - how do we do this?
*
* Problem:
* - Given a string with parenthesis, brackets & braces in them
* - Function should define whether this is valid or not, i.e. whether the parenthesis have been
* closed or not
*
* Tips:
* - Avoid nested loops, you should be able to store information
* - Gotcha: You don't need a stack class
*
*
* Stretch Goal:
* - Figure out where the deleted character is
*
* Understand:
* - We need to use a stack here to identify what the most recent opened parenthesis is
* - If we encounter a closing parenthesis, it should be equivalent to the most recent opened
* parenthesis
*   - Why? B/c otherwise the most recent opened parenthesis wouldn't have a match
*
*
* Plan:
* stack = Stack()
* for character in string:
*   if not is_paren(character):
*       continue
*   if stack.is_empty:
*     stack.push(character)
*     continue
*   if is_closing_parenthesis(character) and is_not_pair(character, stack.pop()):
*       return False
*   stack.push(character)
* return True
*
*
*/

struct Stack<T> {
    stack: Vec<T>,
}

impl<T> Stack<T> {
    fn new() -> Self {
        Stack { stack: Vec::new() }
    }

    fn pop(&mut self) -> Option<T> {
        self.stack.pop()
    }

    fn push(&mut self, item: T) {
        self.stack.push(item)
    }

    fn is_empty(&mut self) -> bool {
        self.stack.len() == 0
    }
}


fn main() {
    let test_case_1 = "()".to_string();
    assert!(paren_match(test_case_1));

    let test_case_1_5 = ")(".to_string();
    assert!(!paren_match(test_case_1_5));

    let test_case_2 = "(()".to_string();
    assert!(!paren_match(test_case_2));

    let test_case_3 = "([())]".to_string();
    assert!(!paren_match(test_case_3));

    let test_case_4 = "abascas)".to_string();
    assert!(!paren_match(test_case_4));

    let test_case_5 = "aba)casf".to_string();
    assert!(!paren_match(test_case_5));

    let test_case_6 = "{([]aaf)$5s[geafd]%^&*}".to_string();
    assert!(paren_match(test_case_6));

    println!("Done");
}

fn paren_match(s: String) -> bool{
    let mut stack: Stack<char> = Stack::new();
    for c in s.chars(){
        if is_opening_paren(c){
            stack.push(c);
        }
        if is_closing_paren(c){
            if stack.is_empty(){
                return false;
            }
            if !is_pair(stack.pop().expect("REASON"), c){
                return false;
            }
        }
    }
    return stack.is_empty();

}

fn is_pair(c1: char, c2: char) -> bool{
    return match (c1, c2) {
        ('[',']') => true,
        ('(',')') => true,
        ('{','}') => true,
        _ => false
    }

}

fn is_opening_paren(c: char) -> bool{
    return match c {
        '[' => true,
        '(' => true,
        '{' => true,
        _ => false
    }
}

fn is_paren(c: char) -> bool{
    return is_opening_paren(c) || is_closing_paren(c);
}

fn is_closing_paren(c: char) -> bool{
    return match c{
        ']' => true,
        ')' => true,
        '}' => true,
        _ => false
    }
}




