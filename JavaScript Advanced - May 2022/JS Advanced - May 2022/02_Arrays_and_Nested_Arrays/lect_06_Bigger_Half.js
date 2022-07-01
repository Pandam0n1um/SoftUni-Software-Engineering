function biggerHalf(array){
    array.sort((a,b)=>(a-b));
    // let spliceStart=array.length-Math.ceil(array.length/2);
    let spliceStart=Math.floor(array.length/2);
    return array.splice(spliceStart)
}

console.log(biggerHalf([3,19,14,7,2,19,6]));