const answer = confirm('Should I calculate the square root?');

if (answer) {
    let num = Number(prompt('Syötä numero'));

    if (num < 0) {
        alert('Neliöjuurta ei voi laskea negatiiviselle luvulle.');
    } else {
        let sqr = Math.sqrt(num);
        alert(sqr);
    }
} else {
    alert('The square root will not be calculated.');
}
