#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

/*
5 5
3
2 0 1 1
3 1 2 3
4 1 2 5
*/
int main()
{

    int m, n;
    cin >> m >> n;

    vector<vector<int>> v(m, vector<int>(n));

    int numstick;
    cin >> numstick;

    vector<vector<int>> inform(numstick);

    for (int i = 0; i < numstick; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            int tmp;
            cin >> tmp;
            inform[i].push_back(tmp);
        }
    }

    for (int i = 0; i < numstick; i++)
    {
        int x = inform[i][2];
        int y = inform[i][3];
        int d = inform[i][1];
        int l = inform[i][0];

        for (int j = 0; j < l; j++)
        {

            if (d)
            {
                if (x - 1 + j >= m)
                    break;
                v[x - 1 + j][y - 1] = 1;
            }
            else
            {
                if (y - 1 + j >= n)
                    break;
                v[x - 1][y - 1 + j] = 1;
            }
        }
    }
    /*
    2 0 1 1
    (1-1,1-1) + (0,1) + (0,1)
    3 1 2 3
    (2-1,3-1) + (1,0) + (1,0) + (1,0)
    */

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