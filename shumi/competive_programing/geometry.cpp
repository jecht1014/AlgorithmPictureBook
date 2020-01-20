#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for(int i = 0; i < n; i++)

double error = 0.000001;

double distance(pair<double, double>xy1, pair<double, double>xy2) {
    return hypot(xy1.first - xy2.first, xy1.second - xy2.second);
}

bool in_circle(double r, pair<double, double> coordinate, vector<pair<double, double>> xy) {
    bool judge = true;
    for (int i = 0; i < xy.size(); i++) {
        if (distance(xy[i], coordinate) > r+error) {
            judge = false;
            break;
        }
    }
    return judge;
}

bool check_line(pair<double, double>xy1, pair<double, double>xy2, pair<double, double>xy3) {
    return (abs((xy2.second-xy1.second)/(xy2.first-xy1.first) - (xy3.second-xy2.second)/(xy3.first-xy2.first)) < error);
}

pair<double, double> calc_circumcenter(pair<double, double>xy1, pair<double, double>xy2, pair<double, double>xy3) {
    double a = xy1.first;
    double b = xy1.second;
    double c = xy2.first;
    double d = xy2.second;
    double e = xy3.first;
    double f = xy3.second;
    
    double x;
    double y = (((e-a)*(a*a+b*b-c*c-d*d)-(c-a)*(a*a+b*b-e*e-f*f)) / (2*(e-a)*(b-d) -2*(c-a)*(b-f)));
    if (c-a != 0)
        x = (2*(b-d)*y-a*a-b*b+c*c+d*d) / (2*(c-a));
    else
        x = (2*(b-f)*y-a*a-b*b+e*e+f*f) / (2*(e-a));
    return make_pair(x, y);
}

int main(void){
    int n;
    cin >> n;
    vector<pair<double, double>> xy(n);
    rep(i, n) {
        double x, y;
        cin >> x >> y;
        xy[i] = make_pair(x, y);
    }
    
    double min_r = 1000;
    for (int i = 0; i < n-1; i++) {
        for (int j = i+1; j < n; j++) {
            double r = distance(xy[i], xy[j]) / 2;
            pair<double, double> center = make_pair((xy[i].first + xy[j].first)/2, (xy[i].second + xy[j].second)/2);
            if (in_circle(r, center, xy))
                min_r = min(min_r, r);
        }
    }
    
    for (int i = 0; i < n-2; i++) {
        for (int j = i+1; j < n-1; j++) {
            for (int k = j+1; k < n; k++) {
                if (!check_line(xy[i], xy[j], xy[k])) {
                    pair<double, double> center = calc_circumcenter(xy[i], xy[j], xy[k]);
                    double r = distance(center, xy[i]);
                    if (in_circle(r, center, xy))
                        min_r = min(min_r, r);
                }
            }
        }
    }
    
    cout << fixed << setprecision(10) << min_r << endl;
}