#include <iostream>
#include <vector>
#include <queue>

using namespace std;
vector<int> children[101];
int parents[101] = {
    0,
};
bool visited[101] = {
    false,
};
int n, m;
int src, dst;

void dfs(int src, int dst, int depth)
{
}

int bfs(int src, int dst)
{
    queue<pair<int, int>> q;
    int cur = src;
    int out, chon = 0;
    while (true)
    {

        q.push({cur, chon});
        while (!q.empty())
        {

            out = q.front().first;
            int cchon = q.front().second;

            q.pop();
            if (!visited[out])
            {
                // cout << out << " " << cchon << endl;
                visited[out] = true;
                if (out == dst)
                {
                    // cout << "Hi!!" << endl;
                    return cchon;
                }
                else
                {
                    // 자식탐방
                    for (int &elem : children[out])
                    {
                        if (elem == dst)
                            return cchon + 1;
                        else
                            q.push({elem, cchon + 1});
                    }
                }
            }
        }
        if (parents[cur])
        {
            cur = parents[cur];
            chon += 1;
        }
        else
        {
            return -1;
        }
    }
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
        children[x].push_back(y);
        parents[y] = x;
    }

    // for (int i = 1; i <= n; i++)
    // {
    //     for (int &elem : children[i])
    //     {
    //         cout << elem << " ";
    //     }
    //     cout << "\n";
    // }

    // for (int i = 1; i <= n; i++)
    // {
    //     cout << parents[i] << "\n";
    // }

    int res = bfs(src, dst);

    cout << res << "\n";

    /*
    1       4
    2  3    5 6
    789

    아래 보고 bfs

    */

    return 0;
}
