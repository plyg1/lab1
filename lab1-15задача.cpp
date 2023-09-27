#include <iostream>
using namespace std;
//Дано змінні A, B, C. Змінити їх значення, перемістивши вміст A в B, B - в C, C - в A, і вивести нові значення змінних A, B, C.
int main() {
	//Begin 15
	float A, B, C, temp ;//деклорація
	//введення
	cout << "Enter A, B and C: ";
	cin >> A >> B >> C;
	//обчислення
	temp = A;
	A = B;
	B = C;
	C = temp ;
	//виведення 
	cout << "A = " << A << endl;
	cout << "B = " << B << endl;
	cout << "C = " << C << endl;
	return 0 ;

} 
