#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

/*
10
10 4 2 3 6 6 7 9 8 5
*/
int main()
{
    vector<int> stack;

    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        int in;
        cin >> in;
        stack.push_back(in);
    }

    while (!stack.empty())
    {
        cout << stack.back() << " ";
        stack.pop_back();
    }
    cout << endl;

    return 0;
}