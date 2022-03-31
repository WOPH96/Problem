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
    vector<int> pstv;
    vector<int> ngtv;
    vector<int> onev;

    bool zero = false;

    for (const auto &elem : v)
    {
        if (elem > 1)
            pstv.push_back(elem);
        else if (elem == 1)
            onev.push_back(elem);
        else if (elem == 0)
            zero = true;
        else // elem <0
            ngtv.push_back(elem);
    }

    sort(pstv.begin(), pstv.end(), greater<>());
    sort(ngtv.begin(), ngtv.end(), less<>());
    // print(pstv);
    int sum = 0;

    for (auto itr = pstv.begin(); itr < pstv.end(); itr += 2)
    {
        if (itr + 1 == pstv.end())
            sum += *itr;
        else
            sum += *(itr) * *(itr + 1);
    }
    // print(ngtv);
    for (auto itr = ngtv.begin(); itr < ngtv.end(); itr += 2)
    {
        if (itr + 1 == ngtv.end())
        {
            if (zero)
                break;
            sum += *itr;
        }
        else
            sum += *(itr) * *(itr + 1);
    }

    sum += onev.size();
    cout << sum << endl;
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