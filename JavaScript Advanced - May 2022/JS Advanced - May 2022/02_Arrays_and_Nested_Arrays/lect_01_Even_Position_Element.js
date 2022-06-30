function evenElements(params){
    result=String(params[0])
    for (let index = 2; index < params.length; index+=2) {
        result+=(' '+ String(params[index]));
    }
    return(result)
}



console.log(evenElements(['20', '30', '40', '50', '60']))