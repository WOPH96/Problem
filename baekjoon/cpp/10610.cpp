#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
/*
N을 입력받는다.
N는 최대 105개의 숫자로 구성되어 있으며, 0으로 시작하지 않는다.

 */
bool verify(string &num)
{
    int verify = 0;
    if (num.find('0') == string::npos)
    {
        return false;
    }
    for (const char &elem : num)
    {
        verify += elem - '0';
    }
    if (verify % 3 != 0)
    {
        return false;
    }
    return true;
}
int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string num;
    cin >> num;

    bool canbe30 = verify(num);

    if (canbe30)
    {
        sort(num.begin(), num.end(), greater<>());
        cout << num << endl;
    }
    else
    {
        cout << -1 << endl;
    }

    return 0;
}