const fs = require("fs");

//Reads the values
var values = fs.readFileSync('input.txt', 'utf8').split("\r\n");

var comparision = [];
var count = 0;
var row;

//Creates an array for "x values" for each value in the array, defined as "y"
for(var x = 0; x < 1000; x++) { comparision[x] = []; }

for(var x = 0; x < values.length; x++) {
    //Parses the value to make meaningful variables.
    var parsedInput = values[x].split("@ ")[1];

    var posX = Number(parsedInput.split(",")[0]);
    var posY = Number(parsedInput.split(",")[1].split(":")[0]);

    var areaX = Number(parsedInput.split(",")[1].split(":")[1].split("x")[0].trim());
    var areaY = Number(parsedInput.split(",")[1].split(":")[1].split("x")[1]);

    //For each row to be filled (areaY), go to the posX and +1 all values for areaX amount of times.
    for(var y = 0; y < areaY; y++) {
        row = comparision[posY + y]; //posY as starting point and goes until the loop stops.

        for(var z = 0; z < areaX; z++) {
            row[posX + z] = (row[posX + z] == null) ? 1 : row[posX + z] += 1;

            //If this is the first overlap, add to the overlap counter.
            if(row[posX + z] == 2) { count += 1; }
        }
    }
}

console.log("Your answer is... " + count);