use std::io;

fn is_prime(num: u32) -> bool {
    if num <= 1 {
        return false;
    }
    for i in 2..=(num as f64).sqrt() as u32 {
        if num % i == 0 {
            return false;
        }
    }
    true
}

fn main() {
    let mut n = String::new();
    println!("Enter a number: ");
    io::stdin().read_line(&mut n).expect("Failed to read line");
    let n: u32 = n.trim().parse().expect("Invalid input");

    println!("Prime numbers up to {} are:", n);
    for i in 2..=n {
        if is_prime(i) {
            print!("{} ", i);
        }
    }
}
