function solve(...params) {
    let result = -Number.MAX_VALUE;
    for (index = 0; index < params.length; index++) {
        if (params[index] > result) {
            result = params[index]
        };
    }
    console.log(`The largest number is ${result}.`)
}


solve(1, 3, 4, 7, 2)