# include <cstdio>
# include <vector>
# include <queue>
# include <algorithm>
using namespace std;

void dfs(vector<int> *v, int start, int* check){
    check[start] = 1;
    printf("%d ", start);

    for(int i = 0; i < v[start].size(); i ++){
        if(check[v[start].at(i)] != 1){
            dfs(v, v[start].at(i), check);
        }
    }
}

void bfs(vector<int>* v, int start, int* check){
    queue<int> q;
    check[start] = 1;
    q.push(start);

    while (!q.empty()){
        int node = q.front();
        q.pop();
        printf("%d ", node);
        for(int i =0 ; i< v[node].size(); i ++){
            if(check[v[node].at(i)] != 1){
                check[v[node].at(i)] = 1;
                q.push(v[node].at(i));
            }
        }

    }
}



int main(void){
    int N, M, V;
    scanf("%d %d %d", &N, &M, &V);

    vector<int> graph[N+1];

    for(int i = 0 ; i < M; i++){
        int start, end;
        scanf("%d %d", &start, &end);
        graph[start].push_back(end);
        graph[end].push_back(start);
    }

    for(int i = 0; i< N +1; i ++){
        sort(graph[i].begin(), graph[i].end());
    }

    int dfs_check[1001] = {0, };
    int bfs_check[1001] = {0, };
    dfs(graph, V, dfs_check);
    printf("\n");
    bfs(graph, V, bfs_check);
    return 0;

}
