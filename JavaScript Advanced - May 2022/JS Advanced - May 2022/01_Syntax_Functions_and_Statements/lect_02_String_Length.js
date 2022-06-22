function stringLength(...params) {
    let sum=0
    let avg=0
    for (var string of params){
        sum+=string.length;
    }

    console.log(sum)
    console.log(sum/params.length|0)

}



