#include <bits/stdc++.h>

using namespace std;

vector<string> split(const string &str, const char &dim = ' ')
{
    vector<string> vs; //= {"hello", "my"};
    string sub;
    size_t previous = 0, current;
    current = str.find(dim);
    while (current != string::npos)
    {
        sub = str.substr(previous, current - previous);
        vs.push_back(sub);
        previous = current + 1;
        current = str.find(dim, previous);
    }
    vs.push_back(str.substr(previous));

    // cout << sub;
    return vs;
}

int main()
{
    vector<string> str;

    string line = "hello my name is wonphil";
    str = split(line, ',');
    for (auto &elem : str)
    {
        cout << elem << endl;
    }

    return 0;
}