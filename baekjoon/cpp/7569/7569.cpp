#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int n, m, h;

int graph[101][101][101];
bool visited[101][101][101] = {
    false,
};

void bfs(queue<tuple<int, int, int>> &q)
{
    int dx[6] = {1, -1, 0, 0, 0, 0};
    int dy[6] = {0, 0, 1, -1, 0, 0};
    int dz[6] = {0, 0, 0, 0, -1, 1};
    int nx, ny, nz;
    while (!q.empty())
    {
        int x, y, z;
        tie(x, y, z) = q.front();
        q.pop();
        for (int i = 0; i < 6; i++)
        {
            nx = x + dx[i];
            ny = y + dy[i];
            nz = z + dz[i];
            if (0 <= nx && nx < n && 0 <= ny && ny < m && 0 <= nz && nz < h &&
                !visited[nx][ny][nz] && graph[nx][ny][nz] != -1)
            {
                if (!graph[nx][ny][nz])
                {
                    visited[nx][ny][nz] = true;
                    graph[nx][ny][nz] = graph[x][y][z] + 1;
                    q.push({nx, ny, nz});
                }
            }
        }
    }
}

int main()
{

    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("7569_input.txt", "r", stdin);

    cin >> m >> n >> h;
    int tmp;
    queue<tuple<int, int, int>> tom_q;
    for (int k = 0; k < h; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {

                cin >> tmp;
                graph[i][j][k] = tmp;
                if (tmp == 1)
                {
                    tom_q.push({i, j, k});
                    visited[i][j][k] = true;
                }
            }
        }
    }

    // while (!tom_q.empty())
    // {
    //     int x, y, z;
    //     tie(x, y, z) = tom_q.front();
    //     cout << x << "," << y << "," << z << endl;
    //     tom_q.pop();
    // }
    // for (int k = 0; k < h; k++)
    // {
    //     for (int i = 0; i < n; i++)
    //     {
    //         for (int j = 0; j < m; j++)
    //         {

    //             cout << graph[i][j][k] << " ";
    //         }
    //         cout << endl;
    //     }
    //     cout << endl;
    // }
    // cout << endl;

    bfs(tom_q);

    // for (int k = 0; k < h; k++)
    // {
    //     for (int i = 0; i < n; i++)
    //     {
    //         for (int j = 0; j < m; j++)
    //         {

    //             cout << graph[i][j][k] << " ";
    //         }
    //         cout << endl;
    //     }
    //     cout << endl;
    // }

    int max = -1;

    for (int k = 0; k < h; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {

                if (graph[i][j][k] == 0)
                {
                    cout << -1 << endl;
                    return 0;
                }
                else
                {
                    if (graph[i][j][k] > max)
                        max = graph[i][j][k];
                }

                // for (const auto &elem : graph[i])
                // {
                //     cout << elem << " ";
                // }
                // cout << endl;
            }
        }
    }
    cout << max - 1 << endl;
    return 0;
}
