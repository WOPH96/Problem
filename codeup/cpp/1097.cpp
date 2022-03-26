#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

/*
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
2
10 10
12 12
*/
int main()
{
    vector<vector<int>> pan(19, vector<int>(19));
    // for (int i = 0; i < 19; i++)
    // {
    //     for (int j = 0; j < 19; j++)
    //     {
    //         cin >> pan[i][j];
    //     }
    // }

    for (auto &i : pan)
    {
        for (auto &elem : i)
        {
            cin >> elem;
        }
    }

    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        //본인은 뺴고 뒤집나? dd
        //두번 뒤집히면됨
        int x, y;
        cin >> x >> y;

        for (int j = 0; j < 2; j++)
        {
            for (int k = 0; k < 19; k++)
            {
                if (j)
                {
                    pan[x - 1][k] ^= 1;
                }
                else
                {
                    pan[k][y - 1] ^= 1;
                }
            }
        }
    }

    // cout << endl;
    for (const auto &i : pan) // 보기용
    {
        for (const auto &elem : i)
        {
            cout << elem << " ";
        }
        cout << endl;
    }

    return 0;
}