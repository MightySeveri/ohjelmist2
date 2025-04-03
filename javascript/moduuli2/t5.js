function main() {
    const numbers = [];
    let input;
    let previousNum = null;

    while (true) {
        input = prompt("Enter a number:");
        let num = parseFloat(input);

        if (isNaN(num)) {
            alert("Please enter a valid number.");
            continue;
        }

        numbers.push(num);

        if (num === previousNum) {
            numbers.pop();
            numbers.pop();
            break;
        }

        previousNum = num;
    }

    numbers.sort((a, b) => b - a);

    console.log("Numbers from largest to smallest:");
    numbers.forEach(num => console.log(num));
}

main();
