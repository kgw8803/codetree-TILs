#include <iostream>

using namespace std;

int main() {
	int n;
	int arr[10] = {};
	for (size_t i = 0; i < 10; i++)
	{
		cin >> n;
		arr[i] = n;
	}
	cout << arr[2] + arr[4] + arr[9];
	return 0;
}