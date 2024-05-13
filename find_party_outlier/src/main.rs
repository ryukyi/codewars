/*
You are given an array (which will have a length of at least 3, but could be very large)
containing integers.
The array is either entirely comprised of odd integers or entirely
comprised of even integers except for a single integer N. Write a method that
takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number) */

// Check first 2 values, 
    // if both even, iterate until odd
    // if both odd, iterate until even
    // if even and odd, check next and revert back

fn find_outlier(values: &[i32]) -> i32 {
    // Collect the first three elements to determine the majority
    let counts = values.iter().take(3).fold((0, 0), |(even, odd), &x| {
        if x % 2 == 0 { (even + 1, odd) } else { (even, odd + 1) }
    });

    let find_even = counts.1 > counts.0;
    // Use find to return the first element that satisfies the condition
    *values.iter().find(|&&x| find_even == (x % 2 == 0)).unwrap()
}
    
fn main() {
    let example1 = [2, 4, 0, 100, 4, 11, 2602, 36];
    let example2 = [160, 3, 1719, 19, 11, 13, -21];
    println!("Outlier in example1: {}", find_outlier(&example1));
    println!("Outlier in example2: {}", find_outlier(&example2));
}