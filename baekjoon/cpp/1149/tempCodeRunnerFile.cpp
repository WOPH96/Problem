#include <bits/stdc++.h>
using namespace std;

int n;

vector<int> costs[1001];
vector<int> dp[1001];

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("1149_input.txt", "r", stdin);

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            int temp;
            cin >> temp;
            costs[i].push_back(temp);
            dp[i].push_back(0);
        }
    }

    for (int i = 0; i < 3; i++)
    {
        dp[0][i] = costs[0][i];
    }

    for (int i = 1; i < n; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            int m = 100000000;
            for (int k = 0; k < 3; k++)
            {
                if (j == k)
                    continue;
                else
                {
                    m = dp[i - 1][k] < m ? dp[i - 1][k] : m;
                }
            }
            dp[i][j] = costs[i][j] + m;
        }
    }

    cout << *min_element(dp[n - 1].begin(), dp[n - 1].end()) << "\n";
    return 0;
}
