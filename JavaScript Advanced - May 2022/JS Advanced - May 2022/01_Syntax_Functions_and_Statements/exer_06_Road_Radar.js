function radar(speed, area) {
    let speedLimit = {
        'motorway': 130,
        'interstate': 90,
        'city': 50,
        'residential': 20,
    }

    let allowedSpeed = speedLimit[area];
    let difference = speed - allowedSpeed;
    let drivingStatus;

    if (difference <= 0) {
        console.log(`Driving ${speed} km/h in a ${allowedSpeed} zone`);
    } else {
        if (difference <= 20) {
            drivingStatus = 'speeding';
        } else if (difference <= 40) {
            drivingStatus = 'excessive speeding';
        } else {
            drivingStatus = 'reckless driving';
        }
        console.log(`The speed is ${difference} km/h faster than the allowed speed of ${allowedSpeed} - ${drivingStatus}`)
    }
}


radar(40, 'city')
radar(21, 'residential')
radar(120, 'interstate')
radar(200, 'motorway')
