#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
/*
첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)가 주어진다.
각 테스트 케이스의 첫째 줄에 지원자의 숫자 N(1 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N개 줄에는 각각의 지원자의 서류심사 성적,
면접 성적의 순위가 공백을 사이에 두고 한 줄에 주어진다.
두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정된다고 가정한다.

2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
 */

template <typename T>
void printv(vector<T> v)
{
    for (const auto &elem : v)
    {
        cout << elem << " ";
    }
    cout << endl;
}

template <typename T>
void printv(vector<pair<T, T>> v)
{
    for (const auto &elem : v)
    {
        cout << elem.first << elem.second << " ";
    }
    cout << endl;
}

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;

        vector<pair<int, int>> scores(n);

        for (auto &elem : scores)
        {
            cin >> elem.first >> elem.second;
        }

        printv(scores);
    }

    return 0;
}