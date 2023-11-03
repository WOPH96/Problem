#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;

unordered_map<char, int> dic;

int get_expire_date(string &y, string &m, string &d, char &t)
{
    int res = stoi(y) * 12 * 28 + (stoi(m) + dic[t] - 1) * 28 + stoi(d) - 1;
    return res;
}

vector<int> solution(string today, vector<string> terms, vector<string> privacies)
{
    vector<int> answer;
    // term [0] = type of term / term[2] = month of term
    // privacy.substr(0,3)
    int current = stoi(today.substr(0, 4)) * 12 * 28 + (stoi(today.substr(5, 2)) - 1) * 28 + stoi(today.substr(8, 2));
    // cout << current << '\n';
    for (auto &term : terms)
    {
        dic[term[0]] = stoi(term.substr(2, 3));
    }
    // for (auto &elem : dic)
    // {
    //     cout << elem.first << elem.second << endl;
    // }
    int i = 1;
    for (auto &pr : privacies)
    {
        // cout << pr << endl;
        char type = pr[11];
        string year = pr.substr(0, 4);
        string month = pr.substr(5, 2);
        string day = pr.substr(8, 2);
        int expire = get_expire_date(year, month, day, type);
        // cout << expire << endl;
        if (expire < current)
        {
            answer.push_back(i);
        }
        i++;
    }
    return answer;
}

int main()
{

    vector<int> res = solution("2022.01.01", {"A 6", "B 12", "C 3"}, {"2021.05.02 A", "2021.01.02 B", "2022.02.19 C", "2022.02.20 C"}); //	[1, 3]
    for (auto &elem : res)
    {
        cout << elem << " ";
    }
    return 0;
}
