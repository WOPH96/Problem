// #include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<int> graph[101];
bool visited[101] = {
    false,
};
int com, load;

int virus = 0;

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
                q.push(elem);
                visited[elem] = true;
                virus++;
            }
        }
        // 처음 뽑은건 무조건 방문안했으니 그냥 진행
    }
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    freopen("2606_input.txt", "r", stdin);

    cin >> com;
    cin >> load;

    for (int i = 0; i < load; i++)
    {
        int a, b;
        cin >> a >> b;
        // cout << a << b << endl;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    // for (int i = 1; i <= com; i++)
    // {
    //     for (auto &elem : graph[i])
    //     {
    //         cout << elem << " ";
    //     }
    //     cout << "\t" << visited[i] << endl;
    // }

    bfs(1);
    cout << virus << endl;
    return 0;
}
