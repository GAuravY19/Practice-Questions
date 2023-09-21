#include<iostream>
using namespace std;

class Employee{
    int id;
    static int count;
    public:
        void SetData(void){
            cout<<"Enter the id"<<endl;
            cin>>id;
            count++;
        }

        void GetData(void){
            cout<<"Your Employee Id is "<<id<<" and this is employee id count "<<count<<endl;
        }

        static void getCount(void){
            cout<<"The value of count is "<<count<<endl;
        }
};

int Employee :: count;


int main(){
    Employee harry, john, garry;
    harry.SetData();
    harry.GetData();
    Employee :: getCount();

    john.SetData();
    john.GetData();
    Employee :: getCount();

    garry.SetData();
    garry.GetData();
    Employee :: getCount();

    return 0;
}
