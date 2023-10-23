#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
/*
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?
첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

200
=>19

4294967295

루트 2
 */

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long S;
    cin >> S;

    long long n = round(sqrt(S) * sqrt(2));

    while (n * (n + 1) / 2 > S)
    {
        n--;
    }

    cout << n << endl;

    return 0;
}