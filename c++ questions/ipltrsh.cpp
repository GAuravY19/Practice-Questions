#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;

    for(int i = 0;i<t;i++){
        int n,m;
        cin>>n>>m;

        if (n>=m){
            cout<<n - m<<endl;
        }else{
            cout<<0<<endl;
        }
    }
}
