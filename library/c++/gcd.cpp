#include<iostream>
using namespace std;

long long GCD(long long a, long long b){
    if(a==0)return b;
    return GCD(b % a, a);
}

/*
返り値はa,bのGCD
a*x + b*y = gcd(a, b)を満たす整数x, yが、変数x, yのアドレスに入る
*/
long long extGCD(long long a, long long b, long long &x, long long &y){
    if(a==0){
        x = 0;
        y = 1;
        return b;
    }
    long long d = extGCD(b%a, a, y, x);
    /*
    Xに入ってほしいのは、Y-b/a*X
    Yに入ってほしいのは、X
    いま、X=y,Y=xなので
    Y-b/a*Xは、x-b/a*yになる。
    */
    x = x - b/a * y;
    return d;
}



int main(){
    cout << GCD(111, 30) << endl;
    long long x, y;
    extGCD(30, 111, x, y);
    cout << x << ' ' << y << endl;
    return 0;
}