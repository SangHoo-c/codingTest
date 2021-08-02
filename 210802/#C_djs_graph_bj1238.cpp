# include <cstdio>
# include <vector>
# include <queue>
# define pii pair<int, int>

using namespace std;

int N, M, X;
const int INF = 1e9;
vector<pii> graph[1001];
vector<int> dist;
int result[1001];

void input(){
    int s, d, cost;
    scanf("%d %d %d", &N, &M, &X);
    for(int i =0 ; i< M; i++){
        scanf("%d %d %d", &s, &d, &cost);
        graph[s].push_back(make_pair(cost, d));
    }
}


void djs(int st){
    dist.clear();
    dist.resize(N+1, INF);

    dist[st] = 0;
    priority_queue<pii, vector<pii>, greater<pii>> heap;
    heap.push({0, st});

    while (!heap.empty()){
        int cur_cost = heap.top().first;
        int now = heap.top().second;
        heap.pop();

        if(cur_cost > dist[now]) continue;

        for(int i =0 ;i < graph[now].size(); i ++){
            int next = graph[now][i].second;
            int next_cost = cur_cost + graph[now][i].first;

            if(next_cost < dist[next]){
                dist[next] = next_cost;
                heap.push({next_cost, next});
            }
        }
    }
}

int main(){
    input();
    for(int i = 1; i < N + 1; i ++){
        djs(i);
        // half : i 가 X 로 가는 최단 거리
        result[i] = dist[X];
    }

    djs(X);
    int res = 0;
    for(int i = 1; i < N + 1; i ++){
        result[i] += dist[i];
        res = max(res, result[i]);
    }
    printf("%d", res);
    return 0;
}


