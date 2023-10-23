#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int n, m;
vector<int> fruit[101];

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("cote_input.txt", "r", stdin);

    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        int temp;

        for (int j = 0; j < m; j++)
        {
            cin >> temp;
            fruit[i].push_back(temp);
        }
    }

    // for (int i = 0; i < n; i++)
    // {

    //     for (int j = 0; j < m; j++)
    //     {
    //         cout << fruit[i][j] << " ";
    //     }
    //     cout << "\n";
    // }

    vector<int> idx_list;

    int s = idx_list.size();

    priority_queue<pair<vector<int>, int>> pq;
    for (int i = 0; i < n; i++)
    {
        pq.push({fruit[i], i});
    }

    while (!pq.empty())
    {
        // vector<int> temp = pq.top().first;

        // for (auto &elem : temp)
        // {
        //     cout << elem << " ";
        // }
        int idx = pq.top().second;
        idx_list.push_back(idx + 1);
        pq.pop();
    }

    return 0;
}
