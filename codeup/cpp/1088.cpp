#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

/*
10
*/
int main()
{
    int n;
    cin >> n;
    for (int i = 0; i <= n; i++)
    {
        if ([](int three)
            { return three % 3 == 0; }(i))
        {
            continue;
        }
        cout << i << " ";
    }
    cout << endl;
    return 0;
}