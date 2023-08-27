const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('', (T) =>{
    T = parseInt(T)

    const WaterConsumption = () =>{
        r1.question('', (X) =>{
            X = parseInt(X)

            if (X >= 2000){
                console.log('YES')
            } else{
                console.log('NO')
            }

            if (--T > 0){
                WaterConsumption();
            } else{
                r1.close()
            }
        })
    }

    WaterConsumption();
})
