#include <iostream>
#include <vector>
using namespace std;

#define MAX_SIZE 1001
vector<int> graph[MAX_SIZE];
bool visited[MAX_SIZE];

void dfs(int start);

int main() {
	int n, m; //정점의 개수, 간선의 개수
	cin >> n >> m;
	
	//간선의 연결
	for (int i = 0; i < m; i++) {
		int u, v;
		cin >> u >> v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}

	/*방문하지 않은 정점들에 대해 
	dfs로 탐색하며 그 정점과 연결된 모든 정점을 방문, 
	visited에 체크해준다*/
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