#include <iostream>
using namespace std;

int recur(int t) {
	if (t == 1) return 1;
	else if (t == 2) return 2;
	else if (t == 3) return 4;
	else return recur(t - 3) + recur(t - 2) + recur(t - 1);
}
int main() {
	int n, t;
	int list[11];
	cin >> n;
	
	for (int i = 0; i < n; i++) {
		cin >> t;
		list[i] = t;
	}
	for(int i=0;i<n;i++) cout << recur(list[i]) << "\n";

	return 0;
}

