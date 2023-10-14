#include <string>
#include <iostream>
using namespace std;

vector<string> strs;

void split(string &S, const char &spliter)
{
    size_t previous = 0, current;
    current = S.find(spliter); // 찾지못한경우 npos반환

    while (current != string::npos)
    {
        string substring = S.substr(previous, current - previous);
        // cout << substring << " ";
        strs.push_back(substring);
        previous = current + 1;
        current = S.find(spliter, previous);
    }
    strs.push_back(S.substr(previous, current - previous));
    // cout << S.substr(previous, current - previous);
}

int main()
{

    string lines = "hello my name is";

    split(lines, ' ');
    for (auto &elem : strs)
        cout << elem << endl;

    return 0;
}