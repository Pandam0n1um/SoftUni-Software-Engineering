function biggestElemen(nestedArray) {
    const maxValue = Math.max(...[].concat(...nestedArray));
    return maxValue;
}


console.log(biggestElemen(
    [[3, 5, 7, 12],
    [-1, 4, 33, 2],
    [8, 3, 0, 4]]
))