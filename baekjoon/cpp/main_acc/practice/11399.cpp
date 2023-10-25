#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;

/*
첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)
5
3 1 4 3 2

*/
int main()
{
    vector<int> p;

    int person;
    cin >> person;

    for (int i = 0; i < person; i++)
    {
        int time;
        cin >> time;
        p.push_back(time);
    }

    sort(p.begin(), p.end());

    int result = 0;
    int sum = 0;
    for (int &elem : p)
    {
        sum += elem;
        result += sum;
    }
    cout << result << endl;

    return 0;
}