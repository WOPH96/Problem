#include <bits/stdc++.h>
using namespace std;
vector<int> graph[100001];
int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("11725_input.txt", "r", stdin);

    int n;
    cin >> n;
    for (int i = 1; i < n; i++)
    {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    for (int i = 1; i <= n; i++)
    {
        for (auto &elem : graph[i])
        {
            cout << elem << " ";
        }
        cout << endl;
    }

    return 0;
}
