```C++
# include <cstdio>
# include <vector>

using namespace std;
int N, M;
vector<int> graph[1001];

void input(){
    int s, d;
    scanf("%d %d", &N, &M);
    for (int i = 0; i < M; ++i) {
        scanf("%d %d", &s, &d);
        graph[s].push_back(d);
        graph[d].push_back(s);
    }
}

int main(){
    input();
    return 0;
}
