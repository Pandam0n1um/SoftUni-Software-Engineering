function sortMultipleCriteria(array) {
    sortedArray = array.sort((a, b) => a.length - b.length || a.localeCompare(b))
    return sortedArray.join('\n');
}


console.log(sortMultipleCriteria(['alpha',
    'beta',
    'gamma']));
console.log('\n')
console.log(sortMultipleCriteria(['Isacc',
    'Theodor',
    'Jack',
    'Harrison',
    'George']));
console.log('\n')
console.log(sortMultipleCriteria(['test',
    'Deny',
    'omen',
    'Default']
));