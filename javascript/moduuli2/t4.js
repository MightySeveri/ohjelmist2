<!-- löysin ohjeistuksen tähän stackoverflowsta -->
function main() {
    const numbers = [];
    let input;

    do {
        input = prompt("Enter a number (0 to stop):");
        let num = parseFloat(input);

        if (!isNaN(num)) {
            if (num !== 0) {
                numbers.push(num);
            }
        } else {
            alert("Please enter a valid number.");
        }

    } while (input !== "0");

    numbers.sort((a, b) => b - a);

    console.log("Numbers from largest to smallest:");
    numbers.forEach(num => console.log(num));
}

main();
