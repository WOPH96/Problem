#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
/*

첫째 줄에 정수 N이 주어진다.
다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다.
이 값은 10,000을 넘지 않는 자연수이다.

2
10
15

=>20

 */

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    vector<int> ropes(n);

    for (auto &elem : ropes)
    {
        cin >> elem;
    }

    sort(ropes.begin(), ropes.end(), greater<>());

    int m_w = ropes.front();

    for (int i = 1; i < n; i++)
    {
        m_w = max(m_w, (i + 1) * ropes[i]);
    }

    cout << m_w << endl;

    return 0;
}