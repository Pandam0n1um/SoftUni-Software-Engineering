function orderNumbers(array) {
    let resultArray = [];
    for (let index = 0; index < array.length; index++) {
        if (array[index] < 0) {
            resultArray.unshift(array[index])
        } else {
            resultArray.push(array[index])
        }
    }
    // resultArray.splice(1,0,4,5,6) 
    //test of splice method
    return resultArray.join('\n');
}

console.log(orderNumbers([7, -2, 8, 9]))