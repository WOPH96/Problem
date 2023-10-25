#include <bits/stdc++.h>
using namespace std;
int main()
{
    std::ios_base::sync_with_stdio(false);
    freopen("11720_input.txt", "r", stdin);

    int total;
    cin >> total;

    string nums;
    cin >> nums;
    int sum = 0;
    for (auto &num : nums)
    {
        sum += num - '0';
    }
    cout << sum << endl;

    return 0;
}
