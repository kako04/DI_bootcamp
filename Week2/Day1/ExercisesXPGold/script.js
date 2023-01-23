// exercise1

let sentence = ["my","favorite","color","is","blue"];
console.log(sentence.join());

// exercise2

let str1 = "mix";
let str2 = "pod";

str1.slice(1)
str2.slice(1)

let concat1 = str1.slice() + str2.slice(0,2)
let concat2 = str2.slice(-1,1) + str1.slice(0,2)
console.log(concat1, concat2);