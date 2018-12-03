const fs = require("fs");

//Reads the values.
var values = fs.readFileSync('input.txt', 'utf8').split("\r\n");

var comparision = [];
var row, idNoClaim;

//Creates a x value array for each value, y or "row"
for(var x = 0; x < 1000; x++) { comparision[x] = []; }

for(var x = 0; x < values.length; x++) {
    //Parses the input
    var id = values[x].split(" @")[0];
    var parsedInput = values[x].split("@ ")[1];

    var posX = Number(parsedInput.split(",")[0]);
    var posY = Number(parsedInput.split(",")[1].split(":")[0]);

    var areaX = Number(parsedInput.split(",")[1].split(":")[1].split("x")[0].trim());
    var areaY = Number(parsedInput.split(",")[1].split(":")[1].split("x")[1]);

    //Adds the id as the value, if there is already a value, change to x.
    for(var y = 0; y < areaY; y++) {
        row = comparision[posY + y];

        for(var z = 0; z < areaX; z++) {
            row[posX + z] = (row[posX + z] == null) ? id : "x";
        }
    }
}

//Checks for an input that does not overlap at all.
for(var x = 0; x < values.length; x++) {
    //Parses the input.
    var id = values[x].split(" @")[0];
    var parsedInput = values[x].split("@ ")[1];

    var posX = Number(parsedInput.split(",")[0]);
    var posY = Number(parsedInput.split(",")[1].split(":")[0]);

    var areaX = Number(parsedInput.split(",")[1].split(":")[1].split("x")[0].trim());
    var areaY = Number(parsedInput.split(",")[1].split(":")[1].split("x")[1]);

    var test = true; //Will change to false if a value of "x" is found.

    for(var y = 0; y < areaY; y++) {
        row = comparision[posY + y];

        for(var z = 0; z < areaX; z++) { 
            if(row[posX + z] == "x") { test = false; } 
        }
    }

    if(test == true) { idNoClaim = id; }
}

console.log("Your answer is... " + idNoClaim);