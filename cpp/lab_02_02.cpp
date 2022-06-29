#include <iostream>

using namespace std;
int sum (int,int);
int sub (int,int);
int mult (int,int);
float idiv (int,int);
void add_mult(int,int,int);
void mult_div(int,int,int);
void add_mult_add(int,int,int);
void sub_div_sub(int,int,int);

int main(){
    int x,y,z;
    cout<<"x입력 : ";
    cin>>x;
    cout<<"y입력 : ";
    cin>>y;
    cout<<"z입력 : ";
    cin>>z;
    add_mult(x,y,z);
    mult_div(x,y,z);
    add_mult_add(x,y,z);
    sub_div_sub(x,y,z);

    return 0;
}

int sum(int x, int y){
    int sum = x + y;
    return sum;
}
int sub(int x, int y ){
    int sub = x - y;
    return sub;
}
int mult(int x, int y){
    int mul = x * y;
    return mul;
}
float idiv(int x, int y){
    float div = x / y;
    return div;
}
void add_mult(int x,int y,int z){
    int add_mult = mult(mult(x,y),mult(y,z));
    cout<<"(x + y) * z = "<<add_mult<<endl;
}
void mult_div(int x,int y,int z){
    float mult_div = idiv(mult(x,y),z);
    cout<<"(x * y) / z = "<<mult_div<<endl;
}
void add_mult_add(int x,int y,int z){
    int add_mult_add = mult(sum(x,y),sum(y,z));
    cout<<"(x + y) * (y + z)"<<add_mult_add;
}
void sub_div_sub(int x,int y ,int z){
    float sub_div_sub = idiv(sub(x,y),sub(x,z));
}