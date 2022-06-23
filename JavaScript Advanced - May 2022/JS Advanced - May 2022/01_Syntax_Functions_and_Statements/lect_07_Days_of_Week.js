function weekdayOrder(day) {
    let order;
    switch (day) {
        case 'Monday': order = 1; break;
        case 'Tuesday': order = 2; break;
        case 'Wednesday': order = 3; break;
        case 'Thursday': order = 4; break;
        case 'Friday': order = 5; break;
        case 'Saturday': order = 6; break;
        case 'Sunday': order = 7; break;
        default: order='error'
    }
    return order;
}



console.log(weekdayOrder('Tuesday'))
console.log(weekdayOrder('Sunday'))
console.log(weekdayOrder('Saturday'))