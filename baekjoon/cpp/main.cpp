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
template <typename T>
void print(vector<pair<T, T>> v)
{
    for (const auto &elem : v)
    {
        cout << "(" << elem.first << "," << elem.second << ")" << endl;
    }
    cout << endl;
}

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

int n;
vector<pair<int, int>> classes;
void input()
{
    ifstream ifs;
    ifs.open("input.txt");
    ifs >> n;
    for (int i = 0; i < n; i++)
    {
        int start, end;
        ifs >> start >> end;
        classes.push_back({start, end});
    }
    print(classes);
}
bool comp(const pair<int, int> &a, const pair<int, int> &b)
{
    if (a.second == b.second)
        a.first < b.first;
    return a.second < b.second;
}
void solution()
{
    sort(classes.begin(), classes.end(), comp);
    print(classes);
}