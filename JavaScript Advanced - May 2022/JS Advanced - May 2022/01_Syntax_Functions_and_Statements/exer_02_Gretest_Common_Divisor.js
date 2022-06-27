function gretestCommonDivisor(argument1, argument2) {
    while (argument1 !== argument2){
        if (argument1>argument2){
            argument1-=argument2;
        }else{
            argument2-=argument1
        }
    }
    console.log(argument1);
}



gretestCommonDivisor(1,0)