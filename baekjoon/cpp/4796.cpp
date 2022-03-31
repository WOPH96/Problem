#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
/*
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있고,
L, P, V를 순서대로 포함하고 있다.
모든 입력 정수는 int범위이다.
마지막 줄에는 0이 3개 주어진다.*/

int L, P, V;

// template <typename T>
// void print(vector<T> v)
// {
//     for (const auto &elem : v)
//     {
//         cout << elem << " ";
//     }
//     cout << endl;
// }
void solution()
{
    static int CASE = 1;
    int all = V / P;
    int part = V % P;

    int day = L * all + min(part, L);
    cout << "Case " << CASE << ": " << day << endl;
    CASE++;
}
void input()
{
    // ifstream ifs;
    // ifs.open("input.txt");

    // while (1)
    // {
    //     ifs >> L >> P >> V;
    //     if ((L == 0 && P == 0 && V == 0))
    //         break;
    //     // cout << L << " " << P << " " << V << " " << endl;
    //     solution();
    // }

    while (1)
    {
        cin >> L >> P >> V;
        if ((L == 0 && P == 0 && V == 0))
            break;
        // cout << L << " " << P << " " << V << " " << endl;
        solution();
    }
}

void solve()
{
    input();
    // solution();
}

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    solve();

    return 0;
}