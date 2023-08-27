const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('', (T) =>{
    T = parseInt(T)

    const BullOrBear = () =>{
        r1.question('', (TestCase) =>{
            const [X,Y] = TestCase.split(" ").map(Number)

            if (X > Y){
                console.log('LOSS')
            } else if( X == Y){
                console.log('NEUTRAL')
            } else{
                console.log('PROFIT')
            }

            if (--T > 0){
                BullOrBear()
            } else{
                r1.close()
            }

        })
    }

    BullOrBear()
})
