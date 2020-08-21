// P_4_7 greedy, using PQ
#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

int main() {
    int n;
    scanf("%d", &n); assert(n<200000);
    priority_queue<LL> PQ;
    for (int i=0; i<n; i++) {
        int m;
        scanf("%d", &m);
        PQ.push(-(LL)m); // change sign (to find minimum)
    }
    LL cost=0; // total cost
    for (int i=0; i<n-1; i++) { // merge n-1 times
        // merge the smallest two sets
        LL m=PQ.top();
        PQ.pop();
        m += PQ.top();
        PQ.pop();
        PQ.push(m);
        cost += m;
    }
    printf("%lld\n%lld\n", -PQ.top(), -cost);
	return 0;
}
