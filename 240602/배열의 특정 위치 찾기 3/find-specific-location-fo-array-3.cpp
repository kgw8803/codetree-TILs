#include <iostream>

using namespace std;

int main() {
	const int MAX_SIZE = 100;
	int arr[MAX_SIZE];
	int count = 0;
	int num;

	while (cin >> num && count < MAX_SIZE) {
		arr[count++] = num;
		if (num == 0 && count >= 4) {
			break;
		}
	}

	
	for (int i = 3; i < count; ++i) {
		if (arr[i] == 0) {
			int sum = arr[i - 1] + arr[i - 2] + arr[i - 3];
			cout << sum <<std::endl;
			break;
		}
	}

	return 0;
}