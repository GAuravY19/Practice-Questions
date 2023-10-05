#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main(){
    int n;
    cin>>n;

    string s;
    cin>>s;

    int zer = count(s.begin(), s.end(), '0');
    int one = count(s.begin(), s.end(), '1');

    cout<<n-(2*min(zer, one))<<endl;

    return 0;
}
