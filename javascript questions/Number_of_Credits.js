const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('', (T)=>{
    T = parseInt(T)

    const CreditScore = () =>{
        r1.question('', (TestCase)=>{
            const [x,y,z] = TestCase.split(" ").map(Number)

            console.log((4 * x) + (2 * y))

            if (--T > 0){
                CreditScore()
            } else{
                r1.close()
            }

        })
    }

    CreditScore()
})
