#include <iostream>
#include <Windows.h>
using namespace std;


int main() {
	//Begin15
	int A = 34, B = 45, C = 76;
	A = B;
	B = C;
	C = A;
	SetConsoleOutputCP(1251);
	SetConsoleCP(1251);
	cout << " Çì³ííà A â Â: " << A << endl;
	cout << " Çì³ííà Â â Ñ: " << B << endl;
	cout << " Çì³ííà Ñ â À: " << C << endl;
}
