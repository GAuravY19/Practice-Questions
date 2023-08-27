const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('', (T) =>{
    T = parseInt(T)

    const FitNess = () =>{
        r1.question('', (TestCase) =>{
            x = parseInt(TestCase)

            console.log(x*2*5)

            if (--T > 0){
                FitNess()
            } else{
                r1.close()
            }
        })
    }

    FitNess()
})
