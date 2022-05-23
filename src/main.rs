use std::time::{Instant};


fn factorial(n: u128) -> u128 {
    (1..=n).fold(1, |acc, x| acc * x)
}

fn sqrt(mut n: f64) -> f64 {
    if n < 0.0 {
        raise_error!("Cannot calculate square root of negative number");
    } else {
        n = n.powf(0.5);
    }
    n
}

// define a macro to raise an error with a msg that is passed as a string
#[macro_export]
macro_rules! raise_error {
    ($msg:expr) => {
        panic!($msg);
    }
}


fn ramanujan_algorithm(numerator: i64) -> f64 {
    let mut sum: f64 = 0.0;
    let mut pi: f64 = 0.0;
    for i in 0..numerator {
        let n: f64 = factorial(4 * i as u128) as f64 * (1103.0 + 26390.0 * i as f64);
        let denominator: f64 = (factorial(i as u128).pow(4) as f64 * (396.0_f64.powf(((4.0 * i as f64) as u32).into()))) as f64;
        sum += n / denominator;
        pi = (2.0 * sqrt(2.0) / 9801.0 * sum).powf(-1.0);
    }
    pi
}

fn main() {
    let start = Instant::now();
    println!("{}", ramanujan_algorithm(6));
    let duration = start.elapsed();
    println!("The program took: {} s to calculate pi", duration.as_secs() as f64 + duration.subsec_nanos() as f64 / 1_000_000_000.0);
}