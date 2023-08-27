const readline = require('readline')
const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
})

r1.on('line', (line) => {
    console.log(typeof line)
    r1.close();
})







// let input = ''

// process.stdin.on('data', function(chunk) {
//     input += chunk
// })

// process.stdin.on('end', function() {
//     console.log(input)
// })
