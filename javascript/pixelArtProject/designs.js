// Select color input
const chooseColor = document.querySelector("#colorPicker");

// Select size input
const tableHeight = document.getElementById('inputHeight');
const tableWidth = document.getElementById('inputWidth');
const canvas = document.getElementById('pixelCanvas');

// When a box is clicked, add color 
function clickedBox(event) {
  const color = colorInput.value;
  event.target.style.backgroundColor = color;
}

// Call makeGrid function when user submits input
function makeGrid() {
  // Your code goes here!
  canvas.innerHTML = '';

  //create a table element and a tbody element
  var table = document.getElementById("pixelCanvas");
  for (var i = 0; i < tableHeight; i++) {
  	var tr = document.createElement("tr");
  	for (var c = 0; c < tableWidth; c++) {
  	var td = document.createElement("td");

    tr.addEventListener('click', clickedBox);
    table.appendChild(tr);
  }
  // Add grid to the table in the DOM
  document.body.appendChild(table);
}
};

document.querySelector('form').addEventListener('submit', function(event){
  event.preventDefault();
  makeGrid();
});