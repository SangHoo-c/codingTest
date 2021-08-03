# include <cstdio>


int N, M;
int arr[201][201] = {0, };
int check[10001]= {0, };
int parent[201] = {0, };

void input(){
    scanf("%d", &N);
    scanf("%d", &M);

    for (int i = 1; i < N + 1; ++i) {
        for (int j = 1; j < N + 1; ++j) {
            scanf("%d", &arr[i][j]);
        }
    }
    for (int i = 0 ; i < M ; i ++){
        scanf("%d", &check[i]);
    }
}

void init(){
    for (int i = 1; i < N + 1; ++i) {
        parent[i] = i;
    }
}

int get_parent(int idx){
    if(parent[idx] == idx){
        return idx;
    }
    parent[idx] = get_parent(parent[idx]);
    return parent[idx];
}

int main(){
    int p_i, p_j;
    input();
    init();
    for (int i = 1; i < N+1; ++i) {
        for (int j = 1; j < N+1; ++j) {
            if(arr[i][j] == 1){
                p_i = get_parent(i);
                p_j = get_parent(j);

                if( p_i < p_j){
                    parent[p_j] = p_i;
                }
                else{
                    parent[p_i] = p_j;
                }
            }
        }
    }

    for (int i = 0; i < M-1; ++i) {
        if( parent[check[i]] != parent[check[i+1]]){
            printf("%s", "NO");
            return 0;
        }
    }
    printf("%s", "YES");
    return 0;
}
