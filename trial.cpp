#include<iostream>
using namespace std;

class employee{
    private: int a, int b, int c;

    public: int d, int c;

    void setData(int a1, int b1, int c1);
    void getData(){
        cout<<a<<endl;
        cout<<b<<endl;
        cout<<c<<endl;
    }
};

void employee :: setData(int a1, int b1, int c1){
    a = a1;
    b = b1;
    c = c1;
}

int main(){
    employee harry;
    harry.setData(10,10,10);
    harry.d = 4;

    return 0;
}
