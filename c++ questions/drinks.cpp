#include<iostream>
using namespace std;

int main(){
    int long n;
    cin>>n;

    float a[n];
    float sum = 0;

    for(int i = 0; i<n;i++){
        cin>>a[i];
    }

    for(int i = 0;i<n;i++){
        sum += a[i];
    }
    float result = sum / n;
    cout<<result<<endl;
    return 0;
}
