const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('', (T) =>{
    T = parseInt(T)

    const Squats = () =>{
        r1.question('', (TestCase) =>{
            TestCase = parseInt(TestCase)

            console.log(15 * TestCase)

            if (--T > 0) {
                Squats()
            } else{
                r1.close()
            }
        })
    }

    Squats();
})
