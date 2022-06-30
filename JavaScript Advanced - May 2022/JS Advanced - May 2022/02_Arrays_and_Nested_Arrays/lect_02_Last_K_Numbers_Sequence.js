function lastElements(n, k) {
    let finalArray = [1,];
    for (let index = 1; index < n; index++) {
        let currentLength = finalArray.length;
        let tempStart = Math.max(0, (currentLength - k));
        let tempArray = finalArray.slice(tempStart,);
        let newElement = tempArray.reduce((a, b) => a + b, 0);
        finalArray[index] = newElement;
    }
    return (finalArray)
}


console.log(lastElements(8, 2))