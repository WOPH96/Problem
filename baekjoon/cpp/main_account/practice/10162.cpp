#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
/*
첫 번째 줄에는 요리시간 T(초)가
정수로 주어져 있으며 그 범위는 1 ≤ T ≤ 10,000 이다.

A = 300
B = 60
C = 10

 */

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;

    vector<int> button({10, 60, 300});
    vector<int> ABC;
    while (T)
    {
        if (T % 10 != 0)
        {
            cout << -1 << endl;
            return 0;
        }
        if (T < button.back())
        {
            ABC.push_back(0);
            button.pop_back();
        }
        ABC.push_back(T / button.back());
        T %= button.back();
        button.pop_back();
    }
    while (ABC.size() != 3)
    {
        ABC.push_back(0);
    }

    for (const auto &elem : ABC)
    {
        cout << elem << " ";
    }
    cout << endl;

    return 0;
}