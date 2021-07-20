#include <iostream>

using namespace std;

void Hanoi(int n, char from, char by, char to) {
    if (n == 1) { //재귀함수 탈출 조건 마지막에 남은 원판개수가 1일때 이를 목적지로 옮긴다
        cout << n << " 이 " << from << " 에서 " << to << " 로이동" << endl;
    }
    else{
    Hanoi(n - 1, from, to, by);
    cout << n << " 이 " << from << " 에서 " << to << " 로 이동" << endl;
    Hanoi(n - 1, by, from, to);
    }
}

int main() {
    Hanoi(3, 'a', 'b', 'c');
    return 0;
}