#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
/*
첫째 줄에 문자열 S가 주어진다. S의 길이는 100만보다 작다.

11001100110011000001

=>4

*/

//#define MAX 10

string N;

void input()
{
    // ifstream ifs;
    // ifs.open("input.txt");
    // ifs >> N;

    // for (const auto &elem : N)
    // {
    //     cout << elem << " ";
    // }
    // cout << endl;

    cin >> N;
    // for (int i = 0; i < N; i++)
    // {
    //     cin >> words[i];
    // }
}

void solution()
{
    int cnt_0 = 0;
    int cnt_1 = 0;

    int prev = N[0] - '0';

    for (const auto &elem : N)
    {
        bool reversed = prev ^ (elem - '0');

        if (reversed)
        {
            if (prev)
                cnt_1++;
            else
                cnt_0++;
        }

        prev = elem - '0';
        // cout << reversed << " ";
    }
    // cout << endl;
    cout << max(cnt_1, cnt_0) << endl;
}

void solve()
{
    input();
    solution();
}

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    solve();

    return 0;
}