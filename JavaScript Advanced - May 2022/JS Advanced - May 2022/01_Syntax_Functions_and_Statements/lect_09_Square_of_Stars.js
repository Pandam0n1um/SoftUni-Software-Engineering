function squareStars(argument=5){
    for (let index = 0; index < argument; index++) {
        lineOutput='*';
        lineOutput+=' *'.repeat(argument-1)
        console.log(lineOutput)
        
    }
}


squareStars()