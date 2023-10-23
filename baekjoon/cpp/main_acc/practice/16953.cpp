#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
/*
첫째 줄에 A, B (1 ≤ A < B ≤ 1e9)가 주어진다.

2 162 => 5
4 42 => -1
100 40021 => 5
*/

//#define MAX 10

int init, finish;

void input()
{
    // ifstream ifs;
    // ifs.open("input.txt");
    // ifs >> init >> finish;

    // cout << init << " " << finish << endl;
    cin >> init >> finish;
}

void solution()
{
    int cnt = 1;
    while (finish > init)
    {
        if (finish % 10 == 1 || finish % 2 == 0)
        {
            if (finish % 10 == 1)
                finish /= 10;
            else
                finish /= 2;
            cnt++;
        }
        else
        {
            cout << -1 << endl;
            return;
        }
    }
    if (finish == init)
    {
        cout << cnt << endl;
    }
    else
    {
        cout << -1 << endl;
    }
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