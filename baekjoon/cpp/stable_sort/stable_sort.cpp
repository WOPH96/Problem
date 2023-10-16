#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class User
{
private:
    int age;
    string name;

public:
    User(int age, string name) : age(age), name(name) {}
    bool operator<(const User &U) const { return age > U.age; } // 함수 선언 const -> 매개변수 변경이 불가한 함수임을 명시
    friend ostream &operator<<(ostream &o, const User &u);
};

ostream &operator<<(ostream &o, const User &u)
{
    o << "(" << u.name << ", " << u.age << ")";
    return o;
}
int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<User> Uv;
    for (int i = 0; i < 100; i++)
    {
        string temp = "";
        temp.push_back('a' + i / 26);
        temp.push_back('a' + i % 26);
        Uv.push_back(User(static_cast<int>(rand() % 10), temp));
    }

    vector<User> Uv2 = Uv;

    for (auto &elem : Uv)
    {
        cout << elem << " ";
    }
    cout << "\n\n";

    sort(Uv.begin(), Uv.end());

    for (auto &elem : Uv)
    {
        cout << elem << " ";
    }
    cout << "\n\n";
    stable_sort(Uv2.begin(), Uv2.end());
    for (auto &elem : Uv2)
    {
        cout << elem << " ";
    }
    cout << "\n";
}