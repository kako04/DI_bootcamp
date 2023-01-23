// exercise 1: The World Translator

let userlang = prompt('which language do you speak?').toLowerCase();

if (userlang == "french") {
    console.log("Bonjour");
    
} else if (userlang == "english") {
    console.log("Hello");
} else if (userlang == 'hebrew') {
    console.log('shalom');
} else {
    console.log('01110011 01101111 01110010 01110010 01111001');
}

// Exercise 2 : The Grade Assigner

let gradeUser = prompt("whats your grade?")
if (gradeUser > 90) {
    console.log("A");
} else if (gradeUser > 80 && gradeUser<91) {
    console.log("B");
} else if (gradeUser < 81 && gradeUser > 69) {
    console.log("C");
} else if (gradeUser < 70) {
    console.log("D");
}

// Exercise 3 : Verbing

let userSTR = prompt("string please").toLowerCase()
if (userSTR.length > 2 && userSTR.slice(-3) != "ing") {
    userSTR = userSTR + "ing"
    console.log(userSTR);
} else if (userSTR.length > 2 && userSTR.slice(-3) == "ing") {
    userSTR = userSTR + "ly"
    console.log(userSTR);
} else {
    console.log(userSTR);
}