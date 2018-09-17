/* ARRAYS */
/*
 * Programming Quiz: UdaciFamily (6-1)
 */

var udaciFamily = ["Julia", "James", "Sheri"];
console.log(udaciFamily);
/* Prints every item in the array/*

/*
 * Programming Quiz: Building the Crew (6-2)
 */

var captain = "Mal";
var second = "Zoe";
var pilot = "Wash";
var companion = "Inara";
var mercenary = "Jayne";
var mechanic = "Kaylee";

// your code goes here
var crew = [captain, second, pilot, companion, mercenary, mechanic];
console.log(crew)

Prints: [ 'Mal', 'Zoe', 'Wash', 'Inara', 'Jayne', 'Kaylee' ]

/*
 * Programming Quiz: The Price is Right (6-3)
 * Change the prices of the 1st, 3rd, and 7th elements in the array.
 */

var prices = [1.23, 48.11, 90.11, 8.50, 9.99, 1.00, 1.10, 67.00];

// your code goes here


prices[0] = 2.46; // changes the second elements price
prices[2] = 93.55; // changes the third elements price
prices[6] = 2.10 // changes the seventh elements price

console.log(prices); 

Prints: [ 2.46, 48.11, 93.55, 8.5, 9.99, 1, 2.1, 67 ]


/*
 * Programming Quiz: Colors of the Rainbow (6-4)
 *
 * Use only the splice() method to modify the rainbow variable:
 *  - remove "Blackberry"
 *  - add "Yellow" and "Green"
 *  - add "Purple"
 */

var rainbow = ['Red', 'Orange', 'Blackberry', 'Blue'];

// your code goes here
rainbow.splice(-2, 1);
rainbow.splice(2, 0, "Yellow", "Green");
rainbow.splice(6, 0, "Purple");
console.log(rainbow);

Prints: [ 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple' ]

/*
 * Programming Quiz: Quidditch Cup (6-5)
 */

// your code goes here
var team = ["Oliver Wood", "Angelina Johnson", "Katie Bell", "Alicia Spinnet", "George Weasley", "Fred Weasley", "Harry Potter"];
console.log(hasEnoughPlayers(team));

function hasEnoughPlayers(array){
  if (array.length >= 7) {
    return true;
  } else {
    return false;
  }
}

var team = ["Oliver Wood", "Angelina Johnson", "Katie Bell", "Alicia Spinnet", "George Weasley", "Fred Weasley", "Harry Potter"];
console.log(hasEnoughPlayers(team));

Prints true

/*
 * Programming Quiz: Joining the Crew (6-6)
 */

var captain = "Mal";
var second = "Zoe";
var pilot = "Wash";
var companion = "Inara";
var mercenary = "Jayne";
var mechanic = "Kaylee";

var crew = [captain, second, pilot, companion, mercenary, mechanic];

var doctor = "Simon";
var sister = "River";
var shepherd = "Book";

// your code goes here
crew.push(doctor, sister, shepherd);
console.log(crew);

Prints: [ 'Mal',
  'Zoe',
  'Wash',
  'Inara',
  'Jayne',
  'Kaylee',
  'Simon',
  'River',
  'Book' ]


/*
 * Programming Quiz: Another Type of Loop (6-8)
 *
 * Use the existing `test` variable and write a `forEach` loop
 * that adds 100 to each number that is divisible by 3.
 *
 * Things to note:
 *  - you must use an `if` statement to verify code is divisible by 3
 *  - you can use `console.log` to verify the `test` variable when you're finished looping
 */

var test = [12, 929, 11, 3, 199, 1000, 7, 1, 24, 37, 4,
    19, 300, 3775, 299, 36, 209, 148, 169, 299,
    6, 109, 20, 58, 139, 59, 3, 1, 139
];

// Write your code here
test.forEach(function(value, index) {
	if(value % 3 === 0) {
		value += 100;
		test.splice(index, 1, value);
	}
});
console.log(test);


/*
 * Programming Quiz: I Got Bills (6-9)
 *
 * Use the .map() method to take the bills array below and create a second array
 * of numbers called totals. The totals array should contains each amount from the
 * bills array but with a 15% tip added. Log the totals array to the console.
 *
 * For example, the first two entries in the totals array would be:
 *
 * [57.76, 21.99, ... ]
 *
 * Things to note:
 *  - each entry in the totals array must be a number
 *  - each number must have an accuracy of two decimal points
 */

var bills = [50.23, 19.12, 34.01,
    100.11, 12.15, 9.90, 29.11, 12.99,
    10.00, 99.22, 102.20, 100.10, 6.77, 2.22
];
var totals = bills.map(function(bill) {
	bill = bill * .15 + bill; 
	return Number(bill.toFixed(2));
});
	
console.log(totals);


/*
 * Programming Quiz: Nested Numbers (6-10)
 *
 *   - The `numbers` variable is an array of arrays.
 *   - Use a nested `for` loop to cycle through `numbers`.
 *   - Convert each even number to the string "even"
 *   - Convert each odd number to the string "odd"
 */

var numbers = [
    [243, 12, 23, 12, 45, 45, 78, 66, 223, 3],
    [34, 2, 1, 553, 23, 4, 66, 23, 4, 55],
    [67, 56, 45, 553, 44, 55, 5, 428, 452, 3],
    [12, 31, 55, 445, 79, 44, 674, 224, 4, 21],
    [4, 2, 3, 52, 13, 51, 44, 1, 67, 5],
    [5, 65, 4, 5, 5, 6, 5, 43, 23, 4424],
    [74, 532, 6, 7, 35, 17, 89, 43, 43, 66],
    [53, 6, 89, 10, 23, 52, 111, 44, 109, 80],
    [67, 6, 53, 537, 2, 168, 16, 2, 1, 8],
    [76, 7, 9, 6, 3, 73, 77, 100, 56, 100]
];

// determines length of the array being looped over in the row
for (var row = 0; row < numbers.length; row++) {
    for (var column = 0; column < numbers[row].length; column++) {
        if (numbers[row][column] % 2 === 0) {
            numbers[row][column] = "even";  //change the numbers divisible by 2 to even
        }
        else {
            numbers[row][column] = "odd";  //change the odd numbers
        }
    }
}
console.log(numbers);