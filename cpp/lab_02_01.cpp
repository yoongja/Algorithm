#include <iostream>

using namespace std;

void sum (int,int);
void sub (int,int);
void mult (int,int);
void idiv (int,int);

int main(){
    int x,y;
    cout<<"x입력 : ";
    cin>>x;
    cout<<"y입력 : ";
    cin>>y;
    sum(x,y);
    sub(x,y);
    mult(x,y);
    idiv(x,y);

    return 0;
}

void sum(int x, int y){
    int sum = x + y;
    cout<<sum;
}
void sub(int x, int y ){
    int sub = x - y;
    cout<<sub;
}
void mult(int x, int y){
    int mul = x * y;
    cout<<mul;
}
void idiv(int x, int y){
    float div = x / y;
    cout<<div;
}