#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

// GCD , LCM

int gcd(int a, int b)
{
    if (a % b == 0)
        return b;

    return gcd(b, a % b);
}

int main()
{
    // a,b 의 최대공약수 (a>b) = a%b ,b의 최대공약수
    int a, b, c;
    cin >> a >> b >> c;

    int day = 1;
    while (day % a != 0 || day % b != 0 || day % c != 0) // 셋 다 나누어 떨어질때까지
    {
        cout << a << b << c << endl;
        day++;
    }
    cout << day << endl;
    return 0;
}