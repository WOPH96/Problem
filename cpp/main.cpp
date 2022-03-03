#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct comp
{
    bool iterator()(const char &c) { return c < c + 1; }
};

string solution(string s)
{
    string answer = "";

    cout << *(s.end() - 1) << endl;

    return answer;
}

int main()
{

    cout << solution("Zbcdefg") << endl;

    return 0;
}