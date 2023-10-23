#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
/*
첫째 줄에 N과 M이 주어진다. N은 100보다 작거나 같은 자연수이고,
 M은 50보다 작거나 같은 자연수이다.
 둘째 줄부터 M개의 줄에는 각 브랜드의 패키지 가격과 낱개의 가격이
  공백으로 구분하여 주어진다.
 가격은 0보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

*/

int N, M;
vector<pair<int, int>> prices;

// template <typename T>
// void print(vector<pair<T, T>> &v)
// {
//     int cnt = 1;
//     for (const auto &elem : v)
//     {
//         cout << "(" << elem.first << "," << elem.second << ")"
//              << " ";
//         if (cnt % 4 == 0)
//             cout << endl;
//         cnt++;
//     }
//     cout << endl;
// }
// template <typename T>
// void print(pair<T, T> &v)
// {

//     cout << "(" << v.first << "," << v.second << ")"
//          << " ";

//     cout << endl;
// }

void input()
{
    // ifstream ifs;
    // ifs.open("input.txt");
    // ifs >> N >> M;

    // prices.reserve(M);

    // for (int i = 0; i < M; i++)
    // {
    //     int six_price, one_price;
    //     ifs >> six_price >> one_price;
    //     prices.push_back({six_price, one_price});
    // }

    cin >> N >> M;

    prices.reserve(M);

    for (int i = 0; i < M; i++)
    {
        int six_price, one_price;
        cin >> six_price >> one_price;
        prices.push_back({six_price, one_price});
    }

    // print(prices);
}
bool comp_six(const pair<int, int> &a, const pair<int, int> &b)
{
    return a.first < b.first;
}
bool comp_one(const pair<int, int> &a, const pair<int, int> &b)
{
    return a.second < b.second;
}
void solution()
{
    auto six_min = *min_element(prices.begin(), prices.end(), comp_six);
    auto one_min = *min_element(prices.begin(), prices.end(), comp_one);
    pair<int, int> least_price = {six_min.first, one_min.second};
    // cout << N << endl;
    // print(least_price);
    int &sp = least_price.first;  // six price
    int &op = least_price.second; // one price
    int res = 0;
    if (sp >= op * 6)
        res = N * op;
    else
    {
        if (N % 6 == 0)
            res = N / 6 * sp;
        else
        {
            res = min((N / 6 + 1) * sp, (N / 6) * sp + (N % 6) * op);
        }
    }
    cout << res << endl;
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