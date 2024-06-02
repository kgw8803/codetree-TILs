#include <iostream>

using namespace std;

int main() {
	
	int arr[10];
	int a = 0;
	int b = 0;
	for (int i = 0; i < 9; i++)
	{	
		cin >> arr[i];
		if (i % 2 == 0) {
			a += arr[i];
		}
		else {
			b += arr[i];
		}
	}
	if (a >= b) {
		cout << a - b;
	}
	else {
		cout << b - a;
	}

	return 0;
}