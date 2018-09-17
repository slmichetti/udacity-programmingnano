/* FUNCTIONS /*

/*
 * Programming Quiz: Laugh it Off 1 (5-1)
 */

// your code goes here
function laugh() {
	var message = "hahahahahahahahahaha!"
	return message;
}

console.log(laugh());

/*
 * Programming Quiz: Laugh it Off 2 (5-2)
 *
 * Write a function called `laugh` with a parameter named `num` that represents the number of "ha"s to return.
 *
 * Note:
 *  - make sure your the final character is an exclamation mark ("!")
 *  - make sure that your function produces the correct results when it is called multiple times
 */

function laugh(num) {
	var ha = '';
	for (i = 0; i < num; i++) {
	    ha = ha + 'ha';
	}
	return ha + '!';
}

console.log(laugh(5));

/*
 * Programming Quiz: Build A Triangle (5-3)
 */

// creates a line of * for a given length
function makeLine(length) {
    var line = "";
    for (var j = 1; j <= length; j++) {
        line += "* ";
    }
    return line + "\n";
}

// your code goes here.  Make sure you call makeLine() in your own code.
function buildTriangle(width) {
	var triangle = ""; 
	for (var i = 1; i <= width; i++){
		triangle += (makeLine(i));
	}
	return triangle;
}
// test your code by uncommenting the following line
console.log(buildTriangle(10));

/*
 * Programming Quiz: Laugh (5-4)
 */

var laugh = function(num) {
    var ha = '';
    for (i = 0; i < num; i++) {
        ha = ha + 'ha';
    }
    return ha + '!';
};

console.log(laugh(10));

/*
 * Programming Quiz: Cry (5-5)
 */

// your code goes here


// named function expression
var cry = function crying() {
  return 'boohoo!';
};

console.log(cry());

/*
 * Programming Quiz: Inline Functions (5-6)
 */

// don't change this code
function emotions(myString, myFunc) {
    console.log("I am " + myString + ", " + myFunc(2));
}

// your code goes here
// call the emotions function here and pass in an
// inline function expression
emotions ("happy", function laugh(num) {
    var ha = '';
    for (i = 0; i < num; i++) {
        ha = ha + 'ha';
    }
    return ha + '!';
});