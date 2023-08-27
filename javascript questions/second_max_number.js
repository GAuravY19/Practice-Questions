const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('', (T)=>{
    T = parseInt(T)

    const SecondMaxNumber = () =>{
        r1.question('', (TestCase) =>{
            const [x,y,z] = TestCase.split(" ").map(Number)

            if (((x > z) && (x < y)) || ((x > y) && (x < z))){
                console.log(x)
            } else if ((y > x) &&  (y < z) || (y > z) && (y < x)){
                console.log(y)
            } else if ((z > y) &&  (z < x) || (z > x) && (z < y)){
                console.log(z)
            }

            if (--T > 0){
                SecondMaxNumber()
            } else{
                r1.close()
            }
        })
    }

    SecondMaxNumber()
})
