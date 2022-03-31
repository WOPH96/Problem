#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;

// template <typename T>
// void print(vector<T> v)
// {
//     for (const auto &elem : v)
//     {
//         cout << elem << " ";
//     }
//     cout << endl;
// }
// template <typename T>
// void print(vector<pair<T, T>> v)
// {
//     for (const auto &elem : v)
//     {
//         cout << "(" << elem.first << "," << elem.second << ")" << endl;
//     }
//     cout << endl;
// }

int n;
vector<pair<int, int>> meetings;

bool comp(pair<int, int> &a, pair<int, int> &b)
{

    if (a.second == b.second)
        return a.first < b.first;
    return a.second < b.second;
}

void input()
{
    // ifstream ifs;
    // ifs.open("input.txt");
    // ifs >> n;

    // meetings.reserve(n);

    // for (int i = 0; i < n; i++)
    // {
    //     int start, end;
    //     ifs >> start >> end;
    //     meetings.push_back({start, end});
    // }
    cin >> n;

    meetings.reserve(n);

    for (int i = 0; i < n; i++)
    {
        int start, end;
        cin >> start >> end;
        meetings.push_back({start, end});
    }
}
void solution()
{
    sort(meetings.begin(), meetings.end(), comp);
    // print(meetings);
    vector<pair<int, int>> schedule;
    schedule.push_back(meetings[0]);
    for (int i = 1; i < meetings.size(); i++)
    {
        if (meetings[i].first >= schedule.back().second)
        {
            schedule.push_back(meetings[i]);
        }
    }
    cout << schedule.size() << endl;
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