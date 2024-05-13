use std::collections::HashMap;

fn delete_nth(lst: &[u8], n: usize) -> Vec<u8> {
    let mut counts = HashMap::new(); // HashMap to track occurrences of each number
    let mut result = Vec::new();

    for &item in lst {
        let count = counts.entry(item).or_insert(0);
        if *count < n {
            result.push(item);
            *count += 1;
        }
    }

    result
}

fn main() {
    let lst = vec![1,2,3,1,2,1,2,3];
    let n = 2;
    let filtered_lst = delete_nth(&lst, n);
    println!("{:?}", filtered_lst); // Should print [1, 2, 3, 1, 2, 3]

    let lst = vec![20,37,20,21];
    let n = 1;
    let filtered_lst = delete_nth(&lst, n);
    println!("{:?}", filtered_lst); // Should print [20, 37, 21]
}