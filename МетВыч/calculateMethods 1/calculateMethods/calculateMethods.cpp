#include <iostream>
#include <iomanip>
#include <vector>
#include <string>

#include <stdlib.h>
#include <stdio.h>
#include <math.h>


using namespace std;

using type = double;

struct point {
    type x;
    type f;
};

void print(vector<vector<type>> &m, int N)
{
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            printf("%.1lf ", m[i][j]);
        }
        puts("");
    }
    puts("");
}

void printF(vector<vector<type>> &m, int N, vector<point>&ps) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            printf("%.1lf  ", m[i][j]);
        }
        printf("%s  ", "|");
        printf("%.1lf  ", ps[i].f);
        puts("");
    }
    puts("");
}

type GaussDet(vector<vector<type>> &m, int n)
{
    type det = 1;
    for (int i = 0; i < n; ++i)
    {
        type mx = fabs(m[i][i]);
        int idx = i;
        for (int j = i + 1; j < n; ++j)
            if (mx < fabs(m[i][j])) mx = fabs(m[i][idx = j]);
        if (idx != i)
        {
            for (int j = i; j < n; ++j)
            {
                type t = m[j][i];
                m[j][i] = m[j][idx];
                m[j][idx] = t;
            }
            det = -det;
        }
        for (int k = i + 1; k < n; ++k)
        {
            type t = m[k][i] / m[i][i];

            for (int j = i; j < n; ++j)
                m[k][j] -= m[i][j] * t;
        }
    }
    for (int i = 0; i < n; ++i) det *= m[i][i];
    return det;
}




int main()
{
    setlocale(LC_ALL, "Russian");
    cout << setprecision(4);

    int n;
    cout << "Введите количество точек: ";
    cin >> n;

    vector<point> points(n);
    cout << "Введите точки и значения в них функции f в формате \"x f(x)\":\n";
    for (int i = 0; i < n; ++i)
        cin >> points[i].x >> points[i].f;


    cout << "1) Таблица для f(x):\n";
    cout << "x:    ";
    for (int i = 0; i < n; ++i) {
        cout << setw(6) << points[i].x;
    } cout << "\n";
    cout << "f(x): ";
    for (int i = 0; i < n; ++i) {
        cout << setw(6) << points[i].f;
    } cout << "\n";

    vector<vector<type>> matr(n, vector<type>(n));
    for (int i = 0; i < n; ++i) {
        matr[i][n - 1] = 1;
        for (int j = n - 2; j >= 0; --j)
            matr[i][j] = matr[i][j + 1] * points[i].x;
    }


    cout << "2) Вспомогательная СЛАУ в виде расширенной матрицы:\n";
    printF(matr, n, points);


    cout << "3) Решения СЛАУ:\n";

    vector<type> dets(n + 1);
    {
        vector<vector<type>> matr_ = matr;
        dets[n] = GaussDet(matr_, n);
    }
    for (int j = 0; j < n; ++j) {
        vector<vector<type>> matr_ = matr;
        for (int i = n - 1; i >= 0; --i)
            matr_[i][j] = points[i].f;
        dets[j] = GaussDet(matr_, n);
    }

    vector<type> a(n);
    for (int i = 0; i < n; ++i) a[i] = dets[i] / dets[n];
    for (int i = 0; i < n; ++i) {
        cout << setw(6) << "a" + to_string(i);
    } cout << "\n";
    for (int i = 0; i < n; ++i) {
        cout << setw(6) << a[i];
    } cout << "\n";


    cout << "4) Заполнение таблицы для P(x):\n";
    vector<point> pointsP(2 * n - 1);
    pointsP[0] = points[0];
    for (int i = 1; i < pointsP.size(); i += 2) {
        pointsP[i + 1] = points[(i + 1) / 2];
        type x = (pointsP[i - 1].x + pointsP[i + 1].x) / 2;
        type f = 0, xx = 1;
        for (int j = 0; j < n; ++j) {
            f += xx * a[j];
            xx *= x;
        }
        pointsP[i] = {x,  f};
    }
    cout << "x:    ";
    for (int i = 0; i < pointsP.size(); ++i) {
        cout << setw(7) << pointsP[i].x;
    } cout << "\n";
    cout << "P(x): ";
    for (int i = 0; i < pointsP.size(); ++i) {
        cout << setw(7) << pointsP[i].f;
    } cout << "\n";
}

