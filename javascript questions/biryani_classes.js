const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})


r1.question('', (T) =>{
    T = parseInt(T)

    const BiryaniClasses = () =>{
        r1.question('', (TestCase) =>{
            const [X,Y] = TestCase.split(" ").map(Number)

            console.log(X*Y)

            if (--T > 0){
                BiryaniClasses()
            } else{
                r1.close()
            }
        })
    }

    BiryaniClasses()
})
