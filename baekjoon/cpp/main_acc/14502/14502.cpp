#include <iostream>
#include <vector>
using namespace std;

vector<int> graph[9];
int n, m;
int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("14502_input.txt", "r", stdin);
    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        int temp;
        for (int j = 0; j < m; j++)
        {
            cin >> temp;
            graph[i].push_back(temp);
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (auto &elem : graph[i])
            cout << elem << " ";
        cout << "\n";
    }

    return 0;
}
