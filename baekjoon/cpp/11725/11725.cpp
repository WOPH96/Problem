#include <bits/stdc++.h>
using namespace std;

vector<int> graph[100001];
vector<int> parents(100001, 0);
vector<bool> visited(100001, false);
void bfs(int start_node)
{
    queue<int> q;
    q.push(start_node);
    visited[start_node] = true;
    while (!q.empty())
    {
        int out = q.front();
        q.pop();
        for (auto &elem : graph[out])
        {
            if (!visited[elem])
            {
                visited[elem] = true;
                parents[elem] = out;
                q.push(elem);
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

    // for (int i = 1; i <= n; i++)
    // {
    //     for (int &elem : graph[i])
    //     {
    //         cout << elem << " ";
    //     }
    //     cout << endl;
    // }

    bfs(1);

    for (int i = 2; i <= n; i++)
    {
        cout << parents[i] << "\n";
        }

    return 0;
}
