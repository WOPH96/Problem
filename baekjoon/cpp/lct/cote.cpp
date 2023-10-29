#include <bits/stdc++.h>
using namespace std;
int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("cote_input.txt", "r", stdin);

    vector<int> heights;
    string temp;
    getline(cin, temp);
    for (auto &elem : temp)
    {
        if (elem == ' ' || elem == '\n')
            continue;
        heights.push_back(elem - '0');
    }
    for (auto &elem : heights)
    {
        cout << elem << " ";
    }

    return 0;
}
