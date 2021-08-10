#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(string s) {
    int answer = 0;
    
    if(s[0]=='-'){
        for(int i = 1; i<s.size();i++){
        answer+=s[i]*pow(10,(s.size()-i-1));
        }
     answer= -answer  ;
    }
    
    else{
    for(int i = 0; i<s.size();i++){
        answer+=s[i]*pow(10,(s.size()-i-1));
         }
    }
   
    return answer;
}

//간단한데 완전 다르다 함수 구현말고 다시 풀어보기