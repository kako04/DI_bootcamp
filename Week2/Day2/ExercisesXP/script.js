
// exercise 1
let x = 5;
let y = 2;

if (x > y){
    console.log("x is the biggest number");
} else if (y > x){
    console.log("y is the biggest number");
} else {
    console.log("x = y");
}

// exercise 2: chihuahua

let newDog = "Chihuahua"
console.log(newDog.length);
console.log(newDog.toLowerCase());
console.log(newDog.toUpperCase());

if (newDog == "Chihuahua") {
    console.log('I love Chihuahuas, it’s my favorite dog breed');
} else {
    console.log('I dont care, I prefer cats');
}

// exrcise 3  even or odd

let num = prompt("number: ");

if (num % 2 == 0 ){
    console.log('x is an even number');
} else if (num % 2 == 1){
    console.log('x is an odd number');
} else {
    console.log("i want number only!");
}

//exercise 4 : group chat

const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000", 'user_1', 'user_2','user_3', 'user_4'];

if (users.length == 0) {
    console.log('no one is online');
} else if (users.length == 1) {
    console.log(users[0]+ " is online");
} else if (users.length == 2) {
    console.log(users[0]+ " and " + users[1]+ " are online");
}else {
    console.log(
        users[0], ", ", users[1], " and", users.slice(2).length, "more are online"
    );
}

