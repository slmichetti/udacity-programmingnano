// Call makeGrid function when user submits input
function makeGrid() {
	console.log("makeGrid is running!")

	// select grid size inputs
	var height = document.getElementById("inputHeight").value
	var width = document.getElementById("inputWidth").value

	//create the table
	var myGrid = document.getElementById("pixelCanvas");
	var tableBody = document.createElement("tbody");
	myGrid.appendChild(tableBody);

	//clear the table data
	myGrid.innerHTML = '';

	// create the rows and cells
	for (var i = 0; i < height; i++) {
  	var tr = document.createElement("tr");
  	tableBody.appendChild(tr);
  		for (var c = 0; c < width; c++) {
  			var td = document.createElement('td');
  			tr.appendChild(td);
  		td.addEventListener('click', clickedBox);
  		}
    }
    myGrid.appendChild(tableBody);
}

// When a box is clicked, add color 
function clickedBox(event) {
	console.log("colorPicker is running!");
	const color = document.getElementById("colorPicker").value
	event.target.style.backgroundColor = color;
}

document.querySelector('form').addEventListener('submit', function(event){
  event.preventDefault();
  makeGrid();
});