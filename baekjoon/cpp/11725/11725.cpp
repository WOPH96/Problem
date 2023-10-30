#include <bits/stdc++.h>
using namespace std;
vector<int> graph[100001];
bool visited[100001] = {
    false,
};
int parent[100001] = {
    0,
};

void bfs()
{
    queue<int> q;
    q.push(1);
    visited[1] = true;
    while (!q.empty())
    {
        int out = q.front();
        q.pop();
        for (auto &elem : graph[out])
        {
            if (!visited[elem])
            {
                parent[elem] = out;
                visited
            }
        }
    }
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("11725_input.txt", "r", stdin);

    int n;
    cin >> n;
    for (int i = 1; i < n; i++)
    {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    for (int i = 1; i <= n; i++)
    {
        for (auto &elem : graph[i])
        {
            cout << elem << " ";
        }
        cout << endl;
    }
    bfs();
    return 0;
}
