// #include <iostream>
// using namespace std;

// unsigned long pow_mod(unsigned long x, unsigned long y, unsigned long z)
// {
//     unsigned long number = 1;
//     while (y)
//     {
//         if (y & 1)
//             number = number * x % z;
//         y >>= 1;
//         x = (unsigned long)x * x % z;
//     }
//     return number;
// }

// unsigned long get_d(unsigned long e){
//     unsigned long x = 233459992;
//     int k = 1;
//     while(true){
//         if(((x*k)+1) % e == 0){
//             return (x*k+1)/e;
//         }
//         k += 1;
//     }
// }

// int main()
// {
//     unsigned long e, c, d, m;
//     unsigned long n = 233493331;
//     cin>>e;
//     cin>>c;
//     d = get_d(e);
//     m = pow_mod(c, d, n);
//     cout<<m;
//     return 0;
// }


// // 申请经费
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
const int N = 1010, M = 1e6 + 10, INF = 0x3f3f3f3f;
int n, m;
int dist[N];
// 是否已经遍历
bool visit[N];
// N家公司和其他公司合作，n=0表示自建
int map[N][N];
int prim(){
    int res = 0;
    memset(dist, 0x3f, sizeof(dist));
    for (int i = 0; i <= n; i++){
        int t = -1;
        // i=0时最小自建成本，i>0时排除合作比自建成本高的
        for (int j = 0; j <= n; j++){
            if (!visit[j] && (t == -1 || dist[t] > dist[j])){
                t = j;
            }
        }
        // 无合作
        if (i != 0 && dist[t] == INF){
            return INF;
        }
        // 成本最低合作方式
        if (i != 0){
            res += dist[t];
        }
        visit[t] = true;
        // t公司与一家公司合作的最小成本
        for (int j = 0; j <= n; j++){
            dist[j] = min(dist[j], map[t][j]);
        }
    }
    return res;
}


int main()
{
    int t;
    cin >> t;
    while (t--){
        cin >> n >> m;
        memset(map, 0x3f, sizeof(map));
        memset(visit, 0, sizeof(visit));
        // 自建团队费用
        for (int i = 1; i <= n; i++){
            int x;
            cin >> x;
            map[0][i] = map[i][0] = min(map[0][i], x);
        }
        // 合作费用
        while (m--){
            int a, b, w;
            cin >> a >> b >> w;
            map[a][b] = map[b][a] = min(map[a][b], w);
        }
        cout << prim() << endl;
    }
    return 0;
}


// #include <iostream>
// #include <map>

// using namespace std;
// int n, m;

// int main(){
//     int t;
//     cin>>t;
//     int ts, times;
//     string _type;
//     while(t--){
//         cin>>n>>m;
//         int logs[n];
//         while(n--){
//             cin>>ts>>_type>>times;
            
//         }

//     }


//     return 0;
// }