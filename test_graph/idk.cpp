#include <iostream>

int main(){
	using namespace std;
	int x;
	cout << "Hello World" << endl;
	cin >> x;

	vector<int> v;
	v.resize(x);

	for (int i=0; i<x; i++){
		cin >> v[i];
	}
	std::sort(v);
}