// C++ Program to print all prime factors
// of a number using nested loop

#include <bits/stdc++.h>
using namespace std;

// A function to print all prime factors of a given number n
void primeFactors(int n)
{int c;
	// Print the number of 2s that divide n
	while (n % 2 == 0) {
		c++;
		n = n / 2;
	}
cout << "2 the power of "<<c;
	// n must be odd at this point. So we can skip
	// one element (Note i = i +2)
	for (int i = 3; i <= sqrt(n); i = i + 2) {
		// While i divides n, print i and divide n
		while (n % i == 0) {
			cout << i<<endl;
			n = n / i;
            i++;
		}
	}

	// This condition is to handle the case when n
	// is a prime number greater than 2
	if (n > 2)
		cout << n;
}

/* Driver program to test above function */
int main()
{
	int n;
    cout<< "enter number ";
    cin >> n;
	primeFactors(n);
	return 0;
}
