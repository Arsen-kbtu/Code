#include <iostream>
using namespace std;
bool isPrime(int n){
    if(n==2){
        return true;
    }
    if(n%2==0||n==1){
        return false;
    }
    for(int i=3; i<n/2; i++){
        if(n%i==0){
            return false;
        }
    }
    return true;
}
int main(){
    int n;
    cin>>n;
    if(isPrime(n)){
        cout<<"YES";
        return 0;
    }
    cout<<"NO";
}