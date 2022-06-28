function sameNumbers(value) {
    let inputNumber = value.toString();
    let totalSum = 0;
    let areSame = true;
    let numberLength = inputNumber.length;
    let initialDigit = inputNumber[0];

    for (let index = 0; index < numberLength; index++) {
        totalSum += Number(inputNumber[index]);

        if (inputNumber[index] != initialDigit) {
            areSame = false;
        }
    }
    console.log(areSame);
    console.log(totalSum);
}



sameNumbers(22222)