function solver(x1, y1, x2, y2) {
    function distanceCalculator(xPoint1, yPoint1, xPoint2, yPoint2) {
        let distance = Math.sqrt((xPoint1 - xPoint2) ** 2 + (yPoint1 - yPoint2) ** 2);
        let validity = Number.isInteger(distance) ? 'valid' : 'invalid';
        return `{${xPoint1}, ${yPoint1}} to {${xPoint2}, ${yPoint2}} is ${validity}`
    }
    return `${distanceCalculator(x1, y1, 0, 0)} \n${distanceCalculator(x2, y2, 0, 0)} \n${distanceCalculator(x1, y1, x2, y2)}`
}




console.log(solver(2,1,1,1))