const { parse } = require('path')
const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})


r1.question('', (TestCase) =>{
    TestCase = parseInt(TestCase)

    const FourTickets = () =>{
        r1.question('', (X) =>{
            const [x] = parseInt(X)
        if ((x * 4) > 100){
            console.log('YES')
        } else{
            console.log('NO')
        }

        if (--T > 0){
            FourTickets()
        } else{
            r1.close()
        }
    })
    }

    FourTickets()
})
