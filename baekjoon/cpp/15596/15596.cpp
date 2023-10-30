#include <bits/stdc++.h>
using namespace std;
long long sum(std::vector<int> &a)
{
    long long s = 0;
    for (auto &elem : a)
    {
        s += elem;
    }
    return s;
}
int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("15596_input.txt", "r", stdin);
    long long S = 0;
    vector<int> vec = {1, 2, 3, 4, 5};
    S = sum(vec);
    cout << S << endl;
    return 0;
}
