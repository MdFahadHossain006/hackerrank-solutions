// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/challenges/arrays-introduction/problem?isFullScreen=true
// Problem     Arrays Introduction
// Difficulty  Easy
// Subdomain   Introduction
// Platform    HackerRank
// Language    cpp
// Status      Accepted
// Submitted   2026-11-18, 01:22 a.m.
// ──────────────────────────────────────────────────

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    // Use a vector (or int arr[n]) to store n integers
    vector<int> arr(n);
    
    // Read the array elements from left to right
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    // Print the elements in reverse order from index n - 1 down to 0
    for (int i = n - 1; i >= 0; i--) {
        cout << arr[i] << " ";
    }
    
    return 0;
} 
