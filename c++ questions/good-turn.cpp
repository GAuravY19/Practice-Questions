#include<iostream>
using namespace std;

int main(){
    int n,x,y;
    cin>>n;

    for(int i = 0; i<n; i++){
        cin>>x>>y;

        if ((x + y) > 6){
            cout<<"Yes"<<endl;
        }
        else{
            cout<<"No"<<endl;
        }
    }

    return 0;
}
