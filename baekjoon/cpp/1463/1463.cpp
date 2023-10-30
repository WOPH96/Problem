#include <bits/stdc++.h>
using namespace std;
int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("1463_input.txt", "r", stdin);

    /*
    정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

    X가 3으로 나누어 떨어지면, 3으로 나눈다.
    X가 2로 나누어 떨어지면, 2로 나눈다.
    1을 뺀다.
    정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

    1<X<10^6

    dp 1  2  3  4  5  6  7
       0  1  1

    dp 4부터 -> 3으로 나눈 몫 테이블의 값 vs 2로 나눈 몫 테이블의 값 vs 1 뺀 테이블의 값 비교, 제일 작은거 + 1


    */
    int n;
    cin >> n;

    vector<int> dp(100002, 0);
    dp[2] = dp[3] = 1;

    int m;
    for (int i = 4; i <= n; i++)
    {
        m = 1e6;
        if (i % 3 == 0)
        {
            if (dp[i / 3] < m)
                m = dp[i / 3];
        }
        if (i % 2 == 0)
        {
            if (dp[i / 2] < m)
                m = dp[i / 2];
        }
        if (dp[i - 1] < m)
            m = dp[i - 1];
        dp[i] = m + 1;
    }
    cout << dp[n] << endl;
    return 0;
}
