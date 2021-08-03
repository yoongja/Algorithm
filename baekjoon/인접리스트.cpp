#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

enum { A, B, C, D ,E};

void AddGraph(vector<int> * v, int x, int y) {
    v[x].push_back(y);
    v[y].push_back(x);
}

int main(void) {

    vector<int> g[5];

    AddGraph(g, A, B);    //A <-> B 연결
    AddGraph(g, A, D);    //A <-> D 연결
    AddGraph(g, B, C);    //B <-> C 연결
    AddGraph(g, C, D);    //C <-> D 연결
    AddGraph(g, D, E);    //D <-> E 연결
    AddGraph(g, E, A);    //E <-> A 연결

    for (int i = 0; i <= E; i++) {
        printf("%c와 연결된 정점 : ", i + 65);
        for_each(g[i].begin(), g[i].end(), [&](auto& s) {
            printf("%c ", s + 65);
        });
        cout << endl;
    }

    return 0;
}