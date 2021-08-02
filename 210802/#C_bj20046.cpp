# include <cstdio>
# include <vector>
# include <queue>

using namespace std;

struct Node{
    int cost;
    int x;
    int y;
};

struct cmp{
    bool operator()(Node n1, Node n2){
        return n1.cost > n2.cost;
        // 최소힙
    }
};






int main(void){
    int m, n;
    int arr[1001][1001] = {};
    int visited[1001][1001] = {0, };
    int dx[4] = {1, -1, 0 ,0};
    int dy[4] = {0, 0, 1, -1};

    scanf("%d %d", &m, &n);

    // 초기화
    for(int i = 0 ; i < m; i++){
        for(int j = 0; j < n ; j++){
            visited[i][j] = -1;
        }
    }

    // 입력값
    for(int i = 0 ; i < m ; i ++){
        for(int j = 0 ; j < n ; j++){
            scanf("%d", &arr[i][j]);
//            printf("%d ", visited[i][j]);
        }
    }

    if(arr[0][0] == -1){
        printf("%d", -1);
        return 0;
    }

    Node node = {arr[0][0], 0, 0};
    
    // priority_queue 를 사용하는 방법
    // priority queue 에 overload 하는 과정 
    priority_queue<Node, vector<Node>, cmp> heap;
    heap.push(node);
    visited[0][0] = arr[0][0];

    while (!heap.empty()){
        int cost, x, y;
        cost = heap.top().cost;
        x = heap.top().x;
        y = heap.top().y;
        heap.pop();

        for(int i = 0; i < 4 ; i ++){
            int r, c, nxt_cost;
            r = x + dx[i];
            c = y + dy[i];

            if(0 <= r  && r < m && 0 <= c && c < n){
                if(arr[r][c] != -1){
                    if(visited[r][c] == -1 || visited[r][c] > cost + arr[x][y]){
                        nxt_cost = cost + arr[r][c];
                        visited[r][c] = nxt_cost;
                        // Node tmp_node = {nxt_cost, r, c}; 이와 같이 선언하지 않고, 직접 {} 을 이용해 넣어준다.
                        heap.push({nxt_cost, r, c});
                    }
                }
            }
        }

    }
//    for(int i = 0 ; i < m ; i ++){
//        for(int j = 0 ; j < n ; j++){
//            printf("%d ", visited[i][j]);
//        }
//        printf("\n");
//    }

    printf("%d", visited[m-1][n-1]);
    return 0;
}
