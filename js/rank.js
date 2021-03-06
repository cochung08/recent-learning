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
        // console.log(arrayOfLines)
    if (arrayOfLines[i][0].match(/[a-zA-Z]/)) {
        company = arrayOfLines[i]
            // console.log(company)
        leetcode[company] = []
    } else {
        // console.log(arrayOfLines[i].replace(/\s\s+/g, ' ').split(" "))
        // leetcode[company].push(arrayOfLines[i].replace(/\s\s+/g, ' ').split(" "))
        leetcode[company].push(arrayOfLines[i].split("        "))
            // console.log(arrayOfLines[i].split("        ").length);
    }
}

// console.log(leetcode)
Object.keys(leetcode).forEach(function(key) {
    var val = leetcode[key];
    val.sort(function(a, b) {
        return parseFloat(a[0]) - parseFloat(b[0]);
    });
    newName = key.substr(0, key.indexOf('(')) + '(' + leetcode[key].length + ')'

    if (newName != key) {
        leetcode[newName] = leetcode[key]
        delete leetcode[key]
    }

});
console.log(leetcode)

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
// console.log(dic)

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

var sortByCompany = './sortByCompany.json';
fs.writeFile(sortByCompany, JSON.stringify(leetcode, null, 4), function(err) {
    if (err) {
        console.log(err);
    } else {
        console.log("JSON saved to: " + sortByCompany);
    }
});

var sortByFrequency = './sortByFrequency.json';
fs.writeFile(sortByFrequency, JSON.stringify(result, null, 4), function(err) {
    if (err) {
        console.log(err);
    } else {
        console.log("JSON saved to: " + sortByFrequency);
    }
});

var fs = require('fs');
var stream = fs.createWriteStream("PROBLEMS.txt");
stream.once('open', function(fd) {

    keys = Object.keys(leetcode)
    keys.sort()
    console.log(keys);
    for (i = 0; i < keys.length; i++) {
        key = keys[i]
        var val = leetcode[key];

        for (j = 0; j < leetcode[key].length; j++) {
            stream.write(key + ": " + leetcode[key][j] + "\n");
        }

        stream.write("\n\n");

    }
    // Object.keys(leetcode).forEach(function(key) {
    //     var val = leetcode[key];
    //     for (i = 0; i < leetcode[key].length; i++) {
    //         stream.write(key + ": " + leetcode[key][i] + "\n");
    //     }

    //     stream.write("\n\n");

    // });
    stream.end();

});

console.log(items.length);