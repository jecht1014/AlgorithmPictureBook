#include <iostream>
#include <vector>
using namespace std;

int lim = 10000000;

int main() {
    vector<vector<int>> hen({{1, 2}, {0, 2, 3, 4}, {0, 1, 3, 5}, {1, 2, 4, 5}, {1, 3, 5, 6}, {2, 3, 4, 6}, {4, 5}});
    vector<vector<int>> weight({{9, 2}, {9, 6, 3, 1}, {2, 6, 2, 9}, {3, 2, 5, 6}, {1, 5, 3, 7}, {9, 6, 3, 4}, {7, 4}});
    vector<int> hen_min({0, lim, lim, lim, lim, lim, lim});

    int start = 0;
    int end = 6;
    for (int i = 0; i < hen.size() ; i++)
        for (int j = 0; j < hen.size(); j++)
            for (int k = 0; k < hen[j].size(); k++)
                if (hen_min[hen[j][k]] > hen_min[j]+weight[j][k])
                    hen_min[hen[j][k]] = hen_min[j]+weight[j][k];

    for (int j = 0; j < hen.size(); j++)
        cout << hen_min[j] << endl;
}