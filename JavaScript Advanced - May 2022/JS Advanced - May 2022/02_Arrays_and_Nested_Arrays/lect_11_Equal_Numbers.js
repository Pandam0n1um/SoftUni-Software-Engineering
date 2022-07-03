function pairFinder(nestedArray) {
    let pairs = 0;
    let rows = nestedArray.length;
    let cols = nestedArray[0].length;
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (j<cols-1 && nestedArray[i][j] == nestedArray[i][j + 1]) {
                pairs += 1;
            }
            if (i<rows-1 && nestedArray[i][j] == nestedArray[i + 1][j]) {
                pairs += 1
            }
        }
    }
    return pairs
}



console.log(pairFinder([
    ['2', '3', '4', '7', '0'],
    ['4', '0', '5', '3', '4'],
    ['2', '3', '5', '4', '2'],
    ['9', '8', '7', '5', '4']]));

console.log(pairFinder([
    ['test', 'yes', 'yo', 'ho'],
    ['well', 'done', 'yo', '6'],
    ['not', 'done', 'yet', '5']]));

console.log(pairFinder(
    [2, 2, 5, 7, 4],
    [4, 0, 5, 3, 4],
    [2, 5, 5, 4, 2]));