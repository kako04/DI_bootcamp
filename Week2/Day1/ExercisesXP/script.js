let FavFood = "khachapuri"
let FavMeal = "dinner"
console.log(`i eat ${FavFood} at every ${FavMeal}`);


const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries.length
let myWatchedSeriesSentence = [myWatchedSeries[0], myWatchedSeries[1], myWatchedSeries[2]]
console.log(`i watched ${myWatchedSeriesLength} series: ${myWatchedSeriesSentence[0]}, ${myWatchedSeriesSentence[1]} and ${myWatchedSeriesSentence[2]}`);

myWatchedSeries[2] = "friends"
myWatchedSeries[3] = "breaking bad"
myWatchedSeries.unshift("rick and morty")
myWatchedSeries.splice(1,1)
console.log(myWatchedSeries[1][2]);
console.log(myWatchedSeries);

// exercise 3

let Ctemp = 130
let Ftemp = (Ctemp * 9/5) + 32
console.log(`${Ctemp}°C is ${Ftemp}°F`);


console.log("/////////////////////////////////////////////////////////////////");
// Exercise 4

// 1.
let c;
let a = 34;
let b = 21;

// 2.
console.log(a+b) //first expression
// Prediction: 55 because , a and b are variables that equal numbers
// Actual: 55

// 3.
a = 2;

console.log(a+b) //second expression
// Prediction: 23 because a changed value
// Actual: 23

// 4.
console.log(c);
// Prediction: c doesnt have value so its NaN
// Actual: undefined

// 4.
console.log(3+4+'5');
// Prediction: 75 cus 5 is string
// Actual: 75

console.log("////////////////////////////////////");
// Exercise 5

typeof(15)
// Prediction: number
// Actual:number

typeof(5.5)
// Prediction: number
// Actual:number

typeof(NaN)
// Prediction: undefined
// Actual:number            wrong

typeof("hello")
// Prediction: string
// Actual:string

typeof(true)
// Prediction: boolean
// Actual:boolean

typeof(1 != 2)
// Prediction: boolean
// Actual:boolean

"hamburger" + "s"
// Prediction: hamburgers
// Actual:hamburgers

"hamburgers" - "s"
// Prediction: undefined / error
// Actual: NaN                   wrong

"1" + "3"
// Prediction: 13
// Actual: 13

"1" - "3"
// Prediction: undefined / error
// Actual: -2                  very wrong

"johnny" + 5
// Prediction: johnny5 
// Actual:johnny5 

"johnny" - 5
// Prediction: undefined / error
// Actual: NaN                    wrong

99 * "hello"
// Prediction: hellohellohellohello 94 more times
// Actual:NaN                       very wrong

1 != 1
// Prediction: false
// Actual: false

1 == "1"
// Prediction: true
// Actual: true

1 === "1"
// Prediction: false
// Actual: false

console.log("//////////////////////////////////////");
// Exercise 6 

5 + "34"
// Prediction: 534
// Actual:534

5 - "4"
// Prediction: NaN
// Actual:1         wrong

10 % 5
// Prediction: 0
// Actual:0

5 % 10
// Prediction: 0.5
// Actual:5                 wrong

"Java" + "Script"
// Prediction:JavaScript
// Actual:JavaScript

" " + " "
// Prediction:'  '
// Actual:'  '

" " + 0
// Prediction:' 0'
// Actual:' 0'

true + true
// Prediction:2
// Actual:2

true + false
// Prediction:1
// Actual:1

false + true
// Prediction:1
// Actual:1

false - true
// Prediction:-1
// Actual:-1

!true
// Prediction:false
// Actual:false

3 - 4
// Prediction:-1
// Actual:-1

"Bob" - "bill"
// Prediction:NaN
// Actual:NaN
