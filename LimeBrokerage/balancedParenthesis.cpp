#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
/*
 * Complete the function below.
 */

bool Pair(char opening, char closing){
    if(opening == '(' && closing==')') 
        return true;
    else if(opening == '{' && closing =='}')
        return true;
    else if(opening == '[' && closing ==']')
        return true;
    else
        return false;
}

vector < string > Braces(vector < string > exp) {
    
    stack <char> S;
    vector <string> res;
    for(int j=0;j<exp.size();j++){
        res.push_back("YES");
        for(int i=0;i <exp[j].length();i++ ){
            if(exp[j][i]=='(' || exp[j][i]=='{' || exp[j][i]=='[')
                S.push(exp[j][i]);
            else if(exp[j][i]==')' || exp[j][i]=='}' || exp[j][i]==']'){
                if(S.empty() || !Pair(S.top(),exp[j][i])){
                    res.pop_back();
                    res.push_back("NO");
                    break;
                }

                else
                    S.pop();
                    
            }
        res.push_back("YES");
        }
    }

    return res;
}


int main() {
    ofstream fout(getenv("OUTPUT_PATH"));
    vector < string > res;
    
    int _values_size = 0;
    cin >> _values_size;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n'); 
    vector<string> _values;
    string _values_item;
    for(int _values_i=0; _values_i<_values_size; _values_i++) {
        getline(cin, _values_item);
        _values.push_back(_values_item);
    }
    
    res = Braces(_values);
    for(int res_i=0; res_i < res.size(); res_i++) {
        cout<< res[res_i] << endl;
        cout<<"hello\n";
        fout << res[res_i] << endl;
    }
    
    fout.close();
    return 0;
}
