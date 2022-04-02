#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
void input();
void solution();
void solve();

/*
첫째 줄에 레벨의 수 N이 주어진다. (1 ≤ N ≤ 100)
다음 N개 줄에는 각 레벨을 클리어하면 얻는 점수가 첫 번째 레벨부터 마지막 레벨까지 순서대로 주어진다.
 점수는 20,000보다 작은 양의 정수이다.

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
vector<int> scores;
void input()
{
    // ifstream ifs;
    // ifs.open("input.txt");
    cin >> n;
    scores.reserve(n);
    for (int i = 0; i < n; i++)
    {
        int score;
        cin >> score;
        scores.push_back(score);
    }
}

void solution()
{
    long least = 0;
    for (auto itr = scores.rbegin() + 1; itr != scores.rend(); itr++)
    {
        if (*(itr - 1) <= *itr)
        {
            int diff = *itr - *(itr - 1) + 1;
            *itr -= diff;
            least += diff;
        }
    }
    cout << least << endl;
}