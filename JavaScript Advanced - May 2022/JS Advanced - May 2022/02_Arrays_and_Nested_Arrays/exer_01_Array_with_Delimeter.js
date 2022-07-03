function arrayDelimeter(array, string) {
    return array.join(string);
}

console.log(arrayDelimeter(
    ['One',
        'Two',
        'Three',
        'Four',
        'Five'],
    '-'));
console.log(arrayDelimeter([
    'How about no?',
    'I',
    'will',
    'not',
    'do',
    'it!'],
    '_'
));