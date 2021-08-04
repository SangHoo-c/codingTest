/*
  조합하는 방법 
  1. 3가지 케이스 => 3중 for 문을 돌린다. 
  2. 백트래킹을 사용한다. 
*/

# include <cstdio>
# include <vector>
# include <deque>
# define pi pair<int, int>

using namespace std;
int N, M;
int arr[9][9] = {0, };
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int result = -1;
vector<pi> empty_list;

void input(){
    scanf("%d %d", &N, &M);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            scanf("%d", &arr[i][j]);
            if (arr[i][j] == 0){
                empty_list.push_back(make_pair(i, j));
            }
        }
    }
}

void bfs(){
    deque<pi> queue;
    int visited[9][9] = {0, };
    int r, c, x, y;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if( arr[i][j] == 2){
                queue.push_back(make_pair(i, j));
                visited[i][j] = 2;
            }
            else if (arr[i][j] == 1){
                visited[i][j] = 1;
            }
        }
    }
    while (!queue.empty()){
        r = queue.front().first;
        c = queue.front().second;
        queue.pop_front();

        for (int i = 0; i < 4; ++i) {
            x = r + dx[i];
            y = c + dy[i];

            if ( 0 <= x and x < N and 0 <= y and y < M){
                if(!visited[x][y]){
                    visited[x][y] = 2;
                    queue.push_back(make_pair(x, y));
                }
            }
        }
    }
    int tmp = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (!visited[i][j]){
                tmp += 1;
            }
        }
    }
    result = max(result, tmp);
}

int main(){
    input();
    int x1, y1, x2, y2, x3, y3;

    for (int i = 0; i < empty_list.size(); ++i) {
        for (int j = i + 1; j < empty_list.size(); ++j) {
            for (int k = j + 1; k < empty_list.size(); ++k) {
                x1 = empty_list[i].first;
                y1 = empty_list[i].second;

                x2 = empty_list[j].first;
                y2 = empty_list[j].second;

                x3 = empty_list[k].first;
                y3 = empty_list[k].second;

                arr[x1][y1] = 1;
                arr[x2][y2] = 1;
                arr[x3][y3] = 1;

                bfs();

                arr[x1][y1] = 0;
                arr[x2][y2] = 0;
                arr[x3][y3] = 0;
            }
        }
    }
    printf("%d", result);
    return 0;
}
