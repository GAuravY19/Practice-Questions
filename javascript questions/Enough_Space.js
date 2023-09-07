const readline = require('readline')

const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r.question('', (T)=>{
    T = parseInt(T)

    const EnoughSpace = () =>{
        r.question('', (TestCase) =>{
            const [n,x,y] = TestCase.split(" ").map(Number)

            if (n >= (x + (y*2))){
                console.log('YES')
            } else{
                console.log('NO')
            }

            if (--T > 0){
                EnoughSpace()
            } else{
                r.close()
            }
        })
    }

    EnoughSpace()
})
