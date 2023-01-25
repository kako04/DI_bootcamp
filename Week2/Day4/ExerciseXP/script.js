function infoAboutMe() {
    console.log('my name is akaki not akki');
}
infoAboutMe()

function infoAboutPerson(personName, personAge, personFavoriteColor) {
    console.log(`your name is ${personName} youur age is ${personAge} your fav color ${personFavoriteColor}`);


}
infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")

console.log('/////////////');
// exercise 2
function calculateTip() {
    let bill = prompt("how much is the bill")
    if (bill < 50) {
        console.log(`pay ${bill*1.2}`);    

    } else if (bill >= 50 && bill < 200) {
        console.log(`pay ${bill*1.15}`);
    } else {
        console.log(`pay ${bill*1.1}`);
    }
}
calculateTip()

console.log('///////////');
// exercise 3
function isDivisible(divisor) {
    for (let i = 0; i <= 500; i++) {
        if (i % divisor == 0 ) {
            console.log(i);
        }
    }
}
isDivisible(33)
console.log('//////');
// exercise 4

const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = ['banana', 'orange', 'apple']
function myBill() {
    for (let i = 0; i < shoppingList.length; i++) {
        if (shoppingList[i] in stock) {
            console.log(`${shoppingList[i]} is in stock`);
            console.log(`price: ${prices[shoppingList[i]]}`);
        } else {
            console.log(`${shoppingList[i]} is not in stock`);
            break
        }
    }
}
myBill()


console.log('/////////');
//exercise 5

function changeEnough(itemPrice, amountOfChange) {
    let totalvalue = amountOfChange[0] * 0.25 + amountOfChange[1] * 0.1 + amountOfChange[2] * 0.05 + amountOfChange[3] * 0.01
    console.log(totalvalue);
    console.log(itemPrice);
    if (itemPrice > totalvalue) {
        console.log("false");
    } else if (itemPrice <= totalvalue){
        console.log('true');
    }
}
changeEnough(4.25, [25, 20, 5, 0])

// changeEnough[1][0] = 0.25
// changeEnough[1][1] = 0.1
// changeEnough[1][2] = 0.05
// changeEnough[1][3] = 0.01

console.log('//////////////');
//exercise 6
function hotelCost(NON) {
    for (let l = 0;  l++) {
        if () {
        
        }
        
    }
}
hotelCost(prompt("how many nights??"))