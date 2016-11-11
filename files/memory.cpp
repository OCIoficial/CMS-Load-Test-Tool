#include <bits/stdc++.h>
using namespace std;

int limit = 10000000;

int main(){
    vector<vector<int> > v;
    for (int i = 0; i < limit; i++){
        vector<int> vv;
        for (int ii = 0; ii < limit; ii++){
            vv.push_back(ii);
        }
        v.push_back(vv);
        cout << v[i][500] << '\n';
    }
    return 0;
}
