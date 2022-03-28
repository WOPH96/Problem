#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
/*
55-50+40
=-35

-하나라도 나오면 전부 그 뒤는 빼버린다.
 */

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string str;
    cin >> str;

    bool isMinus = false;

    int res = 0;
    string num = "";

    for (const char &elem : str)
    {
        if (elem == '-' || elem == '+' || elem == *str.end())
        {
            if (isMinus)
            {
                res -= stoi(num);
            }
            else
            {
                res += stoi(num);
            }
            num = "";
        }
        else
        {
            num += elem;
        }

        if (elem == '-')
            isMinus = true;
    }
    if (isMinus)
        res -= stoi(num);
    else
        res += stoi(num);
    cout << res << endl;
    return 0;
}