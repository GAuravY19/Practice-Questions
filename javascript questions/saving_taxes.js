const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('', (T) =>{
    T = parseInt(T)

    const Taxes = () =>{
        r1.question('', (TestCase) =>{
            const [X,Y] = TestCase.split(" ").map(Number)

            console.log(Math.abs(X - Y))

            if (--T > 0){
                Taxes()
            } else{
                r1.close()
            }
        })
    }

    Taxes();
})
