const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('', (T) =>{
    T = parseInt(T)

    const Top10 = () =>{
        r1.question('', (x) =>{
            x = parseInt(x)

            if (x <= 10){
                console.log('YES')
            } else{
                console.log('NO')
            }


            if (--T > 0){
                Top10()
            } else{
                r1.close()
            }
        })
    }

    Top10()
})
