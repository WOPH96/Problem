#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, m;

vector<int> graph[1001];
bool visited[1001][1001] = {
    false,
};

void bfs(queue<pair<int, int>> &q)
{
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
            if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny] && graph[nx][ny] != -1)
            {
                if (!graph[nx][ny])
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
    freopen("7576_input.txt", "r", stdin);

    cin >> m >> n;
    int tmp;
    queue<pair<int, int>> tom_q;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> tmp;
            graph[i].push_back(tmp);
            if (tmp == 1)
            {
                tom_q.push({i, j});
                visited[i][j] = true;
            }
        }
    }

    // while (!tom_q.empty())
    // {
    //     cout << tom_q.front().first << "," << tom_q.front().second << endl;
    //     tom_q.pop();
    // }

    // for (int i = 0; i < n; i++)
    // {
    //     for (const auto &elem : graph[i])
    //     {
    //         cout << elem << " ";
    //     }
    //     cout << endl;
    // }

    bfs(tom_q);

    int max = -1;
    for (int i = 0; i < n; i++)
    {
        if (find(graph[i].begin(), graph[i].end(), 0) != graph[i].end())
        {
            cout << -1 << endl;
            return 0;
        }
        int linemax = *max_element(graph[i].begin(), graph[i].end());

        if (linemax > max)
            max = linemax;

        // for (const auto &elem : graph[i])
        // {
        //     cout << elem << " ";
        // }
        // cout << endl;
    }
    cout << max - 1 << endl;
    // cout << graph[n - 1][m - 1] << endl;
    return 0;
}
