#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;


    for(int i = 0; i<n;i++){
        int x,y;
        int count = 0;
        cin>>x>>y;

        int arr[x];

        for(int j = 0 ;j < x; j++){
            cin>>arr[j];

            if (arr[j] > y){
                count++;
            }
        }
        cout<<count<<endl;
    }
    return 0;
}
