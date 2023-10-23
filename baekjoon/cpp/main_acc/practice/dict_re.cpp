#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
/*
첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)이 주어진다.
둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다.
단어는 알파벳 대문자로만 이루어져있다. 모든 단어에 포함되어 있는
알파벳은 최대 10개이고, 수의 최대 길이는 8이다.
서로 다른 문자는 서로 다른 숫자를 나타낸다.
2
AAA
AAA

=>1998

*/

// template <typename T>
// void printv(vector<T> v)
// {
//     for (const auto &elem : v)
//     {
//         cout << elem << " ";
//     }
//     cout << endl;
// }

// template <typename T>
// void printv(vector<pair<T, T>> v)
// {
//     for (const auto &elem : v)
//     {
//         cout << elem.first << elem.second << " ";
//     }
//     cout << endl;
// }
#define MAX 10

int N;
string words[MAX];

map<char, int> dict;
// bool comp(const string &a, const string &b)
// {
//     return a.size() > b.size();
// }
struct comp
{
    bool operator()(const string &a, const string &b)
    {
        return a.size() > b.size();
    }
};

void input()
{
    ifstream ifs;
    ifs.open("input.txt");
    ifs >> N;
    for (int i = 0; i < N; i++)
    {
        ifs >> words[i];
    }
    // cin >> N;
    // for (int i = 0; i < N; i++)
    // {
    //     cin >> words[i];
    // }
}

void solution()
{
    sort(words, words + N, comp());
    for (int i = 0; i < N; i++)
    {
        cout << words[i].size() << " ";
    }
    dict[A] = 1;
    auto itr = dict.find('A');

    cout << endl;
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