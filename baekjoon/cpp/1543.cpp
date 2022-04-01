#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
void input();
void solution();
void solve();

/*
첫째 줄에 문서가 주어진다.
문서의 길이는 최대 2500이다.
 둘째 줄에 검색하고 싶은 단어가 주어진다.
 이 길이는 최대 50이다.
 문서와 단어는 알파벳 소문자와 공백으로 이루어져 있다.
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
string org;
string fnd;

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
    // getline(ifs, org);
    // getline(ifs, fnd);

    getline(cin, org);
    getline(cin, fnd);

    // cout << org << endl
    //      << fnd << endl;
}

void solution()
{
    int cnt = 0;
    int n = fnd.size();
    int pos;

    while ((pos = org.find(fnd)) != string::npos)
    {
        cnt++;

        org.erase(0, pos + n);
        // cout << pos << " " << org << endl;
    }
    cout << cnt << endl;
}