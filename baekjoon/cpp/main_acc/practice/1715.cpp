#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
/*
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000) 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 각각의 크기가 주어진다.
 숫자 카드 묶음의 크기는 1,000보다 작거나 같은 양의 정수이다.
3
10
20
40

=>100

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

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    priority_queue<long, vector<long>, greater<>> pq;

    for (int i = 0; i < n; i++)
    {
        long data;
        cin >> data;
        pq.push(data);
    }

    // printpq(pq);
    long sum = 0;
    long result = 0;
    int cnt = 0;
    // sort(cards.begin(), cards.end(), greater<>());

    while (!pq.empty())
    {
        if (cnt == n - 1)
            break;
        sum += pq.top();
        pq.pop();

        sum += pq.top();
        pq.pop();

        pq.push(sum);
        result += sum;
        sum = 0;
        cnt++;
    }

    // while (!pq.empty())
    // {
    //     sum += pq.top();
    //     pq.pop();
    // }
    // result += sum;
    cout << result << endl;

    // printpq(pq);

    return 0;
}