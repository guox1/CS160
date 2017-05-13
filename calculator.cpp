#include<iostream>
#include<string>
#include<cmath>
using namespace std;

int main(){
bool user_input = 1;
int num1;
int num2;
int operation;
while(user_input == 1){
  cout<<"Enter your first number: ";
  cin>>num1;

  cout<<"Enter your second number: ";
  cin>>num2;

  cout<<" What kind of operation do you want to use? ";
  cout<<"1) + ";
  cout<<"2) - ";
  cout<<"3) * ";
  cout<<"4) / ";
  cout<<"5) % ";
  cout<<"6) ^ : ";

  cin>>operation;
  if(operation == 1){
  cout<<num1 + num2<<endl;
  }
  if(operation == 2){
  cout<<num1 - num2<<endl;   
  }
  if(operation == 3){
  cout<<num1 * num2<<endl;
  }
  if(operation == 4){
  cout<<num1 / num2<<endl;
  }
  if(operation == 5){
  cout<<num1 % num2<<endl;
  }
  if(operation == 6){
  cout<<pow(num1, num2)<<endl;
  } 
//your code for exponent here
  cout<<"Try again? 0-no, 1-yes: ";
  cin>>user_input;
 }
   return 0;
 }
