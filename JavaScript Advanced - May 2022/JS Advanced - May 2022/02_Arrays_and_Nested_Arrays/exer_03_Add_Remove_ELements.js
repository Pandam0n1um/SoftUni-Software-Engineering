function arrayAddRemove(commands) {
    let result = [];
    let value = 1;
    for (let index = 0; index < commands.length; index++) {
        if (commands[index] === 'add') {
            result.push(value);
        } else {
            result.pop()
        }
        value += 1
    }
    if (result.length) {
        return result.join('\n');
    } else {
        return 'Empty';
    }
}


console.log(arrayAddRemove(['add',
    'add',
    'add',
    'add']
))

console.log('new row')
console.log(arrayAddRemove(['add',
    'add',
    'remove',
    'add',
    'add']))
console.log(arrayAddRemove(['remove',
    'remove',
    'remove']
))