# include <cstdio>
# include <deque>
# define pi pair<int, int>

using namespace std;
int N, M;
int arr[101][101] = {0, };
int dp[101][101] = {0, };

void input(){
    scanf("%d %d", &M, &N);

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            scanf("%1d", &arr[i][j]);   // 정수한개씩 입력받는 방법
            dp[i][j] = -1;
        }
    }
}

int main(){
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};
    int r, c, x, y;
    input();
    deque<pi> queue;
    queue.push_back(make_pair(0, 0));
    dp[0][0] = 0;

    while (!queue.empty()){
        r = queue.front().first;
        c = queue.front().second;
        queue.pop_front();
        for (int i = 0; i < 4; ++i) {
            x = r + dx[i];
            y = c + dy[i];

            if( 0 <= x && x < N){
                if ( 0 <= y && y < M){
                    if( dp[x][y] == - 1 || dp[x][y] > dp[r][c] + arr[x][y]){
                           dp[x][y] = dp[r][c] + arr[x][y];
                           queue.push_back(make_pair(x, y));
                    }
                }
            }
        }

    }


//    for (int i = 0; i < N; ++i) {
//        for (int j = 0; j < M; ++j) {
//            printf("%d ", dp[i][j]);
//        }
//        printf("\n");
//
//    }
    printf("%d", dp[N-1][M-1]);

    return 0;
}
