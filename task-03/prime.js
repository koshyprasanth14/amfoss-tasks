function isPrime(num) {
    if (num <= 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;
}

const n = parseInt(prompt("Enter a number:"));

console.log(`Prime numbers up to ${n} are:`);
for (let i = 2; i <= n; i++) {
    if (isPrime(i)) {
        console.log(i);
    }
}
