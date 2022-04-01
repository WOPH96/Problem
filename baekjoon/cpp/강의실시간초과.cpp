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

int n;
vector<pair<pair<int, int>, bool>> classes;
void input()
{
    // ifstream ifs;
    // ifs.open("input.txt");
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int start, end;
        cin >> start >> end;
        classes.push_back({{start, end}, false});
    }
    // print(classes);
}
bool comp(const pair<pair<int, int>, bool> &a)
{
    return a.second;
}
void solution()
{
    sort(classes.begin(), classes.end()); //, comp);
    int cnt = 0;
    while (!classes.empty())
    {
        cnt++;
        auto itr = classes.begin();
        int prev = (*itr).first.second;
        (*itr).second = true;
        itr++;
        for (; itr != classes.end(); itr++)
        {
            if ((*itr).first.first >= prev)
            {
                (*itr).second = true;
                prev = (*itr).first.second;
            }
        }
        // print(classes);
        classes.erase(remove_if(classes.begin(), classes.end(), comp), classes.end());
    }

    // print(classes);
    cout << cnt << endl;
}