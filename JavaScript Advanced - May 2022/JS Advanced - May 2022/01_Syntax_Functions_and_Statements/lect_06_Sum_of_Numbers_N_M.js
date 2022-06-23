function sumNtoM(start, end) {
    totalSum = 0
    for (let index = Number(start); index <= Number(end); index++) {
        totalSum += index;
    }
    return totalSum;
}



sumNtoM('1','5')