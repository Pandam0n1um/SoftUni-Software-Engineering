function diagonalSum(nestedArray) {
    let mainDiagonal = 0;
    let secondaryDiagonal = 0;
    let arrLength = nestedArray.length
    for (let index = 0; index < arrLength; index++) {
        mainDiagonal += Number(nestedArray[index][index]);
        secondaryDiagonal += Number(nestedArray[index][arrLength - index - 1]);
    }
    return `${mainDiagonal} ${secondaryDiagonal}`
}



console.log(diagonalSum([[20, 40],
[10, 60]]));
console.log(diagonalSum([
    [3, 5, 17],
    [-1, 7, 14],
    [1, -8, 89]
]));