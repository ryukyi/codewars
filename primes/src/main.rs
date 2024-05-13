/*To efficiently determine if a number is prime, you can use the following approach, 
    which is based on the fact that a prime number is only divisible by 1 and itself.

This method avoids unnecessary checks:
1. Handle Base Cases: Check if the number is less than 2, 
    which are not prime by definition.
2. Check for Even Number: After checking for 2, 
    which is the only even prime number, any other even number can be immediately classified as not prime.
3. Use Square Root Rule: For a number n, if it is divisible by any number less than or equal to the square root of n, then it is not prime. This significantly reduces the number of checks needed. 
    If n is not divisible by any number up to its square root, it is prime.
*/

fn is_prime(i: i64) -> bool {
    if i < 2 {
        return false;
    }
    if i == 2 {
        return true;
    }
    if i % 2 == 0 {
        return false;
    }
    let sqrt = (i as f64).sqrt() as i64;
    for num in 3..=sqrt {
        if i % num == 0 {
            return false;
        }
    }
    true
}

fn main() {
    let p = is_prime(60);
    println!("Hello, world! {}", p);
}
