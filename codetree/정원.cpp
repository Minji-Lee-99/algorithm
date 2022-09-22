#include <iostream>
#include <queue>
#include <tuple>

using namespace std;

int main(){
    int N;
    cin >> N;
    // a, t, i
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int> >, greater<tuple<int, int, int> >> pq;
    // i, a, t
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int> >, greater<tuple<int, int, int> >> temp;
    //입력받기
    int a, t, i;
    for (i=1; i<= N; i++){
        cin >> a >> t;
        pq.push(make_tuple(a, t, i));
    }
    while (!pq.empty()){
    	tie(a, t, i) = pq.top();
    	pq.pop();
	}
    int last_time = 0, wait = 0; // 마지막 사람이 구경을 마친 시간, 가장 오래 기다린 시간
    while(!pq.empty()){
        //일단 한명 바로 공원에 넣기
        tie(a, t, i) = pq.top();
        pq.pop();
        if (last_time > a) {
            cout << "check!!" << endl;
            wait = max(wait, last_time - a);
            last_time = last_time + t;
        }
        else last_time = a + t;
        // 한명이 공원을 구경하는 동안 도착한 사람 temp(대기명단)에 옮기기
        while(true){
            tie(a, t, i) = pq.top();
            if (a < last_time){
                temp.push(make_tuple(i, a, t)); // 대기명단에서는 번호 순서대로 정렬
                pq.pop();
            }
            else break;
        }
        //
        while(!temp.empty()){
            tie(i, a, t) = temp.top();
            cout << i << " " << a << " " << t << " " << endl;
            temp.pop();
            if (last_time > a) {
                cout << "check!!" << endl;
                wait = max(wait, last_time - a);
                last_time = last_time + t;
            }
            else last_time = a + t;
        }
    }
    cout << wait << endl;
}
