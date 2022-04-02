#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
void input();
void solution();
void solve();

/*
첫 줄에는 멀티탭 구멍의 개수 N (1 ≤ N ≤ 100)과 전기 용품의 총 사용횟수 K (1 ≤ K ≤ 100)가 정수로
주어진다. 두 번째 줄에는 전기용품의 이름이 K 이하의 자연수로 사용 순서대로 주어진다.
각 줄의 모든 정수 사이는 공백문자로 구분되어 있다.

*/

template <typename T>
void print(queue<T> v)
{
    queue<T> temp(v);
    while (!temp.empty())
    {
        cout << temp.front() << " ";
        temp.pop();
    }
    cout << endl;
}

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
    solution();
}

int n, k;
queue<int> thing;
// vector<int> thing;
int dp[101] = {
    0,
};
void input()
{
    ifstream ifs;
    ifs.open("input.txt");
    ifs >> n >> k;
    for (int i = 0; i < k; i++)
    {
        int temp;
        ifs >> temp;
        thing.push(temp);
        dp[temp]++;
    }
    print(thing);
}

void solution()
{
    for (const int &elem : dp)
    {
        cout << elem << " ";
    }
    cout << endl;
    vector<int> multitab(n);
}