#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
/*
5
1 1 1 6 0
2 7 8 3 1
 */
int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;

    cin >> T;

    vector<int> A;
    vector<int> B;

    A.reserve(T);
    B.reserve(T);
    for (int j = 0; j < T; j++)
    {
        int in;
        cin >> in;
        A.push_back(in);
    }

    for (int j = 0; j < T; j++)
    {
        int in;
        cin >> in;
        B.push_back(in);
    }

    vector<pair<int, int>> C;
    for (int i = 0; i < T; i++)
    {
        C.push_back({B[i], i});
    }

    sort(C.begin(), C.end());

    // for (const auto &elem : C)
    // {
    //     cout << elem.first << elem.second << " ";
    // }
    // cout << endl;

    sort(A.begin(), A.end(), greater<int>());
    // for (const auto &elem : A)
    // {
    //     cout << elem << " ";
    // }
    // cout << endl;

    vector<pair<int, int>> result;
    result.reserve(T);

    for (int i = 0; i < T; i++)
    {
        result.push_back({C[i].second, A[i]});
    }

    sort(result.begin(), result.end());

    // for (const auto &elem : result)
    // {
    //     cout << elem.first << elem.second << " ";
    // }

    for (int i = 0; i < T; i++)
    {
        A[i] = result[i].second;
    }

    // for (const auto &elem : A)
    // {
    //     cout << elem << " ";
    // }
    int sum = 0;
    for (int i = 0; i < T; i++)
    {
        sum += A[i] * B[i];
    }
    cout << sum << endl;
    return 0;
}