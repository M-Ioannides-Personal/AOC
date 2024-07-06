use std::fs;

fn main() {
    let puzzle_input = fs::read_to_string("input.txt")
    .expect("Something has gone wrong with reading the input");

    /*
    Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

    An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

    To what floor do the instructions take Santa?
     */
    let mut floor = 0;
    for instruction in puzzle_input.chars() {
        match instruction {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => {} 
        }
    }
    let solution_1 = floor;

    /*
    Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.
     */
    let mut floor = 0;
    let mut solution_2 = 0;
    for (position, instruction) in puzzle_input.chars().enumerate() {
        match instruction {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => {} 
        }
        if floor < 0 {
            solution_2 = position + 1;
            break;
        }
    }
    println!("Part 1: {}", solution_1);
    println!("Part 2: {}", solution_2);
}