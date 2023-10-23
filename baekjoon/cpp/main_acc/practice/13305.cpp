#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
/*
표준 입력으로 다음 정보가 주어진다.
첫 번째 줄에는 도시의 개수를 나타내는 정수 N(2 ≤ N ≤ 100,000)이 주어진다.
다음 줄에는 인접한 두 도시를 연결하는 도로의 길이가
제일 왼쪽 도로부터 N-1개의 자연수로 주어진다.
다음 줄에는 주유소의 리터당 가격이 제일 왼쪽 도시부터
순서대로 N개의 자연수로 주어진다. 제일 왼쪽 도시부터
제일 오른쪽 도시까지의 거리는 1이상 1,000,000,000 이하의 자연수이다.
리터당 가격은 1 이상 1,000,000,000 이하의 자연수이다.

4
2 3 1
5 2 4 1
==>18

4
3 3 4
1 1 1 1
==>10
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

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    vector<long long> road(n - 1);
    vector<long long> cities(n);

    for (auto &elem : road)
    {
        cin >> elem;
    }

    for (auto &elem : cities)
    {
        cin >> elem;
    }

    long long oil = 0;
    long long MIN = 1e11;

    for (int i = 0; i < n - 1; i++)
    {
        MIN = min(MIN, cities[i]);

        oil += MIN * road[i];
    }
    cout << oil << endl;
    // printv(road);
    // printv(cities);
    return 0;
}