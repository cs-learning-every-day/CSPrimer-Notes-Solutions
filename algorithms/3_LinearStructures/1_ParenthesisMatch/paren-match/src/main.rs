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

fn main() {
    let test_case_1 = "()".to_string();
    assert!(paren_match(&test_case_1));

    let test_case_1_5 = ")(".to_string();
    assert!(!paren_match(&test_case_1_5));

    let test_case_2 = "(()".to_string();
    assert!(!paren_match(&test_case_2));

    let test_case_3 = "([())]".to_string();
    assert!(!paren_match(&test_case_3));

    let test_case_4 = "abascas)".to_string();
    assert!(!paren_match(&test_case_4));

    let test_case_5 = "aba)casf".to_string();
    assert!(!paren_match(&test_case_5));

    let test_case_6 = "{([]aaf)$5s[geafd]%^&*}".to_string();
    assert!(paren_match(&test_case_6));

    println!("Done");
}

fn paren_match(s: &str) -> bool{
    let mut stack: Vec<char> = Vec::new();
    for c in s.chars(){
        if is_opening_paren(c){
            stack.push(c);
        }
        if is_closing_paren(c){
            if stack.is_empty() || !is_pair(stack.pop().unwrap(), c){
                return false;
            }
        }
    }
    stack.is_empty()

}

fn is_pair(c1: char, c2: char) -> bool{
    matches!((c1, c2), ('[',']') | ('(',')') | ('{','}'))
}

fn is_opening_paren(c: char) -> bool {
    matches!(c, '[' | '(' | '{')
}

fn is_closing_paren(c: char) -> bool {
    matches!(c, ']' | ')' | '}')
}


