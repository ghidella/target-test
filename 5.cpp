#include <iostream>
#include <string>

using namespace std;

int main(){
    string entrada, invertida;
    entrada = "qualquer coisa";

    for(int i = entrada.length() - 1; i >= 0; i--){
        invertida += entrada[i];
    }

    cout<<invertida<<endl;

    return 0;
}