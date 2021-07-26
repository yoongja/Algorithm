#include <iostream>
using namespace std;
void star(int row, int col, int num)
{
    if ((row / num) % 3 == 1 && (col / num) % 3 == 1) {
        cout << ' '; // num이 9일때 공백인곳 (3,3)(3,4)(3,5)(4,3)(4,4)(4,5)(5,3)(5,4)(5,5)을 생각해서 규칙,num이 3일때는 밑에 else후 num/3해서 이해
    }
    else
    {
        if (num / 3 == 0)
            cout << '*';
        else
            star(row, col, num / 3); //*찍혀야 하는곳인 (3,2,27)을 생각해보면 num/3을 계속해서 num을 줄여나간후 *을 찍어냄
    }
}
int main() {
    int num;
    cin >> num;
    for (int row = 0; row < num; row++)
    {
        for (int col = 0; col < num; col++)
            star(row, col, num);
        cout << '\n';
    }
}