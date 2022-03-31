#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;

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
int n;
vector<int> weights;
void input()
{
    ifstream ifs;
    ifs.open("input.txt");
    ifs >> n;

    weights.reserve(n);

    for (int i = 0; i < n; i++)
    {
        int chu;
        ifs >> chu;
        weights.push_back(chu);
    }
    print(weights);
}
void solution()
{
    sort(weights.begin(), weights.end());
    print(weights);
    int sum = 0;
    int temp;
    for (const auto &x : weights)
    {
        temp = x;
        sum += x;
        if (sum < *(&x + 1))
        {
            break;
        }
    }
    for (int i = temp; i <= sum; i++)
    {
    }
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