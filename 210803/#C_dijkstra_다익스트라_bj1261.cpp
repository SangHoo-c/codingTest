/*
TIP
1. 정수 한개씩 입력받는 방법
2. C++ 최소힙 만드는 방법 
*/


# include <cstdio>
# include <deque>
# include <queue>
# define pii pair<int, pair<int, int>>


using namespace std;
int N, M;
int cost[101][101] = {0, };
int dp[101][101] = {0, };
int visited[101][101] = {0,};

void input(){
    scanf("%d %d", &M, &N);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            scanf("%1d", &cost[i][j]);   // 정수한개씩 입력받는 방법
            dp[i][j] = -1;
        }
    }
}

void djs(int x1, int y1){
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};
    int r, c, x, y, prv_cost;
    priority_queue<pii, vector<pii>, greater<pii>> heap;    // greater 을 넣어줘서 최소힙을 만든다. (pii 의 첫번째 원소를 기준으로)
    heap.push(make_pair(cost[x1][y1], make_pair(x1, y1)));

    while (!heap.empty()){
        r = heap.top().second.first;
        c = heap.top().second.second;
        prv_cost = heap.top().first;
        heap.pop();
        if(dp[r][c] == -1)
            dp[r][c] = prv_cost;

        for (int i = 0; i < 4; ++i) {
            x = r + dx[i];
            y = c + dy[i];

            if( 0 <= x and x < N and 0 <= y and y < M){
                if ( dp[x][y] == - 1 and visited[x][y] == 0){
                    heap.push(make_pair(prv_cost + cost[x][y] , make_pair(x, y)));
                    visited[x][y] = 1;
                }
            }
        }
    }
}



int main(){
    input();
    djs(0, 0);
    printf("%d", dp[N-1][M-1]);

    return 0;
}
