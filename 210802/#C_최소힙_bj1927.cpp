# include <queue>
# include <cstdio>
using namespace std;

struct Num{
    int ele;
};

struct cmp{
    bool operator()(Num n1, Num n2){
        return n1.ele > n2.ele;
    }
};

int main(void){
    int n;
    scanf("%d", &n);
    priority_queue<Num ,vector<Num>, cmp> heap;
    for(int i =0 ;i < n ;i ++){
        int command;
        scanf("%d", &command);
        if(command == 0){
            if(!heap.empty()){
                printf("%d\n", heap.top().ele);
                heap.pop();
            }else{
                printf("%d\n", 0);
            }
        }
        else{
            heap.push({command});
        }

    }



    return 0;
}
