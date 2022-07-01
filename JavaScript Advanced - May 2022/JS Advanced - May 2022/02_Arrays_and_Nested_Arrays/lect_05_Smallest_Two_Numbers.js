function smallestTwo(array){
    array.sort((a,b)=>a-b);
    return array.splice(0,2).join(' ')
}


console.log(smallestTwo([30,15,50,5]));