#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

/*
1 -2 1 8
*/
int main()
{
    vector<long long> v;

    int a, m, d, n;

    cin >> a >> m >> d >> n;

    v.push_back(a);

    while (v.size() != n)
    {
        v.push_back(v.back() * m + d);
    }
    cout << v.back() << endl;

    return 0;
}