/*
Count the number of Duplicates
Write a function that will return the count of 
distinct case-insensitive alphabetic characters and numeric digits 
that occur more than once in the input string. 
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
*/

use std::collections::HashMap;

struct Duplicates {
    letters: HashMap<char, i32>
}

impl Duplicates {
    fn new(str: &str) -> Duplicates {
        let mut letters: HashMap<char, i32> = HashMap::new();
        for ch in str.chars() {
            let lower_ch = ch.to_ascii_lowercase();
            letters.entry(lower_ch).and_modify(|val| *val += 1).or_insert(0);
        }
        Duplicates {
            letters
        }
    }

    fn count_non_zeros(&self) -> usize {
        self.letters.values().filter(|&v| *v > 0).count()
    }
}

fn count_duplicates(text: &str) -> u32 {
    Duplicates::new(text).count_non_zeros().try_into().unwrap()
}

fn main() {
    let test = count_duplicates("aabbcde");
    println!("{:?}", test)
}