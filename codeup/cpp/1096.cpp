#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

/*
5
1 1
2 2
3 3
4 4
5 5
*/
int main()
{
    vector<vector<int>> v(19, vector<int>(19, 0));
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int a, b;
        cin >> a >> b;
        v[a - 1][b - 1] = 1;
    }
    for (auto i : v)
    {
        for (auto j : i)
        {
            cout << j << " ";
        }
        cout << endl;
    }

    return 0;
}