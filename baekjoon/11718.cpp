#include <iostream>
#include <string>

using namespace std;

int main() {
	//getline 함수는 입력 스트림에서 문자들을 읽어서, 인자로 받은 문자열에 저장합니다.
	//string의 getline함수는 string을 받을 수 있다.
	/*
	string str1; 
	string str2; 
	ifstream inf("test.txt"); 
	getline(inf,str1); //파일 입출력 
	getline(cin,str2); //표준 입출력
	*/

	string name;
	while(1){
	getline(cin, name);
	if (name == "") //입력받는 문자열이 없을 때 멈춤
		break;
	cout << name<<endl;
	}
    return 0;
}