# include <cstdio>
# include <vector>

using namespace std;
int N, M;
vector<int> graph[1001];
int visited[1001] = {0,};

void input(){
    int s, d;
    scanf("%d %d", &N, &M);
    for (int i = 0; i < M; ++i) {
        scanf("%d %d", &s, &d);
        graph[s].push_back(d);
        graph[d].push_back(s);
    }
}

void dfs(int idx){
    if(!visited[idx]){
        visited[idx] = 1;

        for(int nxt_idx : graph[idx]){
            dfs(nxt_idx);
        }
    }
}

int main(){
    input();
    int cnt = 0;
    for (int i = 1; i <= N; ++i) {
        if(!visited[i]){
            dfs(i);
            cnt += 1;
        }
    }
    printf("%d", cnt);
    return 0;
}
