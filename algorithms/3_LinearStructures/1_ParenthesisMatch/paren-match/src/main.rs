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
    // VALID
    let valid_cases: Vec<&str> = vec![
        "()", "()[]", "([{}])"
    ];
    for case in valid_cases{
        assert!(paren_match(case));
    }

    // INVALID - The minimal cases needed to be invalid
    let invalid_cases: Vec<&str> = vec![
        "(",   // left imbalanced
        ")",   // right imbalanced
        "(()", // too many opening brackets
        "([)]" // incorrect nesting
    ];
    for case in invalid_cases{
        assert!(!paren_match(case));
    }
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


