const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('', (T) =>{
    T = parseInt(T)

    const PlayLudo = () =>{
        r1.question('', (X) =>{
            X = parseInt(X)

            if (X == 6){
                console.log('YES')
            } else{
                console.log('NO')
            }

            if (--T > 0){
                PlayLudo()
            } else{
                r1.close()
            }
        })
    }

    PlayLudo()
})
