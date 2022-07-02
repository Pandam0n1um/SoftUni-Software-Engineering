function processOdd(array) {
    let tempArr = array.filter((x, i) => i % 2)
    newArr=tempArr.map((x)=>x*2).reverse()
    return newArr;
}



console.log(processOdd([10, 15, 20, 25]))
console.log(processOdd([3, 0, 10, 4, 7, 3]))