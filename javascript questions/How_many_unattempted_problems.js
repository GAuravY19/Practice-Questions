const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('', (T) =>{
    const [X,Y] = T.split(" ").map(Number)

    console.log(X - Y)

    r1.close()

})
