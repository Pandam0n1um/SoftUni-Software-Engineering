function calculatorFirstLast(array) {
    let lastIndex = array.length - 1;
    let result = Number(array[0]) + Number(array[lastIndex]);
    return result
}


console.log(calculatorFirstLast(['20', '30', '40']))