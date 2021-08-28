#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    string number = to_string(n);
    sort(number.rbegin(), number.rend()); // 내림 차순 정렬
    
    for(int i = 0; i < number.length(); i++)
        answer = answer * 10 + (number[i] - '0');
    
    return answer;
}