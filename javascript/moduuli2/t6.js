function findTargetNumber() {
    const target = 6;
    let attempts = 0;
    let number;

    while (true) {
        number = Math.floor(Math.random() * 6) + 1;
        attempts++;
        console.log(`Arvottu numero: ${number}`);

        if (number === target) {
            console.log(`Saatiin oikea numero ${target} ${attempts} yrityksen jälkeen!`);
            break;
        }
    }
}

findTargetNumber();
