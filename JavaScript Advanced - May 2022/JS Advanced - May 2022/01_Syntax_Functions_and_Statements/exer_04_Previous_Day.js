function previousDayCalculator(year, month, day) {
    let currentDay = new Date(year, month-1, day);
    let previousDay = new Date(currentDay.setDate(currentDay.getDate() - 1));
    let result = previousDay.getFullYear() + '-' + (previousDay.getMonth()+1) + '-' + previousDay.getDate()
    console.log(result);
}



previousDayCalculator(1999, 01, 01)