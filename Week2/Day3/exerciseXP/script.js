const people = ["Greg", "Mary", "Devon", "James"];

people.shift()
people.splice(-1, 1, "jason")
people.push("kako")

console.log(people.indexOf("Mary"))
console.log(people)

var sliced = people.slice( 1, 3)
console.log(sliced);

console.log(people.indexOf('Foo'));//it returns -1 cus there is no Foo in the array

var last = people.slice(-1);

for (let i = 0; i < people.length; i++) {
    const itemsinpeople = people[i];
    console.log(itemsinpeople);
}
console.log('///////////////////');
for (let i = 0; i < people.length; i++) {
    const itemsinpeople = people[i];
    console.log(itemsinpeople);
    if (itemsinpeople == 'jason') {
        break
    }
}

//exe 2 

