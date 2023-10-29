#include <vector>
#include <iostream>
#include <queue>
#include <cstring>
#include <algorithm>
using namespace std;

int n, m, v;

vector<int> graph[1001];
bool visited[1001] = {
    false,
};

void dfs(int v)
{
    if (!visited[v])
    {
        visited[v] = true;
        cout << v << " ";
        for (auto &elem : graph[v])
        {
            dfs(elem);
        }
    }
}
void bfs(int v)
{
    queue<int> q;
    q.push(v);
    cout << v << " ";
    visited[v] = true;
    while (!q.empty())
    {
        int out = q.front();
        q.pop();
        for (auto &elem : graph[out])
        {
            if (!visited[elem])
            {
                visited[elem] = true;
                cout << elem << " ";
                q.push(elem);
            }
        }
    }
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("1200_input.txt", "r", stdin);

    cin >> n >> m >> v;

    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for (int i = 1; i <= n; i++)
    {
        sort(graph[i].begin(), graph[i].end(), less<int>());
        // for (auto &elem : graph[i])
        // {
        //     cout << elem << " ";
        // }
        // cout << "\n";
    }
    // cout << "\n";

    dfs(v);
    cout << endl;
    memset(visited, false, n + 1);
    bfs(v);
    cout << endl;

    return 0;
}
