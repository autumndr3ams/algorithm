#include <iostream>
#include <vector>
using namespace std;

bool dictionary(vector<int> &v, int n);
int main() {
	int n;
	cin >> n;
	vector<int> v(n); //0으로 초기화 된 n개의 원소를 가지는 vector

	for (int i = 0; i < n; i++) {
		cin >> v[i];
	}

	if (dictionary(v, n)) {
		for (int i = 0; i < n; i++) {
			cout << v[i] << ' ';
		}
		cout << '\n';
	}
	else cout << -1 << '\n';

	return 0;
}

bool dictionary(vector<int> &v, int n) {
	int a = n - 1; //주의! n은 idx보다 하나 크다
	while (a > 0 && v[a - 1] >= v[a])a--; //뒤에서부터 어디까지 내림차순인지 찾기
	//while문을 빠져나왔을 때 a가 내림차순 시작하는 부분
	if (a <= 0) return false; //오름차순인 경우

	int b = n - 1;
	while (v[b] <= v[a - 1])b--; //내림차순이 시작하는 a 인덱스보다 하나 앞의 숫자보다 처음으로 큰 b 찾기
	swap(v[a - 1], v[b]); //둘을 바꾸어줌
	b = n - 1; //순열의 마지막 자리
	while (a < b) { // 내림차순의 시작부분부터 마지막 자리까지 뒤집어준다
		swap(v[a], v[b]);
		a += 1;
		b -= 1;
	}
	return true;



}