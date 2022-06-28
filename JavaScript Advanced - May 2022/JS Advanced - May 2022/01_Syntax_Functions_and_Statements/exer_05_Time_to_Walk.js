function walkDuration(steps, footprint, speedKmH) {
    let distance = steps * footprint;
    let speed = speedKmH * 1000 / 3600
    let countRests = ~~(distance / 500);
    // bitwise division used to  get the quotient
    // console.log(countRests)
    let walkTime = distance / speed;
    let totalTime = walkTime + countRests * 60;
    let hours = Math.floor(totalTime / 3600).toFixed(0).padStart(2, 0);
    let minutes = Math.floor(totalTime / 60).toFixed(0).padStart(2, 0);
    let seconds = (totalTime % 60).toFixed(0).padStart(2, 0);
    console.log(`${hours}:${minutes}:${seconds}`)

}



walkDuration(4000, 0.6, 5)