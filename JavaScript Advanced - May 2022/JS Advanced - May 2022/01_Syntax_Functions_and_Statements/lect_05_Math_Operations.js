function mathOperation(argument_1, argument_2, action){
    let result;
    switch(action){
        case '+': result=argument_1+argument_2;break;
        case '-': result=argument_1-argument_2;break;
        case '*': result=argument_1*argument_2;break;
        case '/': result=argument_1/argument_2;break;
        case '%': result=argument_1%argument_2;break;
        case '**': result=argument_1**argument_2;break;
    }
    console.log(result)
}




mathOperation(1,3,'+')