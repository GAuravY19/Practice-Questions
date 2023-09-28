#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;

    for(int i = 0;i<t;i++){
        int n;
        cin>>n;

        int rem = n/2020;
        if (rem<1){
            cout<<"NO"<<endl;
        } else{
            int lastdigit = n%2020;
            if (lastdigit > rem){
                cout<<"NO"<<endl;
            }
            else{
                cout<<"YES"<<endl;
            }
        }
    }
    return 0;
}
