#include <bits/stdc++.h>
using namespace std;

bool visited[101] = {
    false,
};

vector<int> friends[101];

int n, m;

// int dfs(int person, int target, int depth = 0)
// {
//     if (person == target)
//     {
//         cout << "find!" << depth << endl;
//         return depth;
//     }
//     if (!visited[person])
//     {
//         visited[person] = true;
//         cout << "요소 " << person << endl;
//         for (auto &elem : friends[person])
//         {
//             dfs(elem, target, depth + 1);
//         }
//     }
// }

int bfs(int person, int target)
{
    queue<pair<int, int>> q;
    q.push({person, 0});
    int out, relation;
    while (!q.empty())
    {
        out = q.front().first;
        relation = q.front().second;
        q.pop();
        if (!visited[out])
        {
            for (auto &elem : friends[out])
            {
                if (elem == target)
                    return relation + 1;
                q.push({elem, relation + 1});
            }
        }
    }
    return relation;
}
int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("1389_input.txt", "r", stdin);

    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        friends[a].push_back(b);
        friends[b].push_back(a);
    }

    // for (int i = 1; i <= n; i++)
    // {
    //     for (auto &elem : friends[i])
    //     {
    //         cout << elem << " ";
    //     }
    //     cout << '\n';
    // }
    struct cmp
    {
        bool operator()(pair<int, int> &a, pair<int, int> &b)
        {
            if (a.first == b.first)
            {
                return a.second > b.second;
            }
            else
            {
                return a.first > b.first;
            }
        }
    };
    priority_queue<pair<int, int>, vector<pair<int, int>>, cmp> pq;
    for (int i = 1; i <= n; i++)
    {
        // cout << i << "의 친구"
        //      << "\n";
        int sum = 0;
        for (int j = 1; j <= n; j++)
        {
            if (i == j)
                continue;
            sum += bfs(i, j);

            memset(visited, false, n);
        }
        pq.push({sum, i});
    }

    cout << pq.top().second << " \n";
    return 0;
}
