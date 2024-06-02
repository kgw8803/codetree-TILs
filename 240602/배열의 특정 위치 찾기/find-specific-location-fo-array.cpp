#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	int arr[10];
	for (size_t i = 0; i < 10; i++)
	{
		cin >> arr[i];
	}
	int sum = 0;
	for (size_t i = 0; i < 10; i += 2)
	{
		sum += arr[i + 1];
	}
	double average;
	average = (double)(arr[2] + arr[5] + arr[8]) / (double) 3;
	cout << sum << " " << fixed << setprecision(1) << average;
	
	
}