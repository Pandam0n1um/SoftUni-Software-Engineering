function arrayNthElement(array, value) {
    const result = array.filter((_, index) => index % value==0);
    return result
}


console.log(arrayNthElement(['5',
    '20',
    '31',
    '4',
    '20'],
    2))
console.log(arrayNthElement(['dsa',
    'asd',
    'test',
    'tset'],
    2))
console.log(arrayNthElement(['1',
    '2',
    '3',
    '4',
    '5'],
    6))