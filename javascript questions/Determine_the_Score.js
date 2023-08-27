const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('', (T) =>{
    T = parseInt(T)

    const Score = () =>{
        r1.question('', (TestCase) =>{
            const [X,N] = TestCase.split(" ").map(Number)

            Marks = Math.abs(X/10)

            console.log(Marks * N)

            if (--T > 0){
                Score()
            } else{
                r1.close()
            }

        })
    }

    Score()
})

