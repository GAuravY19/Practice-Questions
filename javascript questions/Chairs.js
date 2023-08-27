// your code goes here
const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('', (TestCase)=>{
    T = parseInt(TestCase)

    const Chairs = () =>{
        r1.question('', (NewCase) =>{
            const [x,y] = NewCase.split(' ').map(Number)

            ch = x - y
            if (ch > 0){
                console.log(ch)
            } else{
                console.log(0)
            }

            if (--T > 0){
                Chairs()
            } else{
                r1.close()
            }
        })
    }

    Chairs()
})

