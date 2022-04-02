#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
void input();
void solution();
void solve();

/*
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
 각 테스트 케이스는 거스름돈 C를 나타내는 정수 하나로 이루어져 있다.
 C의 단위는 센트이다. (1달러 = 100센트) (1<=C<=500)

*/

template <typename T>
void print(vector<T> v)
{
    for (const auto &elem : v)
    {
        cout << elem << " ";
    }
    cout << endl;
}
// template <typename T>
// void print(vector<pair<T, T>> v)
// {
//     for (const auto &elem : v)
//     {
//         cout << "(" << elem.first << "," << elem.second << ")" << endl;
//     }
//     cout << endl;
// }

// template <typename T, typename Y>
// void print(vector<pair<pair<T, T>, Y>> v)
// {
//     for (const auto &elem : v)
//     {
//         cout << "(" << elem.first.first << "," << elem.first.second << "," << elem.second << ")" << endl;
//     }
//     cout << endl;
// }

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    solve();

    return 0;
}
void solve()
{
    input();
    // solution();
}

int t, c;
vector<pair<pair<int, int>, bool>> classes;
void input()
{
    // ifstream ifs;
    // ifs.open("input.txt");
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> c;
        solution();
    }
}

void solution()
{
    vector<int> coins({1, 5, 10, 25});
    vector<int> charged;
    int n = coins.size();
    charged.reserve(n);
    while (c)
    {
        charged.push_back(c / coins.back());
        c %= coins.back();
        coins.pop_back();
    }
    while (charged.size() != n)
    {
        charged.push_back(0);
    }
    print(charged);
}