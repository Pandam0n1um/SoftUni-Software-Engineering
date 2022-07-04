function arrayRotate(array, value) {
    for (let rotation = 0; rotation < value; rotation++) {
        array.unshift(array.pop());
    }
    return array.join(' ')
}

console.log(arrayRotate(['1',
    '2',
    '3',
    '4'],
    2));
console.log(arrayRotate(['Banana',
    'Orange',
    'Coconut',
    'Apple'],
    15
));