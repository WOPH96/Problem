#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
void input();
void solution();
void solve();

/*
첫째 줄에 물이 새는 곳의 개수 N과 테이프의 길이 L이
 주어진다. 둘째 줄에는 물이 새는 곳의 위치가 주어진다.
 N과 L은 1,000보다 작거나 같은 자연수이고,
 물이 새는 곳의 위치는 1,000보다 작거나 같은 자연수이다.


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
int n, l;
vector<int> loc;

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
    solution();
}

void input()
{
    // ifstream ifs;
    // ifs.open("input.txt");
    // ifs >> n >> l;
    // l *= 2;
    // loc.reserve(n);
    // // cout << n << " " << l << endl;
    // for (int i = 0; i < n; i++)
    // {
    //     int water;
    //     ifs >> water;
    //     loc.push_back(water * 2);
    // }
    // // print(loc);
    cin >> n >> l;
    l *= 2;
    loc.reserve(n);
    // cout << n << " " << l << endl;
    for (int i = 0; i < n; i++)
    {
        int water;
        cin >> water;
        loc.push_back(water * 2);
    }
    // print(loc);
}

void solution()
{

    vector<bool> zone(2002, false);
    vector<int> waterzone;
    int cnt = 0;
    for (const int &elem : loc)
    {
        zone[elem - 1] = true;
        zone[elem] = true;
        zone[elem + 1] = true;
    }
    // for (auto itr = zone.begin(); itr != zone.end(); itr++)
    // {
    //     if (*itr)
    //         cout << itr - zone.begin() << " ";
    // }
    // cout << endl;
    vector<bool>::iterator pos;
    while ((pos = find(zone.begin(), zone.end(), true)) != zone.end())
    {
        cnt++;
        // cout << cnt << " " << pos - zone.begin() << endl;
        auto end = pos + l;
        // cout << pos - zone.begin() << " " << end - zone.begin() << endl;
        for (; pos != end + 1; pos++)
        {
            *pos = false;
        }
    }

    cout << cnt << endl;
}