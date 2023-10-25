#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

// iterable container 받아서, 조합 반환
template <typename T>
void combination(vector<T> &vec, int r, vector<vector<T>> &res, bool selected[], int depth = 0, int idx = 0)
{
    if (depth == r)
    {
        vector<T> temp;
        for (int i = 0; i < vec.size(); i++)
        {
            if (selected[i] == true)
            {
                temp.push_back(vec[i]);
            }
        }
        res.push_back(temp);
    }
    for (int i = idx; i < vec.size(); i++)
    {
        if (selected[i] == true)
            continue;
        selected[i] = true;
        combination(vec, r, res, selected, depth + 1, i);
        selected[i] = false;
    }
}

// iterable container 받아서, 순열 반환
template <typename T>
void permutation(vector<T> &vec, int r, vector<vector<T>> &res, bool selected[], vector<T> &temp, int depth = 0)
{

    if (depth == r)
    {
        res.push_back(temp);
    }

    for (int i = 0; i < vec.size(); i++)
    {
        if (selected[i] == true)
            continue;
        selected[i] = true;
        temp.push_back(vec[i]);
        permutation(vec, r, res, selected, temp, depth + 1);
        temp.pop_back();
        selected[i] = false;
    }
}

int main()
{
    string s = "1234";
    const int len = s.size();

    vector<char> vec_string;
    vector<vector<char>> res;
    vector<char> temp;
    bool selected[len];
    memset(selected, false, len);
    for (auto &elem : s)
    {
        vec_string.push_back(elem);
    }

    // combination(vec_string, 2, res, selected);
    for (int i = 0; i < res.size(); i++)
    {
        for (auto &elem : res[i])
        {
            cout << elem << " ";
        }
        cout << "\n";
    }
    memset(selected, false, len);
    permutation(vec_string, 2, res, selected, temp);
    for (int i = 0; i < res.size(); i++)
    {
        for (auto &elem : res[i])
        {
            cout << elem << " ";
        }
        cout << "\n";
    }
    return 0;
}
