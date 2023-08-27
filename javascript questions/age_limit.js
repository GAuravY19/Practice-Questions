const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('', (T) =>{
    T = parseInt(T)

    const AgeLimit = () => {
        r1.question('', (TestCase) => {
            const [X,Y,A] = TestCase.split(" ").map(Number)

            if ((A >= X) && (A < Y)){
                console.log("YES")
            } else{
                console.log("NO")
            }

            if (--T >0){
                AgeLimit();
            } else{
                r1.close()
            }

        })
    }

    AgeLimit();
})

