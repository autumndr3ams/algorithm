#include <iostream>
#include <vector>
using namespace std;

bool dictionary(vector<int> &v, int n);
int main() {
	int n;
	cin >> n;
	vector<int> v(n); //0���� �ʱ�ȭ �� n���� ���Ҹ� ������ vector

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
	int a = n - 1; //����! n�� idx���� �ϳ� ũ��
	while (a > 0 && v[a - 1] >= v[a])a--; //�ڿ������� ������ ������������ ã��
	//while���� ���������� �� a�� �������� �����ϴ� �κ�
	if (a <= 0) return false; //���������� ���

	int b = n - 1;
	while (v[b] <= v[a - 1])b--; //���������� �����ϴ� a �ε������� �ϳ� ���� ���ں��� ó������ ū b ã��
	swap(v[a - 1], v[b]); //���� �ٲپ���
	b = n - 1; //������ ������ �ڸ�
	while (a < b) { // ���������� ���ۺκк��� ������ �ڸ����� �������ش�
		swap(v[a], v[b]);
		a += 1;
		b -= 1;
	}
	return true;



}