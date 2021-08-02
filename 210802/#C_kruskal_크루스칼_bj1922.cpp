# include <cstdio>
# include <vector>
# include <algorithm>

using namespace std;
class Edge{
public:
    int node[2];
    int cost;
    Edge(int s, int d, int cost){
        this->node[0] = s;
        this->node[1] = d;
        this->cost = cost;
    }

    // 정렬 방법
    // 1. 연산자 오버로딩 (이름은 그대로, 매개변수만 바꿔서 선언한다. )
    // algorithm 에서 const 를 매개변수로 받기 때문에 const 로 선언해줘야한다.
    bool operator <(const Edge &edge) const{
        return this -> cost < edge.cost;
    }

};


// 2. compare 함수를 통해 구현
bool compare(Edge e1, Edge e2){
    return e1.cost < e2.cost;
}

void Print(vector<Edge> &v){
    for(int i=0; i<v.size(); i++){
        printf("%d %d %d\n", v[i].node[0], v[i].node[1], v[i].cost);

    }
    printf("\n");
}

int get_parent(int idx, int * parent){
    if(parent[idx] == idx)
        return idx;
    else
        return get_parent(parent[idx], parent);
}


int main(){
    int N, M;
    vector<Edge> graph;
    int parent[1001] = {};
    int tot_cost = 0;

    scanf("%d", &N);
    scanf("%d", &M);
    for(int i=0; i<M; i++){
        int s, d, cost;
        scanf("%d %d %d", &s, &d, &cost);
        graph.push_back(Edge(s, d, cost));
    }

    // 간선의 cost 로 오름차순 정렬
    //Print(graph);
    sort(graph.begin(), graph.end());

    // Print(graph);
//    for(Edge e : graph){
//        printf("%d %d %d \n", e.node[0], e.node[1], e.cost);
//    }

    // parent 배열 초기화
    for(int i = 1; i<N+1; i++){
        parent[i] = i;
    }
//    printf("%d", get_parent(graph, 2, parent));
    for(Edge e : graph){
        int s = e.node[0];
        int d = e.node[1];
        int p_s = get_parent(s, parent);
        int p_d = get_parent(d, parent);

        if (p_s != p_d){
            tot_cost += e.cost;
            if (p_s <= p_d){
                parent[p_d] = p_s;
            }
            else{
                parent[p_s] = p_d;
            }
        }
    }
    printf("%d", tot_cost);




    return 0;
}
