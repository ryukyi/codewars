/*
Create a function taking a positive integer 
between 1 and 3999 (both included) as its parameter 
and returning a string containing the Roman Numeral 
representation of that integer.

Modern Roman numerals are written by expressing each digit 
separately starting with the leftmost digit and skipping any 
digit with a value of zero. There cannot be more than 3 identical symbols in a row.

In Roman numerals:

1990 is rendered: 1000=M + 900=CM + 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII.
1666 uses each Roman symbol in descending order: MDCLXVI.
Example:

   1 -->       "I"
1000 -->       "M"
1666 --> "MDCLXVI"
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
*/

#[derive(PartialEq, PartialOrd)]
enum RomanNumerals {
    I = 1,
    V = 5,
    X = 10,
    L = 50,
    C = 100,
    D = 500,
    M = 1000,
}

// Function to convert a Roman numeral character to its corresponding enum variant
fn char_to_roman(c: char) -> Option<RomanNumerals> {
    match c {
        'I' => Some(RomanNumerals::I),
        'V' => Some(RomanNumerals::V),
        'X' => Some(RomanNumerals::X),
        'L' => Some(RomanNumerals::L),
        'C' => Some(RomanNumerals::C),
        'D' => Some(RomanNumerals::D),
        'M' => Some(RomanNumerals::M),
        _ => None,
    }
}

// Function to convert a Roman numeral string to an integer
fn roman_to_int(s: &str) -> i32 {
    let mut total = 0;
    let mut prev_value = 0;

    for c in s.chars().rev() {
        if let Some(roman) = char_to_roman(c) {
            let value_i32 = roman as i32;

            if value_i32 >= prev_value {
                total += value_i32;
            } else {
                total -= value_i32;
            }

            prev_value = value_i32;
        } else {
            panic!("Invalid character");
        }
    }

    total
}

// Function to convert an integer to a Roman numeral string
fn num_as_roman(num: i32) -> String {
    let mut result = String::new();
    let mut value = num;

    let values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ];

    for &(val, roman) in values.iter() {
        while value >= val {
            result.push_str(roman);
            value -= val;
        }
    }

    result
}

fn main() {
    let s = "MDCLXVI";
    let num = roman_to_int(s);
    println!("{}", num);
}
