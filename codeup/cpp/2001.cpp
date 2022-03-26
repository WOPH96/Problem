#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

/*
800
700
900
198
330
*/
double round_n(double d, int n)
{
    return round(d * pow(10, n)) / pow(10, n);
}
int main()
{
    vector<int> pasta(3);
    vector<int> juice(2);

    for (auto &elem : pasta)
        cin >> elem;
    for (auto &elem : juice)
        cin >> elem;

    double set_menu =
        *min_element(pasta.begin(), pasta.end()) + *min_element(juice.begin(), juice.end());
    // cout << set_menu << endl;
    printf("%.1lf \n", round_n(set_menu * 1.1, 1));
}