function areaCalc(argument) {
    let argType = typeof (argument);
    if (argType !== 'number') {
        console.log(`We can not calculate the circle area, because we receive a ${argType}.`);
    } else {
        area = Math.pow(argument, 2) * Math.PI;
        // console.log(typeof(area));
        console.log(area.toFixed(2));
    }
}



areaCalc(4.5)
areaCalc(5)