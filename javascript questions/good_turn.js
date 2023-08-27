// your code goes here
const readline = require('readline');

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('', (T) =>{
    T = parseInt(T);

    const isSumGood = () => {
        r1.question('', (TestCase) => {
            const [X, Y] = TestCase.split(" ").map(Number);

            if(X + Y > 6){
                console.log("YES")
            } else{
                console.log("NO")
            }

            if(--T > 0){
                isSumGood();
            } else{
                r1.close();
            }
        })
    }

    isSumGood();
})
