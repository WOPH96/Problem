#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
/*
첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)

다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)

다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)

모든 숫자는 양의 정수이다.

*/

//#define MAX 10

// template <typename T>
// void print(const T &s)
// {
//     for (const auto &elem : s)
//     {
//         cout << elem << " ";
//     }
//     cout << endl;
// }

string A, B;

void input()
{
    // ifstream ifs;
    // ifs.open("input.txt");
    // ifs >> A >> B;

    cin >> A >> B;
    // print(A);
    // print(B);
}

int tomax(string a, string b)
{

    for (auto &elem : a)
    {
        if (elem == '5')
        {
            elem = '6';
        }
    }

    for (auto &elem : b)
    {
        if (elem == '5')
        {
            elem = '6';
        }
    }
    return stoi(a) + stoi(b);
}

int tomin(string a, string b)
{

    for (auto &elem : a)
    {
        if (elem == '6')
        {
            elem = '5';
        }
    }

    for (auto &elem : b)
    {
        if (elem == '6')
        {
            elem = '5';
        }
    }
    return stoi(a) + stoi(b);
}

void solution()
{
    int sum_max = tomax(A, B);
    int sum_min = tomin(A, B);
    cout << sum_min << " " << sum_max << endl;
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