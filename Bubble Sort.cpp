#include <iostream>
using namespace std;

void BubbleSort(int arr[], int n) {
    int temp = 0;
    for (int k = 0; k < n - 1; k++) {
        for (int i = 0; i < n - k - 1; i++) {
            // Compare adjacent elements
            if (arr[i] > arr[i + 1]) {
                // Swap if the current element is greater than the next element
                temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
            }
        }
    }
    
    cout << "Sorted Array: " << endl;
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl; // Added for better formatting
}

int main() {
    int arr[6] = {10, 1, 7, 6, 14, 9};
    BubbleSort(arr, 6); // Calling the BubbleSort function
    return 0; // Added return statement for main function
}
