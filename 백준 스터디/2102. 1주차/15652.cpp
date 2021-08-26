#include <iostream>
using namespace std;
#define MAX 8

int test[MAX];
int n, m;

void sequence(int cnt, int index) {
	//m과 길이가 같아지면 출력한다
	if (m == cnt) {
		for (int i = 0; i < m; i++) cout << test[i] << ' ';
		cout << '\n';
	}
	//아닌 경우 원소를 추가한다
	else {
		for (int i = index; i < n; i++) {
			test[cnt] = i+1;
			sequence(cnt+1,i);
		}
	}
}
int main() {
	cin >> n >> m;
	sequence(0, 0);
	return 0;
}