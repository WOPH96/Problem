#include <bits/stdc++.h>
using namespace std;
vector<int> graph[1001];
bool visited[1001] = {
    false,
};

vector<int> res_bfs;
vector<int> res_dfs;
void bfs(int node)
{
    queue<int> q;
    q.push(node);
    visited[node] = true;
    while (!q.empty())
    {
        int out = q.front();
        q.pop();
        res_bfs.push_back(out);
        for (const auto &elem : graph[out])
        {
            if (!visited[elem])
            {
                visited[elem] = true;
                q.push(elem);
            }
        }
    }
}
void dfs(int node)
{
    visited[node] = true;
    res_dfs.push_back(node);
    for (const auto &elem : graph[node])
    {
        if (!visited[elem])
        {
            dfs(elem);
        }
    }
}
// int dfs_rcs(int node)
// {
//     if (visited[node])
//         return false;
//     else
//     {
//         visited[node] = true;
//         cout << node << " ";
//         for (int &elem : graph[node])
//         {
//             dfs_rcs(elem);
//         }
//         return true;
//     }
// }
// void dfs_stack(int node)
// {
//     vector<int> s;
//     s.push_back(node);
//     // visited[node] = true;
//     // cout << node << " ";
//     while (!s.empty())
//     {
//         int out = s.back();
//         s.pop_back();
//         if (!visited[out])
//         {
//             visited[out] = true;
//             cout << out << " ";
//             for (int i = graph[out].size() - 1; i != -1; --i)
//             {
//                 int &elem = graph[out][i];
//                 s.push_back(elem);
//             }
//         }
//     }
//     cout << endl;
// }

int main()
{
    std::ios_base::sync_with_stdio(false);
    freopen("1260_input.txt", "r", stdin);

    int n, m, v;
    cin >> n >> m >> v;
    // cout << n << m << v << endl;
    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for (int i = 1; i <= n; i++)
    {
        sort(graph[i].begin(), graph[i].end());
    }

    // for (int i = 1; i <= n; i++)
    // {
    //     cout << i << " : ";
    //     for (auto &elem : graph[i])
    //     {
    //         cout << elem << " ";
    //     }
    //     cout << endl;
    //     // cout << graph[i].size() << endl;
    // }
    // dfs_stack(v);
    // memset(visited, false, sizeof(visited));
    // dfs_rcs(v);
    // cout << endl;
    dfs(v);
    memset(visited, false, sizeof(visited));
    bfs(v);
    for (const auto &elem : res_dfs)
    {
        cout << elem << " ";
    }
    cout << endl;
    for (const auto &elem : res_bfs)
    {
        cout << elem << " ";
    }
    cout << endl;
    // cout << visited[0] << endl;

    // cout << visited[0] << endl;
    return 0;
}
