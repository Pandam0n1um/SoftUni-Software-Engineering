function sortNumbers(array) {
    let resultArray = [];
    array = array.sort((a, b) => a - b);
    while (array.length !== 0) {
        resultArray.push(array.shift());
        if (array.length !== 0) {
            resultArray.push(array.pop());
        }
    }
    return resultArray;
}


console.log(sortNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18]
));