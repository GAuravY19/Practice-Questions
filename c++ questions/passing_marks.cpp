#include<iostream>
using namespace std;
#include<algorithm>

int main(){
    int t;
    cin>>t;

    for(int i=0;i<t;i++){
        int n,x;
        cin>>n>>x;

        int a[n];
        for(int j = 0;j<n;j++){
            cin>>a[i];
        }

        sort(a, a+n);
        cout<<a[n-x] - 1<<endl;
    }
    return 0;
}
