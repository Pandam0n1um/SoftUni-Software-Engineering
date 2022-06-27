function aggregateElements(params) {
    let numbersArray = params.map(Number);
    let totalSum=0;
    let totalInverseSum=0;
    let concatResult='';
    for (let index = 0; index < numbersArray.length; index++) {
        currentElem=numbersArray[index];
        totalSum += currentElem;
        totalInverseSum += (1 /currentElem);
        concatResult += String(currentElem);
    }
    console.log(totalSum);
    console.log(totalInverseSum);
    console.log(concatResult);
}


aggregateElements([1, 2, 3])



// alternative
// function aggregateElements(array) {
//     let numbersArray = array.map(Number);
//     let sum = numbersArray.reduce((a, b) => a + b);
 
//     let inverseValuesSum = 0;
 
//     for (let i = 0; i < numbersArray.length; i++) {
//         inverseValuesSum += 1 / numbersArray[i];
//     }
 
//     let stringConcat = numbersArray.join('');
 
//     console.log(sum);
//     console.log(inverseValuesSum);
//     console.log(stringConcat);
// }