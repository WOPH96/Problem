#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;

/*
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다.
 (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
10 4200
1
5
10
50
100
500
1000
5000
10000
50000

*/
int main()
{
    vector<int> coins;

    int n;
    long long k;

    cin >> n >> k;

    for (int i = 0; i < n; i++)
    {
        int coin;
        cin >> coin;
        if (coin > k)
            continue;
        coins.push_back(coin);
    }
    int answer = 0;

    while (k != 0)
    {
        answer += k / coins.back();
        k %= coins.back();
        coins.pop_back();
    }
    cout << answer << endl;
    // for (auto &elem : coins)
    //     cout << elem << " ";
    // cout << endl;
    return 0;
}