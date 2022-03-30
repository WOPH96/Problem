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

int N, K;
vector<pair<int, int>> jw;
vector<int> bag;

bool comp_value(const pair<int, int> &a, const pair<int, int> &b)
{
    if (a.second == b.second)
        return a.first < b.first;
    return a.second < b.second;
}
template <typename T>
void print(const vector<pair<T, T>> &v)
{
    for (const auto &elem : v)
    {
        cout << "(" << elem.first << "," << elem.second << ")"
             << " ";
    }
    cout << endl;
}

template <typename T>
void print(const vector<T> &v)
{
    for (const auto &elem : v)
    {
        cout << elem << " ";
    }
    cout << endl;
}

void input()
{
    // ifstream ifs;
    // ifs.open("input.txt");
    // ifs >> N >> K;
    // jw.reserve(N);
    // bag.reserve(K);
    // for (int i = 0; i < N; i++)
    // {
    //     int M, V;
    //     ifs >> M >> V;
    //     jw.push_back({M, V});
    // }
    // for (int i = 0; i < K; i++)
    // {
    //     int C;
    //     ifs >> C;
    //     bag.push_back(C);
    // }

    cin >> N >> K;
    jw.reserve(N);
    bag.reserve(K);
    for (int i = 0; i < N; i++)
    {
        int M, V;
        cin >> M >> V;
        jw.push_back({M, V});
    }
    for (int i = 0; i < K; i++)
    {
        int C;
        cin >> C;
        bag.push_back(C);
    }

    // print(jw);
    // print(bag);
}

void solution()
{
    sort(jw.begin(), jw.end(), comp_value);
    // sort(jw.begin(), jw.end(), [](const pair<int, int> &a, const pair<int, int> &b) -> bool
    //      { return a.second < b.second; });
    // for (const auto &elem : jw)
    // {
    //     cout << "(" << elem.first << "," << elem.second << ")"
    //          << " ";
    // }
    sort(bag.begin(), bag.end());
    // print(jw);
    // print(bag);

    long long val = 0;
    while (!bag.empty() && !jw.empty())
    {
        if (bag.back() < jw.back().first)
            jw.pop_back();
        else
        {
            auto itr = lower_bound(bag.begin(), bag.end(), jw.back().first);
            bag.erase(itr);
            val += jw.back().second;
            // print(bag);
            jw.pop_back();
        }
    }
    cout << val << endl;
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