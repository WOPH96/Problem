#include <bits/stdc++.h>
using namespace std;

vector<int> graph[26];
vector<bool> visited[26];
vector<int> homes;
int line;
bool bfs(int sx, int sy)
{
    if (graph[sx][sy] == 0 || visited[sx][sy] == 1)
        return false;
    queue<pair<int, int>> q;
    q.push({sx, sy});
    int home = 1;
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};
    visited[sx][sy] = true;
    while (!q.empty())
    {
        int x, y;
        x = q.front().first;
        y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < line && 0 <= ny && ny < line)
            {
                if (!visited[nx][ny] && graph[nx][ny])
                {
                    home++;
                    visited[nx][ny] = true;
                    q.push({nx, ny});
                }
            }
        }
    }
    homes.push_back(home);

    return true;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    freopen("2667_input.txt", "r", stdin);

    cin >> line;

    for (int i = 0; i < line; i++)
    {
        string homes;
        cin >> homes;
        for (auto &elem : homes)
        {
            graph[i].push_back(elem - '0');
            visited[i].push_back(false);
        }
        // fill(visited[i].begin(), visited[i].begin() + line, 0);
    }

    // for (int i = 0; i < line; i++)
    // {
    //     for (auto &elem : graph[i])
    //     {
    //         cout << elem << " ";
    //     }
    //     cout << "\t";
    //     for (auto elem : visited[i])
    //     {
    //         cout << elem << " ";
    //     }
    //     cout << endl;
    // }
    int danzi = 0;
    for (int i = 0; i < line; i++)
    {
        for (int j = 0; j < line; j++)
        {
            if (bfs(i, j) == true)
            {
                danzi++;
            }
        }
    }
    cout << danzi << endl;
    sort(homes.begin(), homes.end(), less<int>());
    for (auto &elem : homes)
    {
        cout << elem << endl;
    }

    // for (int i = 0; i < line; i++)
    // {
    //     for (auto &elem : graph[i])
    //     {
    //         cout << elem << " ";
    //     }
    //     cout << "\t";
    //     for (auto elem : visited[i])
    //     {
    //         cout << elem << " ";
    //     }
    //     cout << endl;
    // }
    return 0;
}
