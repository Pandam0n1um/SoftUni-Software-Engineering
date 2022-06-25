function dayMonthOrder(month,year){
    return new Date(year,month,0).getDate();
}



console.log(dayMonthOrder(1,2012))
console.log(dayMonthOrder(2,2012))