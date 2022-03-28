#include <bits/stdc++.h>
// #include <vector>
// #include <iostream>
using namespace std;
/*
split
 */
vector<string> split(string input, string delimiter)
{
    vector<string> ret;
    long long pos = 0;
    string token = "";
    while ((pos = input.find(delimiter)) != string::npos)
    {
        token = input.substr(0, pos);
        ret.push_back(token);
        input.erase(0, pos + delimiter.length());
        // cout << input << endl;
    }
    ret.push_back(input);
    return ret;
}

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    return 0;
}