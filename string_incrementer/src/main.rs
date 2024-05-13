/*
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100
*/

struct Word {
    letters: String,
    numbers: String,
}

impl Word {
    // Function to split the input string into a Word instance
    fn from_string(s: &str) -> Word {
        let mut letters = String::new();
        let mut numbers = String::new();
        let mut is_number = false;

        for c in s.chars().rev() {
            if c.is_digit(10) {
                numbers.push(c);
                is_number = true;
            } else if is_number {
                break;
            } else {
                letters.push(c);
            }
        }

        // Reverse the letters and numbers to maintain original order
        Word {
            letters: letters.chars().rev().collect(),
            numbers: numbers.chars().rev().collect(),
        }
    }

    // Function to increment the numeric part of the Word
    fn increment(&mut self) {
        if !self.numbers.is_empty() {
            let mut num: i32 = self.numbers.parse().unwrap();
            num += 1;
            self.numbers = num.to_string();
        } else {
            self.numbers = "1".to_string();
        }
    }

    fn pad_zeros(&mut self, total_digits: usize) {
        let num_digits = self.numbers.len();
        if num_digits < total_digits {
            let padding = total_digits - num_digits;
            let zeros = "0".repeat(padding);
            self.numbers = format!("{}{}", zeros, self.numbers);
        }
    }

    // Function to combine the letters and numbers parts into a single string
    fn to_string(&self) -> String {
        format!("{}{}", self.letters, self.numbers)
    }
}

fn main() {
    let tests = vec![
        "foo", "foobar23", "foo0042", "foo9", "foo099",
    ];

    for test in tests {
        let mut word = Word::from_string(test);
        word.increment();
        println!("{} -> {}", test, word.to_string());
    }
}