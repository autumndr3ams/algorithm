#include <iostream>
#include <vector>
using namespace std;

#define MAX_SIZE 1001
vector<int> graph[MAX_SIZE];
bool visited[MAX_SIZE];

void dfs(int start);

int main() {
	int n, m; //������ ����, ������ ����
	cin >> n >> m;
	
	//������ ����
	for (int i = 0; i < m; i++) {
		int u, v;
		cin >> u >> v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}

	/*�湮���� ���� �����鿡 ���� 
	dfs�� Ž���ϸ� �� ������ ����� ��� ������ �湮, 
	visited�� üũ���ش�*/
	int cnt = 0;
	for (int i = 1; i <= n; i++) {
		if (!visited[i]) {
			cnt++;
			dfs(i);
		}
	}
	cout << cnt;
	return 0;
}

void dfs(int start) {
	visited[start] = true;
	for (int i = 0; i < graph[start].size(); i++) {
		int next = graph[start][i];
		if (!visited[next]) dfs(next);
	}
}