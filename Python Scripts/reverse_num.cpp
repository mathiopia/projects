#include <iostream>
#include <math.h1>
using namespace std;
int main (){
int reminder,number, rev_num =0 ;
char q;

 

   cout<<" input number: "; 
cin >> number; 
while(number>0) {
  
reminder=number % 10;
number =number /10;
rev_num=abs((rev_num*10)+reminder);
}
cout <<"the reverse number is: "  <<rev_num;


return 0;
}