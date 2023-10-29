#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, m;

vector<int> graph[101];
bool visited[101][101] = {
    false,
};

void bfs(int sx, int sy)
{
    queue<pair<int, int>> q;
    q.push({sx, sy});
    visited[sx][sy] = true;

    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};
    int nx, ny;
    while (!q.empty())
    {
        int x, y;
        x = q.front().first;
        y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            nx = x + dx[i];
            ny = y + dy[i];
            if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny])
            {
                if (graph[nx][ny])
                {
                    visited[nx][ny] = true;
                    graph[nx][ny] = graph[x][y] + 1;
                    q.push({nx, ny});
                }
            }
        }
    }
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("2178_input.txt", "r", stdin);

    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        string tmp;
        cin >> tmp;
        for (const auto &elem : tmp)
        {
            graph[i].push_back(elem - '0');
        }
    }
    // for (int i = 0; i < n; i++)
    // {
    //     for (const auto &elem : graph[i])
    //     {
    //         cout << elem << " ";
    //     }
    //     cout << endl;
    // }

    bfs(0, 0);

    // for (int i = 0; i < n; i++)
    // {
    //     for (const auto &elem : graph[i])
    //     {
    //         cout << elem << " ";
    //     }
    //     cout << endl;
    // }
    cout << graph[n - 1][m - 1] << endl;
    return 0;
}
