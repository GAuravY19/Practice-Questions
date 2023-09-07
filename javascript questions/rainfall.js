const readline = require('readline')

const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r.question('', (T) =>{
    T = parseInt(T)

    const RainFall = () =>{
        r.question('', (x) =>{
            let x = parseInt(x)

            if (x <= 3){
                console.log('Light')
            } else if ((x > 3) && (x <= 7)){
                console.log('Moderate')
            } else{
                console.log('heavy')
            }

            if (--T > 0){
                RainFall()
            } else{
                r.close()
            }

        })
    }

    RainFall()
})
