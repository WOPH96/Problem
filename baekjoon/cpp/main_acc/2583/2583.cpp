#include <bits/stdc++.h>
using namespace std;
int m, n, k;

int graph[101][101] = {
    0,
};

bool visited[101][101] = {
    false,
};

vector<int> areas;

bool bfs(int sx, int sy)
{
    if (graph[sx][sy] || visited[sx][sy])
        return false;
    queue<pair<int, int>> q;
    q.push({sx, sy});
    visited[sx][sy] = true;
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};
    int area = 1;
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
            if (0 <= nx && nx < m && 0 <= ny && ny < n &&
                graph[nx][ny] == 0 && !visited[nx][ny])
            {
                visited[nx][ny] = true;
                q.push({nx, ny});
                area++;
            }
        }
    }
    areas.push_back(area);
    return true;
}

void fill_graph(int x1, int y1, int x2, int y2)
{
    // 0,2 / 4,4 ->
    // graph[2][0] = 1;
    // graph[3][3] = 1;

    // 1,1 / 2,5
    // graph[1][1] = 1;
    // graph[4][1] = 1;

    // 4,0 / 6,2
    // graph[0][4] = 1;
    // graph[1][5] = 1;

    for (int i = y1; i < y2; i++)
    {
        for (int j = x1; j < x2; j++)
        {
            graph[i][j] = 1;
        }
    }
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("2583_input.txt", "r", stdin);

    cin >> m >> n >> k;
    for (int i = 0; i < k; i++)
    {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        fill_graph(x1, y1, x2, y2);
    }
    // for (int i = 0; i < m; i++)
    // {
    //     for (int j = 0; j < n; j++)
    //     {
    //         cout << graph[i][j] << " ";
    //     }
    //     cout << "\n";
    // }
    int reg = 0;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (bfs(i, j) == true)
            {
                reg++;
            }
        }
    }
    cout << reg << "\n";
    sort(areas.begin(), areas.end(), less<int>());
    for (int &elem : areas)
    {
        cout << elem << " ";
    }

    cout << "\n";

    return 0;
}
