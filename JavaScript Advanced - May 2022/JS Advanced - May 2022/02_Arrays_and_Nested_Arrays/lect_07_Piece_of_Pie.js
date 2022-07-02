function pieSection(pieFlavours, start, end) {
    let addFlavour = false;
    let sectionFlavour = [];
    for (let index = 0; index < pieFlavours.length; index++) {
        if (pieFlavours[index] === start) {
            addFlavour = true;
        }
        if (addFlavour) {
            sectionFlavour.push(pieFlavours[index]);
        }
        if (pieFlavours[index] === end) {
            break;
        }
    }
    return sectionFlavour;
}

console.log(pieSection(['Pumpkin Pie',
    'Key Lime Pie',
    'Cherry Pie',
    'Lemon Meringue Pie',
    'Sugar Cream Pie'],
    'Key Lime Pie',
    'Lemon Meringue Pie'));