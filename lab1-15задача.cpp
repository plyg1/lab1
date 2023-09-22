#include <iostream>
using namespace std;
//Äàíî çì³íí³ A, B, C. Çì³íèòè ¿õ çíà÷åííÿ, ïåðåì³ñòèâøè âì³ñò A â B, B - â C, C - â A, ³ âèâåñòè íîâ³ çíà÷åííÿ çì³ííèõ A, B, C.
int main() {
	//Begin 15
	float A, B, C;//äåêëîðàö³ÿ
	//ââåäåííÿ
	cout << "Enter A, B and C: ";
	cin >> A >> B >> C;
	//îá÷èñëåííÿ
	A = B;
	B = C;
	C = A;
	//âèâåäåííÿ 
	cout << "A = " << A << endl;
	cout << "B = " << B << endl;
	cout << "C = " << C << endl;
	return;

}
