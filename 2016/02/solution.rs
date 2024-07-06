use std::fs;

fn main() {
    let puzzle_input: Vec<String> = fs::read_to_string("input.txt")
    .expect("Something has gone wrong with reading the input")
    .lines()
    .map(String::from)
    .collect();

    /*
The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.
     */
    
    let mut total_paper: u32 = 0;
    let mut total_ribbon: u32 = 0;
    for line in puzzle_input {
        let mut box_attributes: Vec<u32> = line.split("x").map(|s| s.parse::<u32>().unwrap()).collect();
        box_attributes.sort();
        let length = box_attributes[0];
        let width = box_attributes[1];
        let height = box_attributes[2];
        let this_box = 2 * length * width + 2 * width * height + 2 * height * length;
        let slack = length * width;
        total_paper += this_box + slack;
        let bow = length * width * height;
        let ribbon = 2* (length + width);
        total_ribbon += ribbon + bow;
    }
    let solution_1 = total_paper;
    let solution_2 = total_ribbon;

    println!("Part 1: {}", solution_1);
    println!("Part 1: {}", solution_2);
}