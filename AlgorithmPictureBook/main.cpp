#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int lim = 10000000;

int main() {
    vector<vector<int>> hen({{1, 2}, {0, 2, 3, 4}, {0, 1, 3, 5}, {1, 2, 4, 5}, {1, 3, 5, 6}, {2, 3, 4, 6}, {4, 5}});
    vector<vector<int>> weight({{9, 2}, {9, 6, 3, 1}, {2, 6, 2, 9}, {3, 2, 5, 6}, {1, 5, 3, 7}, {9, 6, 3, 4}, {7, 4}});
    vector<int> hen_min({0, lim, lim, lim, lim, lim, lim});

    int start = 0;
    int end = 6;

    // ベルマンフォード
    /*
    for (int i = 0; i < hen.size() ; i++)
        for (int j = 0; j < hen.size(); j++)
            for (int k = 0; k < hen[j].size(); k++)
                if (hen_min[hen[j][k]] > hen_min[j]+weight[j][k])
                    hen_min[hen[j][k]] = hen_min[j]+weight[j][k];
    */

    // ダイクストラ法
    vector<int> koho({0});
    vector<int> value({0});
    vector<int> tansakuzumi;
    while(!koho.empty()) {
        auto min_value = *min_element(value.begin(), value.end());
        int min_index = distance(value.begin(), min_value);
        int min_koho = koho[min_index];

        tansakuzumi.append(koho);
        koho.erase(koho.begin()+min_index);
        value.erase(value.begin()+min_index);
        for (int i = 0; i < hen[min_koho].size(); i++) {
            auto tansakuzumi_exist = find(tansakuzumi.begin(), tansakuzumi.end(), min_index)
            auto koho_exist = find(koho.begin(), koho.end(), min_index)
            if (tansakuzumi_exist == tansakuzumi.end()) {
                if (koho_exist == koho.end()) {
                    koho.append(hen[min_index][i]);
                    value.append(hen_min[min_koho] + weight[min_koho][i]);
                }
                else {
                    if (hen_min[])
                }
            }
        }
    }

    for (int j = 0; j < hen.size(); j++)
        cout << hen_min[j] << endl;
}