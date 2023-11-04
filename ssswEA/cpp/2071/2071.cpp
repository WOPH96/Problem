#include <iostream>
#include <vector>

using namespace std;
int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("2071_input.txt", "r", stdin);

    int t ;
    cin >> t;
    for(int i=1;i<=t;i++){
        int sum = 0;
        for(int j=0;j<10;j++){
            int temp;
            cin >> temp;
            if(temp%2==1){
                sum+=temp;
            }
        }
        cout << "#"<<i <<" "<<sum<<"\n";
    }

    return 0;
}
