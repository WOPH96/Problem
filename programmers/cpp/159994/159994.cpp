#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(vector<string> cards1, vector<string> cards2, vector<string> goal)
{
    string answer = "";
    int i = 0, j = 0;

    for (auto &elem : goal)
    {
        if (cards1[i] == elem)
        {
            i++;
        }
        else if (cards2[j] == elem)
        {
            j++;
        }
        else
        {
            return "No";
        }
    }

    return "Yes";
}

int main()
{

    cout << solution({"i", "drink", "water"}, {"want", "to"}, {"i", "want", "to", "drink", "water"}); //	"Yes");
    cout << solution({"i", "water", "drink"}, {"want", "to"}, {"i", "want", "to", "drink", "water"}); //	"No"

    return 0;
}