#include <bits/stdc++.h>
using namespace std;
int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("2839_input.txt", "r", stdin);

    int n;
    cin >> n;

    // 3키로, 5키로, 봉지수 최대한 적게
    // 0  1  2  3  4  5  6
    //   -1 -1  1  -1 1
    vector<int> dp(5001, 5000);
    dp[3] = dp[5] = 1;
    // cout << sizeof(dp) << " " << sizeof(int) << endl;
    // dp[n] = min(dp[n-3], dp[n-5])+1
    for (int i = 6; i <= n; i++)
    {
        int m = 5000;
        if (dp[i - 3] < m)
            m = dp[i - 3];
        if (dp[i - 5] < m)
            m = dp[i - 5];
        if (m != 5000)
            dp[i] = m + 1;
    }
    if (dp[n] == 5000)
    {
        cout << -1 << endl;
        return 0;
    }
    cout << dp[n] << endl;

    return 0;
}
