#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int num;
	cin >> num;
	vector <int> time(num);
	int tTime=0;
	int temp = 0;

	for (int i = 0; i < num; i++) {
		cin >> time[i];
	}
	sort(time.begin(), time.end());

	for (int i = 0; i < num; i++) {
		tTime += temp + time[i];
		temp += time[i];
	}

	cout << tTime;


	return 0;

}