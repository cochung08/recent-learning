console.log('Hello World');
var myLines = require('fs').readFileSync('leetcode.txt').toString()

arrayOfLines = myLines.match(/[^\r\n]+/g);
// console.log(arrayOfLines)

var count = 0;
var leetcode = {};
var company = ""

for (i = 0; i < arrayOfLines.length; i++) {
    arrayOfLines[i] =
        arrayOfLines[i].trim()
        // console.log('!'+arrayOfLines[i]+'!',arrayOfLines[i][0].match(/[a-zA-Z]/),"\n");
    if (arrayOfLines[i][0].match(/[a-zA-Z]/)) {
        company = arrayOfLines[i]
            // console.log(company)
        leetcode[company] = []
    } else {
        // console.log(arrayOfLines[i].replace(/\s\s+/g, ' ').split(" "))
        // leetcode[company].push(arrayOfLines[i].replace(/\s\s+/g, ' ').split(" "))
        leetcode[company].push(arrayOfLines[i].split("        "))
    }
}

// console.log(leetcode)
var result = []
var dic = {}
for (var key in leetcode) {
    var value = leetcode[key];
    // console.log(value.length);

    for (index = 0; index < value.length; ++index) {

        if (value[index][1] in dic)
            dic[value[index][1]] += 1
        else dic[value[index][1]] = 1
    }
}
console.log(dic)

// Create items array
var items = Object.keys(dic).map(function(key) {
    return [key, dic[key]];
});
// console.log(items)

// Sort the array based on the second element
items.sort(function(first, second) {
    return second[1] - first[1];
    // return first[1] - second[1];

});

// Create a new array with only the first 5 items
// console.log(items.slice(0, 5));
// console.log(items);
// console.log(leetcode)
// console.log(dic)

result = {};
// console.log(items.length);
for (q = 0; q < items.length; ++q) {
    // company=[]
    // console.log(index)

    for (var comp in leetcode) {
        var record = leetcode[comp];
        // console.log(value.length);

        for (index = 0; index < record.length; ++index) {
            // console.log(value[index][1]);
            // console.log(items[index])

            if (record[index][1] === items[q][0]) {
                // console.log(items[index][0])
                // console.log(items[index][0],items[index][1],comp)
                if (!(items[q][0] in result))
                    result[items[q][0]] = [
                        items[q][1], record[index][3], comp
                    ]
                else result[items[q][0]].push(comp)
            }
        }
    }
}

// var result = JSON.stringify(result)
// for (var key in result) {
//         result[key] = result[key].slice(0,2);
//     }
// console.log(result)


var fs = require('fs');

// var myData = {
//   name:'test',
//   version:'1.0'
// }

myData=result
var outputFilename = './my.json';

fs.writeFile(outputFilename, JSON.stringify(myData, null, 4), function(err) {
    if(err) {
      console.log(err);
    } else {
      console.log("JSON saved to " + outputFilename);
    }
});
console.log(items.length);
