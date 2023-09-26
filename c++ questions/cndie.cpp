#include<iostream>
using namespace std;

int main(){
    int t,x,n = 0;
    cin>>t;
    for(int i =0;i<t;i++){
        int n;
        cin>>n;
        for(int k = 2; k <= 35; k++){
            int den = 2*k - 1;

            if (n%den != 0){
                continue;
            }
            x = n/den;
            break;
    }

    cout<<x<<endl;}
    return 0;
}
