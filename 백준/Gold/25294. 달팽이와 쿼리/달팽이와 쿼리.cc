#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#define FASTIO cin.tie(0); cout.tie(0);
#define MAX 5000

using namespace std;
int Q, N, X, Y, Z;
vector<int> Vec[MAX];

void init() {
    Vec[0].push_back(0);
    Vec[0].push_back(1);
    int Number = 0;
    for (int i = 1; i < MAX; i++) {
        Number += 8;
        Vec[i].push_back(0);
        Vec[i].push_back(Number);
        for (int j = 1; j < Vec[i - 1].size(); j++) {
            Vec[i].push_back(Vec[i - 1][j] + Number);
        }
    }
}

void first_Query() {
    if (((N / 2) + 1 == X) && ((N / 2) + 1 == Y)) {
        cout << N * N << "\n";
    }
    int Center = (N / 2) + 1;
    int SubX = abs(Center - X);
    int SubY = abs(Center - Y);
    int Big = max(SubX, SubY);
    int Number = Center - Big;
    int Start = Vec[N / 2][Number - 1] + 1;
    int Len = N - ((Number - 1) * 2);
    int CurX = Number;
    int CurY = Number;
    Len--;
    for (int i = 0; i < Len; i++) {
        if ((CurX == X) && (CurY == Y)) {
            cout << Start << "\n";
            return;
        }
        CurY++;
        Start++;
    }
    for (int i = 0; i < Len; i++) {
        if ((CurX == X) && (CurY == Y)) {
            cout << Start << "\n";
            return;
        }
        CurX++;
        Start++;
    }
    for (int i = 0; i < Len; i++) {
        if ((CurX == X) && (CurY == Y)) {
            cout << Start << "\n";
            return;
        }
        CurY--;
        Start++;
    }
    for (int i = 0; i < Len; i++) {
        if ((CurX == X) && (CurY == Y)) {
            cout << Start << "\n";
            return;
        }
        CurX--;
        Start++;
    }
}

void second_Query() {
    if (N * N == Z) {
        cout << (N / 2) + 1 << " " << (N / 2) + 1 << "\n";
        return;
    }
    int Number = 0;
    int Start = 0;
    for (int i = 1; i < Vec[N / 2].size(); i++) {
        int Cur = Vec[N / 2][i - 1];
        int Next = Vec[N / 2][i];
        if ((Z > Cur) && (Z <= Next)) {
            Number = i;
            Start = Cur + 1;
            break;
        }
    }
    int Len = N - ((Number - 1) * 2);
    for (int i = 0; i < Len; i++) {
        if (Z == Start) {
            cout << Number << " " << Number + i << "\n";
            return;
        }
        Start++;
    }
    Len--;
    for (int i = 0; i < Len; i++) {
        if (Z == Start) {
            cout << Number + 1 + i << " " << N - Number + 1 << "\n";
            return;
        }
        Start++;
    }
    for (int i = 0; i < Len; i++) {
        if (Z == Start) {
            cout << N - Number + 1 << " " << N - Number - i << "\n";
            return;
        }
        Start++;
    }
    Len--;
    for (int i = 0; i < Len; i++) {
        if (Z == Start) {
            cout << N - Number - i << " " << Number << "\n";
            return;
        }
        Start++;
    }
}

void input() {
    cin >> Q;
    while (Q--) {
        int I;
        cin >> I;
        if (I == 1) {
            cin >> N >> X >> Y;
            first_Query();
        }
        else if (I == 2) {
            cin >> N >> Z;
            second_Query();
        }
    };
}

int main() {
    FASTIO
    init();
    input();

    return 0;
}