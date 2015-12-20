#include <iostream>
#include <string>
#include <list>

using namespace std;


list<string,int> phone_book={
        {"David" ,123}
        {"karl",234}
        {"bert",345}
};


int get_number(const string& s)
{
	for(const auto& x:phone_book)
	if(x.name == s)
	return x.number;

return 0;
}

int main()

{

cout<<get_number("123");

return 0;

}
