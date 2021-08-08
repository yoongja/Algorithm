#include <string>
#include <iostream>
using namespace std;
 
bool solution(string s)
{
    int pCnt = 0;
    int yCnt = 0;
    for(int i = 0; i < s.size(); i++)
    {
        if(s[i] == 'P' || s[i] == 'p')
        {
            pCnt++;
        }
        else if(s[i] == 'Y' || s[i] == 'y')
        {
            yCnt++;
        }
    }
    
    if(pCnt == yCnt)
    {
        return true;
    }
    else
    {
        return false;
    }
}