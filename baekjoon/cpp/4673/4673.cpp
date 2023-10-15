#include <bits/stdc++.h>
using namespace std;

int dp[10001] = {
    0,
};

int pos_sum(int n)
{
    /*
    12345
    1+2+3+4+5
    한자리씩 줄여가기
    */
    int sum = 0;
    while (n != 0)
    {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int self(int n)
{
    // n을 쪼개기
    /*
    1+1=2
    2+2=4
    11 -> 11 + 1 + 1
    1234 -> 1234 + 1+2+3+4
    */
    n += pos_sum(n);
    if (n > 10000) // 10000넘는 un-self number
        return 0;
    else if (dp[n] == 0) // 본적없는 un-self number
    {
        dp[n] = 1;
        return self(n);
    }
    else // 이미 해본 거
    {
        return 0;
    }
}
int main()
{
    std::ios_base::sync_with_stdio(false);
    freopen("4673_input.txt", "r", stdin);

    for (int i = 1; i <= 10000; i++)
    {
        self(i);
    }
    for (int i = 1; i <= 10000; i++)
    {
        if (!dp[i])
            cout << i << endl;
    }

    return 0;
}
