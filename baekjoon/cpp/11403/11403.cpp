#include <bits/stdc++.h>
using namespace std;

vector<int> graph[101];
vector<int> result[101];
vector<bool> visited(101, false);
void dfs(int src, int dst)
{
    // src로 출발해서 dst로 도착하면 ok
    vector<int> s;
    s.push_back(src);
    while (!s.empty())
    {
        int out = s.back();
        s.pop_back();
        if (!visited[out])
        {
            for (int &elem : graph[out])
            {
                if (elem == dst)
                {
                    result[src][dst] = 1;
                }
                s.push_back(elem);
                visited[out] = true;
            }
        }
    }
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("11403_input.txt", "r", stdin);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            int temp;
            cin >> temp;
            if (temp == 1)
                graph[i].push_back(j);
            result[i].push_back(0);
        }
    }

    // for (int i = 0; i < n; i++)
    // {
    //     for (int &elem : graph[i])
    //     {
    //         cout << elem << " ";
    //     }
    //     cout << "\n";
    // }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            dfs(i, j);
            fill(visited.begin(), visited.end(), false);
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int &elem : result[i])
        {
            cout << elem << " ";
        }
        cout << "\n";
    }
    return 0;
}
