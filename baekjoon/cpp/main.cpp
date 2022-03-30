#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
/*
첫째 줄에 수열의 크기 N이 주어진다. N은 50보다 작은 자연수이다.
둘째 줄부터 N개의 줄에 수열의 각 수가 주어진다.
수열의 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.
*/

int n;
vector<int> v;

// template <typename T>
// void print(vector<T> v)
// {
//     for (const auto &elem : v)
//     {
//         cout << elem << " ";
//     }
//     cout << endl;
// }
void input()
{
    // ifstream ifs;
    // ifs.open("input.txt");
    // ifs >> n;

    // v.reserve(n);

    // for (int i = 0; i < n; i++)
    // {
    //     int num;
    //     ifs >> num;
    //     v.push_back(num);
    // }

    cin >> n;

    v.reserve(n);

    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        v.push_back(num);
    }
    // print(v);
}

void solution()
{
    sort(v.begin(), v.end());
    // print(v);
    int res = 0;
    int zero_cnt = 0;
    while (!v.empty() && v.back() >= 0)
    {
        int size = size;
        if (size >= 2 && *(v.end() - 2) > 1)
        {
            int last = v.back();
            v.pop_back();
            last *= v.back();
            v.pop_back();
            res += last;
        }
        else if (size >= 2 && (*(v.end() - 2) == 1))
        {
            int last = v.back();
            v.pop_back();
            last += v.back();
            v.pop_back();
            res += last;
        }
        else if (v.back() == 1)
        {
            res += v.back();
            v.pop_back();
        }
        else if (v.back() == 0)
        {
            zero_cnt++;
            v.pop_back();
        }

        // print(v);
        // cout << res << " zero : " << zero_cnt << endl;
    }
    if (v.empty())
    {
        cout << res << endl;
        return;
    }
    sort(v.begin(), v.end(), greater<>());
    // print(v);
    while (!v.empty())
    {
        int size = v.size();
        if (size >= 2)
        {
            int last = v.back();
            v.pop_back();
            last *= v.back();
            v.pop_back();
            res += last;
        }
        else
        {
            if (zero_cnt)
            {
                v.pop_back();
                zero_cnt--;
            }
            else
            {
                res += v.back();
                v.pop_back();
            }
        }
        // print(v);
        cout << res << endl;
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