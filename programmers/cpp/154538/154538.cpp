#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int x, int y, int n)
{
    /*x에 n을 더합니다
    x에 2를 곱합니다.`
    x에 3을 곱합니다.*/
    int answer = 0;
    int dp[1000001];
    fill_n(dp, 1000001, 1e7);

    dp[x] = 0;

    int start = x + n;

    if (x * 2 < start)
        start = x * 2;
    if (x * 3 < start)
        start = x * 3;

    // cout << "start:" << start << endl;

    for (int i = x + 1; i <= y; i++)
    {
        int m = 1e7;
        if (i % 2 == 0)
        {
            // cout << i << "->" << dp[i / 2] << endl;
            if (dp[i / 2] < m)
                m = dp[i / 2];
        }
        if (i % 3 == 0)
        {
            // cout << i << "->" << dp[i / 3] << endl;
            if (dp[i / 3] < m)
                m = dp[i / 3];
        }
        if (i >= n)
        {
            // cout << i - n << "->" << dp[i - n] << endl;
            if (dp[i - n] < m)
                m = dp[i - n];
        }

        dp[i] = m + 1;
    }
    // for (int i = x; i <= y; i++)
    // {
    //     cout << i << ":" << dp[i] << endl;
    // }
    // cout << endl;
    answer = dp[y] > 1e7 ? -1 : dp[y];
    cout << answer << endl;

    return answer;
}
int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("154538_input.txt", "r", stdin);

    // solution(10, 40, 5); //	2
    solution(10, 40, 30); //,1)
    // solution(2, 5, 4);    //	-1)

    return 0;
}
