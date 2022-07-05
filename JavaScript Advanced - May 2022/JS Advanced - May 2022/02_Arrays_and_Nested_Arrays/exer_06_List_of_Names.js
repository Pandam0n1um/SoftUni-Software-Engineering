function sortAlphabetically(array) {
    let sortedArray = array.sort((a, b) => a.localeCompare(b));
    let positionNumber = 1;
    sortedArray.forEach((el) => {
        console.log(`${positionNumber}.${el}`);
        positionNumber += 1;
    })
}



console.log(sortAlphabetically(["John", "Bob", "Christina", "Ema"]));
