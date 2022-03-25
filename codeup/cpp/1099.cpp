#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

/*
1 1 1 1 1 1 1 1 1 1
1 0 0 1 0 0 0 0 0 1
1 0 0 1 1 1 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 1 0 1 0 1
1 0 0 0 0 1 2 1 0 1
1 0 0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
*/
int main()
{
    vector<vector<int>> v(10);

    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            int in;
            cin >> in;
            v[i].push_back(in);
        }
    }

    // cout << endl;

    int dx[] = {0, 1};
    int dy[] = {1, 0};
    int cood[] = {1, 1};
    bool feed = false;

    while (true)
    {
        pair<int, int> org = {cood[0], cood[1]};
        if (v[cood[0]][cood[1]] == 2)
        {
            feed = true;
            v[cood[0]][cood[1]] = 9;
            break;
        }
        else if (v[cood[0]][cood[1]] == 0)
            v[cood[0]][cood[1]] = 9;
        for (int i = 0; i <= 1; i++)
        {
            cood[0] += dx[i];
            cood[1] += dy[i];

            if (v[cood[0]][cood[1]] == 1)
            {
                cood[0] = org.first;
                cood[1] = org.second;
            }
            else
            {
                if (v[cood[0]][cood[1]] == 2)
                    feed = true;
                v[cood[0]][cood[1]] = 9;
                break;
            }
        }
        if (feed || (cood[0] == org.first && cood[1] == org.second))
            break;
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