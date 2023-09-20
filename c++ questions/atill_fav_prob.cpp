#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;

    for(int i=0;i<t;i++){
        int n;
        cin>>n;

        string s;
        cin>>s;

        char alphabet[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

        sort(s.begin(), s.end());

        char place = s[n-1];

        for(int j=0;j<26;j++){
            if (alphabet[j] == place){
                cout<<j+1<<endl;
                break;
            }
        }
    }
    return 0;
}
