#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> solution(vector<int> numbers)
{
    vector<int> answer;

    // probably 시간초과
    // for (int i = 0; i < numbers.size(); i++)
    // {
    //     int j;
    //     for (j = i + 1; j < numbers.size(); j++)
    //     {
    //         if (numbers[i] < numbers[j])
    //         {
    //             answer.push_back(numbers[j]);
    //             break;
    //         }
    //     }
    //     if (j == numbers.size())
    //         answer.push_back(-1);
    // }
    for (auto &elem : answer)
    {
        cout << elem << " ";
    }
    cout << "\n";
    return answer;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("154539_input.txt", "r", stdin);

    solution({2, 3, 3, 5});       //	[3, 5, 5, -1]
    solution({9, 1, 5, 3, 6, 2}); //	[-1, 5, 6, 6, -1, -1]
    // 100만개 max
    // 풀려면 풀 수 있다. 시간초과가 날뿐
    return 0;
}
