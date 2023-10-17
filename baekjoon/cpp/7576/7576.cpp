#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int m, n;
vector<int> graph[1001];
bool visited[1001][1001] = {
    false,
};

queue<pair<int, int>> pos_tomatos;

void bfs()
{
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};

    while (!pos_tomatos.empty())
    {
        int x = pos_tomatos.front().first;
        int y = pos_tomatos.front().second;
        pos_tomatos.pop();

        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (0 <= nx && nx < n && 0 <= ny && ny < m)
            {
                if (!visited[nx][ny] && graph[nx][ny] == 0)
                {
                    visited[nx][ny] = true;
                    graph[nx][ny] = graph[x][y] + 1;
                    pos_tomatos.push({nx, ny});
                }
            }
        }
    }
}
int main()
{
    //. 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("7576_input.txt", "r", stdin);

    cin >> m >> n;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            int temp;
            cin >> temp;
            graph[i].push_back(temp);
            if (temp == 1)
            {
                pos_tomatos.push({i, j});
                // visited[i][j] = true;
            }
        }
    }

    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < m; j++)
    //     {
    //         cout << graph[i][j] << " ";
    //     }
    //     cout << "\n";
    // }
    // cout << "\n";
    bfs();
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < m; j++)
    //     {
    //         cout << graph[i][j] << " ";
    //     }
    //     cout << "\n";
    // }

    int M = 0;

    for (int i = 0; i < n; i++)
    {
        int CMP_M = *max_element(graph[i].begin(), graph[i].end());
        M = M > CMP_M ? M : CMP_M;
        auto it = find(graph[i].begin(), graph[i].end(), 0);
        if (it != graph[i].end())
        {
            cout << -1 << "\n";
            return 0;
        }
    }
    cout << M - 1 << "\n";

    return 0;
}
