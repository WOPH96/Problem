#include <iostream>
#include <vector>
#include <queue>

using namespace std;
vector<int> graph[101];
int parents[101] = {
    0,
};
bool visited[101] = {
    false,
};
int n, m;
int src, dst;

int bfs(int src, int dst)
{
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("2644_input.txt", "r", stdin);

    cin >> n;
    cin >> src >> dst;
    cin >> m;

    for (int i = 0; i < m; i++)
    {
        int x, y;
        cin >> x >> y;
        graph[x].push_back(y);
        parents[y] = x;
    }

    for (int i = 1; i <= n; i++)
    {
        for (int &elem : graph[i])
        {
            cout << elem << " ";
        }
        cout << "\n";
    }

    for (int i = 1; i <= n; i++)
    {
        cout << parents[i] << " " << visited[i] << "\n";
    }

    int res = bfs(src, dst);

    cout << res << "\n";

    /*
    1       4
    2    3  5 6
    789

    아래 보고 bfs

    */

    return 0;
}
