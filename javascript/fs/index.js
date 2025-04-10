const path = require('path');
const fs = require('fs')

const filePath = path.join(__dirname, 'test.txt');
console.log(filePath);
const data = fs.readFile(filePath, 'utf-8', (err, data) => {
    if(err){
        console.log(`Error: ${err}`)
    }
    else{
        console.log(data);
    }
});