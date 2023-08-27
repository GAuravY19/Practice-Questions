const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('', (N) =>{
    N =parseInt(N)

    if (N >=6 && (N <=8)){
        console.log('YES')
    } else{
        console.log('NO')
    }

    r1.close()
})
