#include <bits/stdc++.h>
using namespace std;
int n, k;
string numbers;
int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("2812_input.txt", "r", stdin);

    cin >> n >> k;
    cin >> numbers;

    vector<char> stack;
    int stored = k;
    for (char &elem : numbers)
    {
        while (!stack.empty() && stack.back() < elem && k > 0)
        {
            stack.pop_back();
            k--;
        }
        stack.push_back(elem);
    }
    if (k > 0)
    {
        for (int i = 0; i < n - stored; i++)
        {
            cout << stack[i];
        }
    }
    else
    {
        for (char &elem : stack)
        {
            cout << elem;
        }
    }
    cout << "\n";

    return 0;
}
