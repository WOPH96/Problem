#include <string>
#include <iostream>
using namespace std;
int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("10926_input.txt", "r", stdin);

    string input;
    cin >> input;

    input += "\?\?!";
    // input.append("\?\?!");
    cout << input << "\n";

    return 0;
}
