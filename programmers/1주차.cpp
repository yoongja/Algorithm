using namespace std;

long long solution(int price, int money, int count)
{
    long long  answer = -1;
    long long  pay=0;
    for(int i=1;i<=count;i++){
        pay += price*i;
    }
    
    if(money>=pay){
        answer = 0;
    }
    else{
        answer = pay-money;
    }
    return answer;
}