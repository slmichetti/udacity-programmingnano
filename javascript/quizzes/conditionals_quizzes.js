
/*
 * Programming Quiz: Musical Groups (3-3)
 * 
 *  prints "not a group" if musicians is less than or equal to 0
 *  prints "solo" if musicians is equal to 1
 *  prints "duet" if musicians is equal to 2
 *  prints "trio" if musicians is equal to 3
 *  prints "quartet" if musicians is equal to 4
 *  prints "this is a large group" if musicians is greater than 4
 */

// change the value of `musicians` to test your conditional statements
var musicians = 1;

/*
 * Programming Quiz: Musical Groups (3-3)
 */

// change the value of `musicians` to test your conditional statements
var musicians = 1;

if(musicians === 1) {
  musicians = "solo";
} else if(musicians === 2) {
  musicians = "duet";
} else if(musicians === 3) {
  musicians = "trio";
} else if(musicians === 4) {
  musicians = "quartet";
} else if(musicians > 4) {
  musicians = "This is a large group";
} else {
  musicians = "Not a group";
}

/*
 * Programming Quiz: Murder Mystery (3-4)
 */

// change the value of `room` and `suspect` to test your code
var room = "dining room";
var suspect = "Mr. Parkes";

var weapon = "";
var solved = false;

if (room == "dining room") {
        weapon = "knife";
			if (suspect == "Mr. Parkes") {
				solved = true;
			}
    
} else if (room == "gallery") {
		weapon = "trophy";
			if (suspect == "Ms. Van Cleve") {
				solved = true;
			}
} else if (room == "ballroom") {
		weapon = "poison";
			if (suspect == "Mr.Kalehoff") {
				solved = true;
			}
} else {
		weapon == "pool stick";
			if (suspect = "Mrs. Sparr") {
				solved = true;
			}
    
}

if (solved) {
	console.log(suspect + " did it in the " + room + " with the " + weapon +"!");
}

// Alternative Answer:

// change the value of `room` and `suspect` to test your code
var room = "dining room";
var suspect = "Mr. Parkes";

var weapon = "";
var solved = false;

if (room === "dining room") {
    weapon = "knife", solved = true, suspect === "Mr. Parkes";
} else if (room === "ballroom") {
    weapon = "poison", solved = true, suspect === "Mr. Kalehoff";
} else if (room === "billiards room") {
    weapon = "pool stick", solved = true, suspect === "Mrs. Sparr";
} else {
    weapon = "trophy", solved = true, suspect === "Ms. Van Cleve";
}

if (solved) {
	console.log(suspect + " did it in the " + room + " with the " + weapon +"!");
}

/*
 * Programming Quiz - Checking Your Balance (3-5)
 */

// change the values of `balance`, `checkBalance`, and `isActive` to test your code
var balance = 650.00; //the account balance; can be less than, greater than or equal to 0
var checkBalance = true; // to check the balance. boolean
var isActive = true; // if the account is active  boolean

// your code goes here
if (checkBalance === false) {
    console.log("Thank you. Have a nice day");
}
else if (checkBalance == isActive && balance > 0) {
	console.log("Your balance is $" + balance.toFixed(2) + ".");
}
else if (checkBalance == isActive && balance === 0) {
	console.log("Your account is empty.");
}
else if (checkBalance == isActive && balance < 0) {
	console.log("Your balance is negative. Please contact the bank.");
}
else if (checkBalance === true && isActive === false) {
	console.log("Your account is no longer active.");
}
else {
	console.log("Thank you. Have a nice day!");
}

/*
 * Programming Quiz: Ice Cream (3-6)
 *
 * Write a single if statement that logs out the message:
 * 
 * "I'd like two scoops of __________ ice cream in a __________ with __________."
 * 
 * ...only if:
 *   - flavor is "vanilla" or "chocolate"
 *   - vessel is "cone" or "bowl"
 *   - toppings is "sprinkles" or "peanuts"
 *
 * We're only testing the if statement and your boolean operators. 
 * It's okay if the output string doesn't match exactly.
 */

// change the values of `flavor`, `vessel`, and `toppings` to test your code
var flavor = "vanilla";
var vessel = "cone";
var toppings = "sprinkles";

// Add your code here
if ((flavor == "vanilla" || flavor == "chocolate") && (vessel == "cone" || vessel == "bowl") && (toppings == "sprinkles" || toppings == "peanuts")) {
	console.log("I'd like two scoops of " + flavor + " ice cream in a " + vessel + " with " + toppings + ".");
} else 
	console.log()


/*
 * Programming Quiz: What do I Wear? (3-7)
 *
 * Using if/else statements, create a series of logical expressions that logs the size of a t-shirt based on the measurements of:
 *   - shirtWidth
 *   - shirtLength
 *   - shirtSleeve
 *
 * Use the chart above to print out one of the following correct values:
 *   - S, M, L, XL, 2XL, or 3XL
 */

// change the values of `shirtWidth`, `shirtLength`, and `shirtSleeve` to test your code
var shirtWidth = 18;
var shirtLength = 29;
var shirtSleeve = 8.47;

// Write your if/else code here
if ((shirtWidth >= 18 && shirtWidth < 20) && 
    (shirtLength >= 20 && shirtLength < 29) &&
    (shirtSleeve >= 8.13 && shirtSleeve < 8.38)) {
    console.log("S");
}
else if ((shirtWidth >= 20 && shirtWidth < 22) && 
    (shirtLength >= 29 && shirtLength < 30) &&
    (shirtSleeve >= 8.38 && shirtSleeve < 8.63)) {
    console.log("M");
}
else if ((shirtWidth >= 22 && shirtWidth < 24) && 
    (shirtLength >= 30 && shirtLength < 31) &&
    (shirtSleeve >= 8.63 && shirtSleeve < 8.88)) {
    console.log("L");
}
else if ((shirtWidth >= 24 && shirtWidth < 26) && 
    (shirtLength >= 31 && shirtLength < 33) &&
    (shirtSleeve >= 8.88 && shirtSleeve < 9.63)) {
    console.log("XL");
}
else if ((shirtWidth >= 26 && shirtWidth < 28) && 
    (shirtLength >= 33 && shirtLength < 34) &&
    (shirtSleeve >= 9.63 && shirtSleeve < 10.13)) {
    console.log("2XL");
}
else if ((shirtWidth >= 28 && shirtWidth < 30) && 
    (shirtLength >= 34 && shirtLength < 35) &&
    (shirtSleeve >= 10.13 && shirtSleeve < 10.63)) {
    console.log("3XL");
} else 
	console.log("N/A");

/*
 * Programming Quiz: Back to School (3-9)
 *
 * Write a switch statement to set the average salary of a person based on their type of completed education.
 *
 */

// change the value of `education` to test your code
var education = 'no high school diploma';

// set the value of this based on a person's education
var salary;

// your code goes here
switch (education) {
  case "no high school diploma":
    salary ="$25,636";
    break;
  case "a high school diploma":
    salary ="$35,256";
    break;
  case"an Associate's degree" :
    salary ="$41,496";
    break;
  case "a Bachelor's degree":
    salary ="$59,124";
    break;
  case "a Master's degree": 
    salary ="$69,732";
    break;
  case "a Professional degree":
    salary ="$89,960";
    break;
  case "a Doctoral degree":
    salary="$84,396";
    break;
}
console.log("In 2015, a person with " + education +" earned an average of "+ salary.toLocaleString()+"/year.");
