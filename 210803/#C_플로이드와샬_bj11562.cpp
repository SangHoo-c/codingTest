# include <cstdio>
# define INF 1e9
int N, M, K;
int adj[251][251] = {0, };

void input(){
    int u, v, b;
    scanf("%d %d", &N, &M);

    // init
    for (int i = 1; i < N+1; ++i) {
        for (int j = 1; j < N+1; ++j) {
            adj[i][j] = INF;
        }
    }

    // set value
    for (int i = 0; i < M; ++i) {
        scanf("%d %d %d", &u, &v, &b);
        if(b == 0){
            adj[u][v] = 0;
            adj[v][u] = 1;
        }
        else{
            adj[u][v] = 0;
            adj[v][u] = 0;
        }
    }
}

void fw(){
    for (int i = 1; i < N+1; ++i) {
        adj[i][i] = 0;
    }
    for (int k = 1; k < N+1; ++k) {
        for (int i = 1; i < N+1; ++i) {
            for (int j = 1; j < N+1; ++j) {
                if(adj[i][j] > adj[i][k] + adj[k][j]){
                    adj[i][j] = adj[i][k] + adj[k][j];
                }
            }
        }
    }
}

int main(){
    int s, d;
    input();
    fw();
    scanf("%d", &K);
    for (int i = 0; i < K; ++i) {
        scanf("%d %d", &s, &d);
        printf("%d\n", adj[s][d]);
    }
    return 0;
}
