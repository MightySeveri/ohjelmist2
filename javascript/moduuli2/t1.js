const numbers = [];
numbers[0] = prompt('syötä numero')
numbers[1] = prompt('syötä numero')
numbers[2] = prompt('syötä numero')
numbers[3] = prompt('syötä numero')
numbers[4] = prompt('syötä numero')
let reversedNumbers = numbers.map((e, i, a)=> a[(a.length -1) -i])
alert(numbers);