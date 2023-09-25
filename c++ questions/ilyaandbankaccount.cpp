#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;

    int last = n%10;
    int lastdigit = n/10;

    if (n < 0){
        int seclastdigit = (lastdigit - (lastdigit%10)) + last ;
        if (lastdigit < seclastdigit){
            cout<<seclastdigit<<endl;
        }
        else{
            cout<<lastdigit<<endl;
        }
    }
    else{
        cout<<n<<endl;
    }


    return 0;
}
