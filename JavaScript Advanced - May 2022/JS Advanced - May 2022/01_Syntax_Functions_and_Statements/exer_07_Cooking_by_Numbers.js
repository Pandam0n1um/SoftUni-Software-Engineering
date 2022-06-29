function cooking(initialValue, ...params) {
    let cookingActions = {
        'chop': function () { return initialNumber / 2 },
        'dice': function () { return Math.sqrt(initialNumber) },
        'spice': function () { return initialNumber + 1 },
        'bake': function () { return initialNumber * 3 },
        'fillet': function () { return initialNumber * 0.8 },
    }
    let initialNumber = Number(initialValue);
    for (let index = 0; index < params.length; index++) {
        currentAction = cookingActions[params[index]];
        initialNumber = currentAction(initialNumber);
        console.log(initialNumber);
    }
}


cooking('32', 'chop', 'chop', 'chop', 'chop', 'chop')
cooking('9', 'dice', 'spice', 'chop', 'bake', 'fillet')