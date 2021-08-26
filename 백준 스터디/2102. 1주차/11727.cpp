#include <iostream>
using namespace std;

int arr[1001] = { 0, };

int recur(int n);
int main() {
	int n, result;
	cin >> n;

	result = recur(n);
	cout << result;
	return 0;
}

int recur(int n) {
	arr[1] = 1;
	arr[2] = 3;
	for (int i = 3; i <= n; i++) {
		arr[i] = (arr[i - 1] + 2 * arr[i - 2]) % 10007;
	}
	return arr[n];
}