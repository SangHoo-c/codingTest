# include <deque>
# include <cstdio>
# define pii pair<pair<int, int>, int>
using namespace std;

int M, N;
int arr[1001][1001] = {0,};
int visited[1001][1001] = {0, };
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int r, c;
int cnt;
void input(){
    scanf("%d %d", &N, &M);
    for(int i =0 ; i < M; i ++){
        for(int j = 0 ; j < N; j ++){
            scanf("%d", &arr[i][j]);
        }
    }
}

int main(){
    input();
    cnt = 0;

    deque<pii> queue;
    for (int i = 0; i <M ; ++i) {
        for (int j = 0; j < N; ++j) {
            if(arr[i][j] == 1){
                queue.push_back(make_pair(make_pair(i, j), cnt));
            }
        }
    }

    while (!queue.empty()){
        r = queue.front().first.first;
        c = queue.front().first.second;
        cnt = queue.front().second;
        queue.pop_front();
        int x, y;
        for (int i = 0; i < 4; ++i) {
            x = r + dx[i];
            y = c + dy[i];

            if ( 0 <= x && x < M){
                if( 0 <= y && y < N){
                    if(!visited[x][y] && arr[x][y] == 0){
                        queue.push_back(make_pair(make_pair(x, y), cnt + 1));
                        visited[x][y] = cnt + 1;
                    }
                }

            }


        }
    }
    int _max = -1e9;
    for(int i =0 ; i < M; i ++){
        for(int j = 0 ; j < N; j ++){
//            printf("%d ", visited[i][j]);
            if(arr[i][j] == 0){
                if(visited[i][j] == 0){
                    printf("%d", -1);
                    return 0;
                }
            }
            _max = max(_max, visited[i][j]);
        }
//        printf("\n");
    }
    printf("%d", _max);
    return 0;
}
