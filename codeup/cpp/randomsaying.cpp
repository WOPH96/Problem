#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

/*
10
1 3 2 2 5 6 7 4 5 9
*/
int main()
{
    vector<int> num(24);
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        int temp;
        cin >> temp;
        num[temp]++;
    }
    for (auto it = num.begin() + 1; it != num.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;

    return 0;
}