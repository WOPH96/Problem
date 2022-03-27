#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
#define INF 1e9
using namespace std;

/*
첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)
*/
int main()
{
    vector<int> dp(5001, INF);

    dp[3] = dp[5] = 1;

    int N;
    cin >> N;

    for (int i = 6; i <= N; i++)
    {
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1;
    }

    if (dp[N] < N)
        cout << dp[N] << endl;
    else
        cout << -1 << endl;

    // for (int &elem : dp)
    //     cout << elem << " ";
    // cout << endl;

    return 0;
}