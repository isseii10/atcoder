#include <bits/stdc++.h>
//#include <atcoder/all>
#define rep(i, n) for (int i=0; i < (n); i++)
using namespace std;
//using namespace atcoder;
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int, int> P;
const int INF = 1 << 30;
const ll LINF = 1LL << 61;
const int NIL = -1;
const int MAX = 10000;
const int MOD = 1000000007;
const double pi = 3.141592653589;


template <typename T> 
struct simple_queue {
    std::vector<T> payload;
    int pos = 0;
    void reserve(int n) { payload.reserve(n); }
    int size() const { return int(payload.size()) - pos; }
    bool empty() const { return pos == int(payload.size()); }
    void push(const T& t) { payload.push_back(t); }
    T& front() { return payload[pos]; }
    void clear() {
        payload.clear();
        pos = 0;
    }
    void pop() { pos++; }
};
template <typename Cap> //Cap:Capacity
struct mf_graph {
  public:
    mf_graph() : _n(0) {}
    mf_graph(int n) : _n(n), g(n) {}
 
    int add_edge(int from, int to, Cap cap) {
        /*
        assertは条件が真になるようにつける。
        想定した範囲になっていなかったら、
        （これについてはfromなどのインデックスが変だったら）
        エラーにする。
        */
        assert(0 <= from && from < _n);
        assert(0 <= to && to < _n);
        assert(0 <= cap);
        int m = int(pos.size());
        pos.push_back({from, int(g[from].size())});
        int from_id = int(g[from].size());
        int to_id = int(g[to].size());
        if (from == to) to_id++;
        g[from].push_back(_edge{to, to_id, cap});
        g[to].push_back(_edge{from, from_id, 0});
        return m;
    }
 
    struct edge // edgeは、有向枝でfromとtoのノードと、重み、フローを持つ。 
    {
        int from, to;
        Cap cap, flow;
    };
 
    edge get_edge(int i) {
        int m = int(pos.size());
        assert(0 <= i && i < m);
        auto _e = g[pos[i].first][pos[i].second];
        auto _re = g[_e.to][_e.rev];
        return edge{pos[i].first, _e.to, _e.cap + _re.cap, _re.cap};
    }
    vector<edge> edges() {
        int m = int(pos.size());
        vector<edge> result;
        for (int i = 0; i < m; i++) {
            result.push_back(get_edge(i));
        }
        return result;
    }
    void change_edge(int i, Cap new_cap, Cap new_flow) {
        int m = int(pos.size());
        assert(0 <= i && i < m);
        assert(0 <= new_flow && new_flow <= new_cap);
        auto& _e = g[pos[i].first][pos[i].second];
        auto& _re = g[_e.to][_e.rev];
        _e.cap = new_cap - new_flow;
        _re.cap = new_flow;
    }
 
    Cap flow(int s, int t) {
        return flow(s, t, numeric_limits<Cap>::max());
    }
    Cap flow(int s, int t, Cap flow_limit) {
        assert(0 <= s && s < _n);
        assert(0 <= t && t < _n);
        assert(s != t);
 
        vector<int> level(_n), iter(_n);
        simple_queue<int> que;
 
        auto bfs = [&]() {
            fill(level.begin(), level.end(), -1);
            level[s] = 0;
            que.clear();
            que.push(s);
            while (!que.empty()) {
                int v = que.front();
                que.pop();
                for (auto e : g[v]) {
                    if (e.cap == 0 || level[e.to] >= 0) continue;
                    level[e.to] = level[v] + 1;
                    if (e.to == t) return;
                    que.push(e.to);
                }
            }
        };
        auto dfs = [&](auto self, int v, Cap up) {
            if (v == s) return up;
            Cap res = 0;
            int level_v = level[v];
            for (int& i = iter[v]; i < int(g[v].size()); i++) {
                _edge& e = g[v][i];
                if (level_v <= level[e.to] || g[e.to][e.rev].cap == 0) continue;
                Cap d =
                    self(self, e.to, min(up - res, g[e.to][e.rev].cap));
                if (d <= 0) continue;
                g[v][i].cap += d;
                g[e.to][e.rev].cap -= d;
                res += d;
                if (res == up) break;
            }
            return res;
        };
 
        Cap flow = 0;
        while (flow < flow_limit) {
            bfs();
            if (level[t] == -1) break;
            fill(iter.begin(), iter.end(), 0);
            while (flow < flow_limit) {
                Cap f = dfs(dfs, t, flow_limit - flow);
                if (!f) break;
                flow += f;
            }
        }
        return flow;
    }
 
    vector<bool> min_cut(int s) {
        vector<bool> visited(_n);
        simple_queue<int> que;
        que.push(s);
        while (!que.empty()) {
            int p = que.front();
            que.pop();
            visited[p] = true;
            for (auto e : g[p]) {
                if (e.cap && !visited[e.to]) {
                    visited[e.to] = true;
                    que.push(e.to);
                }
            }
        }
        return visited;
    }
 
  private:
    int _n;
    struct _edge {
        int to, rev;
        Cap cap;
    };
    vector<pair<int, int>> pos;
    vector<vector<_edge>> g;
};
 

int main() {
    int n;
    cin >> n;
    mf_graph<int> graph(2*n + 2);
    rep(i,n){
        graph.add_edge(0, i+1, 1); 
        //idx0はソースで二部グラフの片側に重み１で全てつなぐ
        graph.add_edge(n + i+1, 2*n+1, 1);
        //idx(2*n+1)はシンクでもう片側に全てつなぐ
    }
    vector<P> r(n), b(n);
    rep(i,n) cin >> r[i].first >> r[i].second;
    rep(i,n) cin >> b[i].first >> b[i].second;
    rep(i,n){
        rep(j,n){
            if(r[i].first < b[j].first && r[i].second < b[j].second)
                graph.add_edge(i+1, n+j+1, 1);
        }
    }
    cout << graph.flow(0, 2*n+1) << endl;
    return 0;
}