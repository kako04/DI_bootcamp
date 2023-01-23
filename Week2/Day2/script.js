// const userCart = {
// 	username : "John",
// 	password: 1234,
// 	isUserSignedIn : true,
// 	cart : {
// 		apple : 2,
// 		banana : 1,
// 		pear : 5,
// 	},
// 	prices : {
// 		apple : 0.5,
// 		banana : 0.8646466363,
// 		pear : 0.2
// 	}
// };

// userCart.lastname = "smith"

// userCart.username = "Tom"

// userCart.prices.pear *=  1.17

// let userChoice = prompt('Which fruit do you want, apple, banana or pear?').toLowerCase()

// let value = userCart['prices'][userChoice]
// console.log(`price: ${value}`);

// console.log(userCart);

// 1. Add the lastname Smith to the object
// 2. Change the username from John to Tom
// 2. Change the price of the pear, so it will include the Taxes. (17% is 0.17)
// 3. Ask the user for the fruit he wants between Apple, Banana and Pear. Make sure that your code accept all type of strings, for example "Banana" or "banana" or "BaNaNA"
// 4. Console.log the price for the specific fruit the user wants


// exercise 1

let userAge = prompt("how old are you?")

if (userAge < 18){
    console.log('Sorry, you are too young to drive this car. Powering off');
    
} else if (userAge == 18) {
    console.log('Congratulations on your first year of driving. Enjoy the ride!');
    
} if (userAge > 18) {
    console.log('Powering On. Enjoy the ride!');
    
}