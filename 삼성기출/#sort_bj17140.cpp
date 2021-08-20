/*
  1. r / c 구분
  2. count
  3. sort
  4. renewal
*/


# include <cstdio>
# include <algorithm>
# include <vector>
# define pii pair<int, int>

using namespace std;


int compare(pii a, pii b){
    if(a.second == b.second){
        return a.first < b.first;
    }
    return a.second < b.second;
}


int main(){
    int R, C, K;
    int r, c;
    vector<pii> v;
    r = 3;
    c = 3;
    scanf("%d %d %d", &R, &C, &K);
    int arr[101][101] = {0, };
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            scanf("%d", &arr[i][j]);
        }
    }

    for (int t = 0; t < 101; ++t) {
        int new_ar[101][101] = {0, };
        if (arr[R-1][C-1] == K){
            printf("%d", t);
            return 0;
        }

        if (r >= c){
            // R 연산
            int max_len = 1;
            for (int i = 0; i < 101; ++i) {
                v.clear();
                int tmp_len = 0;
                int num_count[101] = {0,};
                for (int j = 0; j < 101; ++j) {
                    if(arr[i][j] == 0) continue;
                    num_count[arr[i][j]] += 1;
                }

                for (int k = 1; k < 101; ++k) {
                    if(num_count[k] == 0) continue;
                    v.push_back(make_pair(k, num_count[k]));    // 숫자, 빈도 v 에 넣기
                    tmp_len += 2;
                }
                sort(v.begin(), v.end(), compare);
                max_len = max(max_len, tmp_len);
                for (int j = 0; j < v.size(); ++j) {
                    new_ar[i][2 * j] = v[j].first;
                    new_ar[i][2 * j + 1] = v[j].second;
                }
            }

            c = max_len;
        }

        else{
            // C 연산
            int max_len = 1;
            for (int j = 0; j < 101; ++j) {
                v.clear();
                int tmp_len = 0;
                int num_count[101] = {0,};
                for (int i = 0; i < 101; ++i) {
                    if(arr[i][j] == 0) continue;
                    num_count[arr[i][j]] += 1;
                }
                
                for (int k = 1; k < 101; ++k) {
                    if(num_count[k] == 0) continue;
                    v.push_back(make_pair(k, num_count[k]));    // 숫자, 빈도 v 에 넣기
                    tmp_len += 2;
                }
                sort(v.begin(), v.end(), compare);
                max_len = max(max_len, tmp_len);

                for (int i = 0; i < v.size(); ++i) {
                    new_ar[2 * i][j] = v[i].first;
                    new_ar[2 * i + 1][j] = v[i].second;
                }
            }

            r = max_len;
        }

        // arr 갱신
        for (int i = 0; i < 101; ++i) {
            for (int j = 0; j < 101; ++j) {
                arr[i][j] = new_ar[i][j];
            }
        }
    }


    printf("%d", -1);
    return 0;
}
