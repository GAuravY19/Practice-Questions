const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('', (T) =>{
    T = parseInt(T)

    const Tax = () =>{
        r1.question('', (TEstCase) =>{
            const x = parseInt(TEstCase)

            if (x > 100){
                console.log(x-10)
            } else{
                console.log(x)
            }

            if (--T > 0){
                Tax()
            } else{
                r1.close()
            }
        })
    }

    Tax()
})
