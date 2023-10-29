#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

vector<int> solution(vector<int> seq, int k)
{
    vector<int> answer;
    //     int left = 0, right = 0;
    //     int sum, i;

    //     // {index 길이,시작점} 저장하자, 정렬 편하게
    //     // 저장은 -index,시작점 , 오름차순 정렬을 위해

    //     /* 최적화1 ! */
    //     // gap이 제일 작고, idx가 제일 빠를수록 좋다
    //     // 즉 gap 작은거 나오면, 그 위 범위는 볼 필요 없음
    //     // ex) 처음으로 2,3 나왔으면 gap을 줄인다 = 3,3 / 4,4 / 5,5 / 6,6 ..
    //     // ex) 처음으로 2,4 나왔으면 -> 3,4 / 4,5 / 5,6

    //     // idx..는 안해도될것같은데 최적화 후보 !
    //     priority_queue<pair<int, int>> lists;
    //     int gap=-1;
    //     do
    //     {
    //         // 과정중에 idx 하나로 찾으면 끝
    //         sum = 0;
    //         for (i = left; i <= right; i++)
    //         {
    //             sum += seq[i];
    //             // cout << sum << " " << left << "," << right << "\n";
    //         }
    //         if (sum == k)
    //         {
    //             //gap 한번 찾았으면, 앞으로는 이 값보다 작은 범위로만 찾아야 함
    //             gap = right - left;
    //             lists.push({-gap, -left});
    //             // cout << gap << " " << left <<","<<right << '\n';
    //             if (gap == 0)
    //             {
    //                 answer.push_back(left);
    //                 answer.push_back(right);
    //                 return answer;
    //             }

    //             left+=2;
    //             right++;

    //         }
    //         else if (sum < k)
    //         {
    //             // 오른쪽이 한칸 가면, 더 큰 수를 더하므로
    //             right++;
    //             // 찾은 gap보다 작은 범위를 찾게 하기
    //             if(right-left==gap) left++;
    //         }
    //         else
    //         {
    //             // 왼쪽이 한칸 가면, 더했던 수를 빼므로
    //             left++;
    //         }
    //         // cout << gap << " " << left <<","<<right << '\n';

    //     } while (right < seq.size() && left <= right);

    //     gap = -1 * lists.top().first;
    //     left = -1 * lists.top().second;
    //     answer.push_back(left);
    //     answer.push_back(left + gap);

    // 위 코드는 계속 처음부터 더하는 코드여서, 시간이 오래걸림
    // 구한 sum에서 빼거나 더해서 코드를 완성하는게 포인트

    int left = 0, right = -1;
    int sum = 0;
    int gap;
    priority_queue<pair<int, int>> lists;

    while (true)
    {
        if (sum < k)
        {
            ++right;
            if (right == seq.size())
                break;
            sum += seq[right];
            // cout << right << " " << sum << '\n';
        }
        else
        {
            sum -= seq[left];

            if (left == seq.size())
                break;
            left++;
            // cout << left << " " << sum << '\n';
        }
        if (sum == k)
        {
            lists.push({-1 * (right - left), -1 * left});
        }
    }

    gap = -lists.top().first;
    left = -lists.top().second;
    cout << gap << " " << left;

    return answer;
}
int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // freopen("178870_input.txt", "r", stdin);
    vector<int> res = solution({1, 2, 3, 4, 5}, 7);

    for (auto &elem : res)
    {
        cout << elem << " ";
    }

    return 0;
}
