#include <iostream>

using namespace std;

int swap_call_by_value(int,int);
int swap_call_by_reference(int&,int&);

int main(){
    int x,y;
    cout<<"x 입력 : ";
    cin>>x;
    cout<<"y 입력 : ";
    cin>>y;

    cout<<"swap_call_by_value 함수 사용 전"<<endl<<"x = "<<x<<", y ="<<y<<endl;
    swap_call_by_value(x,y);
    cout<<"swap_call_by_value 함수 사용 후"<<endl<<"x = "<<x<<", y ="<<y<<endl<<endl;
    cout<<"swap_call_by_reference 함수 사용 전"<<endl<<"x = "<<x<<", y ="<<y<<endl;
    swap_call_by_reference(&x,&y);
    cout<<"swap_call_by_reference 함수 사용 후"<<endl<<"x = "<<x<<", y ="<<y;
    return 0;
}
int swap_call_by_value(int x,int y){
    int temp;
    temp = x;
    x = y;
    y = temp;
    return x,y;
}
int swap_call_by_reference(int& x,int& y){
    int temp;
    temp = x;
    x = y;
    y = temp;
    return x,y;
}