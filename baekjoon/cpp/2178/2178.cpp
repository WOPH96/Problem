#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
using namespace std;

// vector<string> split(string str, char Delimiter) {
//     istringstream iss(str);             // istringstream에 str을 담는다.
//     string buffer;                      // 구분자를 기준으로 절삭된 문자열이 담겨지는 버퍼

//     vector<string> result;

//     // istringstream은 istream을 상속받으므로 getline을 사용할 수 있다.
//     while (getline(iss, buffer, Delimiter)) {
//         result.push_back(buffer);               // 절삭된 문자열을 vector에 저장
//     }

//     return result;
// }
vector<int> graph[101];
int n, m;

void bfs(int sx, int sy)
{
    queue<pair<int, int>> q;
    q.push(make_pair(sx, sy));
    cout << q.size() << endl;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    freopen("2178_input.txt", "r", stdin);

    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        string load;
        cin >> load;
        for (auto &elem : load)
        {
            graph[i].push_back(elem - '0');
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (auto &elem : graph[i])
            cout << elem;
        cout << endl;
    }

    return 0;
}
