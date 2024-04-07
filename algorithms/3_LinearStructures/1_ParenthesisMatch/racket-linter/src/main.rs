use std::fs;

/*
* Understand:
* - We want to figure out whether there is an unmatched parenthesis in the file (mini-linter)
* - If there is some unmatched parenthesis, we want to be able to tell the line and column of the
* issue
* - We don't care about non-parenthesis characters
*   - As soon as we meet a paren that doesn't match up with the state of our stack, we know to
*   return False
* - As we iterate over the file three things are important:
*   - Have we hit a paren that is incorrectly placed?
*       - If yes, then we should return 
*   - What row are we in?
*       - We can keep track of this outside of the matching code by reading line by line
*   - What position in the row are we in?
*       - For this we should update the paren match function to return both the number of the
*       character and whether it is a false match
*
*
* Plan:
* - Read the file
* - Split the file according to new line character
* - For each line in the file:
*   - For each index, character in the line:
*       - If the character is an opening parenthesis:
*           - Push it to the stack
*       - if the character is a closing parenthesis:
*           - If the stack is empty or the last element of the stack is not a match:
*               - print("NO MATCH: <row_number>, <row_index>)
*               - return
*/


fn main() {
    let contents = fs::read_to_string("stretch.rkt")
        .expect("Should have been able to read the file");
    let mut stack: Vec<char> = Vec::new();
    let rows = contents.split('\n');
    for (row_num, row) in rows.enumerate(){
        for (index, c) in row.chars().enumerate(){
            if is_opening_paren(c){
                stack.push(c);
            }
            if is_closing_paren(c){
                if stack.is_empty() || !is_pair(stack.pop().unwrap(), c){
                    println!("Invalid Syntax:\nLine: {}\nIndex: {}.\nCharacter: {}", row_num, index+1, c);
                    return;
                }
            }
        }
    }
    if !stack.is_empty(){
        println!("Invalid Syntax.\nYou are missing a closing bracket."); 
    } else{
        println!("Done");
    }
}

fn is_pair(l: char, r: char) -> bool{
    matches!((l, r), ('[',']') | ('(',')') | ('{','}'))
}

fn is_opening_paren(c: char) -> bool {
    matches!(c, '[' | '(' | '{')
}

fn is_closing_paren(c: char) -> bool {
    matches!(c, ']' | ')' | '}')
}

