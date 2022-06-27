function fruitMoney(fruitType, weightGrams, priceKilogram) {
    moneyNeeded = weightGrams * priceKilogram / 1000
    output = `I need $${moneyNeeded.toFixed(2)} to buy ${(weightGrams / 1000).toFixed(2)} kilograms ${fruitType}.`;
    console.log(output)
}


fruitMoney('orange', 2500, 1.8)