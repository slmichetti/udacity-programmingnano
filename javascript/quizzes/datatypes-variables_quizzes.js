/* code in JavaScript*/
var count = 1; 
var name = "Julia";
var num = 1.2932;
var price = 2.99;


// this expression equals 4, change it to equal 42
console.log(((10*10) - 50 + 24) / 2 + 5);

/*
 * Programming Quiz: Converting Tempatures (2-2)
 *
 * The Celsius-to-Fahrenheit formula:
 *
 *    F = C x 1.8 + 32
 *
 * 1. Set the fahrenheit variable to the correct value using the celsius variable and the forumla above
 * 2. Log the fahrenheit variable to the console
 *
 */

var celsius = 12;
var fahrenheit = (celsius * 1.8 + 32)

console.log(fahrenheit);

/*
 * Programming Quiz: Favorite Food (2-3)
 */

console.log("My favorite food is Thai Red Curry");

/*
 * Programming Quiz: String Equality for All (2-4)
 */

// fix the right side of the expression
var answer = "ALL Strings are CrEaTeD equal" == "ALL Strings are CrEaTeD equal";
console.log(answer);

/*
 * Programming Quiz: All Tied Up (2-5)
 */

var joke = "Why couldn\'t the shoes go out and play? \nThey were all \"tied\" up!"
console.log(joke);

/*
 * Programming Quiz: Yosa Buson (2-6)
 */

var haiku = "Blowing from the west \nFallen leaves gather \nIn the east.";
console.log(haiku);

/*
 * Programming Quiz: Semicolons! (2-8)
 */

// your code goes here
var thingOne = "red";
var thingTwo = "blue";
console.log(thingOne, thingTwo);

/*
 * Programming Quiz: Out to Dinner (2-10)
 */

// your code goes here
var bill = 10.25 + 3.99 + 7.15;
var tip = bill * 0.15;
var total = bill + tip;
console.log("$" + total.toFixed(2))

/*
 * Programming Quiz: MadLibs (2-11)
 * 
 * 1. Declare a madLib variable
 * 2. Use the adjective1, adjective2, and adjective3 variables to set the madLib variable to the message:
 * 
 * 'The Intro to JavaScript course is amazing. James and Julia are so fun. I cannot wait to work through the rest of this entertaining content!'
 */

var adjective1 = 'amazing';
var adjective2 = 'fun';
var adjective3 = 'entertaining';
var madLib = "The Intro to JavaScript course is "+ adjective1 +". James and Julia are so "+ adjective2 + ". I cannot wait to work through the rest of this " + adjective3 + " content!";
// your code goes here
console.log(madLib);

/*
 * Programming Quiz: One Awesome Message (2-12)
 *
 * 1. Create the following variables:
 *     - firstName
 *     - interest
 *     - hobby
 * 2. Create a variable named awesomeMessage and set it to an awesome message using
      string concatenation and the variables above.
 * 3. Log the awesomeMessage variable to the console.
 */

/*
 * Notes:
 * - The `awesomeMessage` should have the format of:
 *   Hi, my name is _____. I love _____. In my spare time, I like to _______.
 *
 * - Be sure to include spaces and periods where necessary!
 */

// Add your code here
var firstName = "Sheri";
var interest = "horses";
var hobby = "kayak";
var awesomeMessage = "Hi, my name is " + firstName +". I love " +interest+". In my spare time, I like to " + hobby +".";
console.log(awesomeMessage);

/*
 * Programming Quiz: Even or Odd (3-2)
 *
 * Write an if...else statement that prints `even` if the 
 * number is even and prints `odd` if the number is odd.
 *
 * Note - make sure to print only the string "even" or the string "odd"
 */

// change the value of `number` to test your if...else statement
var number = 2;

if (number % 2 === 0) {
    console.log("even");
} else {
	console.log("odd");
}

