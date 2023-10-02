#include<iostream>
using namespace std;

int main(){
    int n, m;
    cin>>n>>m;

    for(int i=1;i<n+1;i++){
        if ((i*m) <= n){
            n += 1;
        }
    }

    cout<<n;
    return 0;
}
