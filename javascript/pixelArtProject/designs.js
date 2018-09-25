// Call makeGrid function when user submits input
function makeGrid() {
	var height = document.getElementById("inputHeight").value
	var width = document.getElementById("inputWidth").value

	//create the table
	var myGrid = document.getElementById("pixelCanvas");
	var tableBody = document.createElement("tbody");
	myGrid.appendChild(tableBody);

	myGrid.innerHTML = '';
	for (var i = 0; i < height; i++) {
  	var tr = document.createElement("tr");
  	tableBody.appendChild(tr);

  		for (var c = 0; c < width; c++) {
  			var td = document.createElement('td');
  			tr.appendChild(td);
  		}
    }
    myGrid.appendChild(tableBody);
    td.addEventListener('click', clickedBox);
}



// When a box is clicked, add color 
function clickedBox(event) {

	const color = document.getElementById("colorPicker").value
	event.target.style.backgroundColor = color;
}

document.querySelector('form').addEventListener('submit', function(event){
  event.preventDefault();
  makeGrid();
});