#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
/*
380
입력은 한줄로 이루어져있고,
타로가 지불할 돈(1 이상 1000미만의 정수) 1개가 쓰여져있다.

1000-380
620
500 100 10 10

큰동전부터
 */

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    vector<int> coins({1, 5, 10, 50, 100, 500});

    int pay;
    cin >> pay;

    pay = 1000 - pay;
    int coin = 0;
    while (pay)
    {
        if (pay < coins.back())
            coins.pop_back();
        coin += pay / coins.back();
        pay %= coins.back();
        coins.pop_back();
    }

    cout << coin << endl;

    return 0;
}