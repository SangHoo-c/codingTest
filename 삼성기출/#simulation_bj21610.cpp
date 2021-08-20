#include <cstdio>
#include <vector>

using namespace std;

int main(){
    int N, M;
    int arr[51][51] = {0,};
    int goorm[51][51] = {0,};
    int dx[9] = {0, -1, -1, -1, 0, 1, 1, 1};
    int dy[9] = {-1, -1, 0, 1, 1, 1, 0, -1};
    scanf("%d %d", &N, &M);

    goorm[N][1] = 1;
    goorm[N][2] = 1;
    goorm[N-1][1] = 1;
    goorm[N-1][2] = 1;

    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= N; ++j) {
            scanf("%d", &arr[i][j]);
        }
    }

    for (int t = 0; t < M; ++t) {
        int s, d;
        scanf("%d %d", &d, &s);
        d -= 1;

        // 1. 구름 이동
        int new_goorm[51][51] = {0,};
        int nx, ny;
        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= N; ++j) {
                if(goorm[i][j] == 1){
                    nx = i + dx[d] * s;
                    ny = j + dy[d] * s;
                    nx = ( 50 * N + nx) % N;
                    ny = ( 50 * N + ny) % N;

                    if (nx == 0) nx = N;
                    if (ny == 0) ny = N;
                    new_goorm[nx][ny] = 1;
                }
            }
        }

        // 2. 비내림
        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= N; ++j) {
                if (new_goorm[i][j] == 1){
                    arr[i][j] += 1;
                }
            }
        }

        // 3. 물복사
        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= N; ++j) {
                if (new_goorm[i][j] == 1){
                    new_goorm[i][j] = -1;
                    int d[4] = {1, 3, 5, 7};
                    int cnt = 0;
                    for (int k = 0; k < 4; ++k) {
                        nx = i + dx[d[k]];
                        ny = j + dy[d[k]];
                        if (1 <= nx and nx <= N and 1 <= ny and ny <= N){
                            if(arr[nx][ny] > 0){
                                cnt += 1;
                            }
                        }
                    }
                    arr[i][j] += cnt;
                }
            }
        }



        // 4. 구름 생성
        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= N; ++j) {
                if (new_goorm[i][j] == -1) continue;
                if (arr[i][j] >= 2){
                    new_goorm[i][j] = 1;
                    arr[i][j] -= 2;
                }
            }
        }

        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= N; ++j) {
                if(new_goorm[i][j] == 1){
                    goorm[i][j] = 1;
                }
                else{
                    goorm[i][j] = 0;
                }
            }
        }
    }
    int sum = 0;
    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= N; ++j) {
            sum += arr[i][j];
        }
    }
    printf("%d", sum);
    return 0;
}
