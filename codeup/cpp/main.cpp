#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

// lower, upper bound

int main()
{
    int myints[] = {10, 20, 30, 30, 20, 10, 10, 20};
    vector<int> v(myints, myints + 8);

    sort(v.begin(), v.end());

    for (auto x : v)
    {
        cout << x << " ";
    }

    auto low = lower_bound(v.begin(), v.end(), 20);
    auto up = upper_bound(v.begin(), v.end(), 20);
    cout << endl;

    cout << distance(v.begin(), low) << endl;
    cout << distance(v.begin(), up) << endl;

    return 0;
}