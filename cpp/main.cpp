#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<long long> solution(int x, int n)
{
    vector<long long> answer;
    tmp = x;
    while (n)
    {
        answer.push_back(x);
        x += tmp;
        n -= 1;
    }

    return answer;
}

int main()
{

    return 0;
}