const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('',(T) =>{
    T = parseInt(T)

    const Burgers = () =>{
        r1.question('', (TestCase) =>{
            const [X,Y] = TestCase.split(' ').map(Number)

            console.log(Math.min(X,Y))

            if (--T > 0){
                Burgers()
            } else{
                r1.close()
            }
        })
    }

    Burgers()
})


