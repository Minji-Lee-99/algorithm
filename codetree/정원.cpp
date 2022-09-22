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
    //�Է¹ޱ�
    int a, t, i;
    for (i=1; i<= N; i++){
        cin >> a >> t;
        pq.push(make_tuple(a, t, i));
    }
    while (!pq.empty()){
    	tie(a, t, i) = pq.top();
    	pq.pop();
	}
    int last_time = 0, wait = 0; // ������ ����� ������ ��ģ �ð�, ���� ���� ��ٸ� �ð�
    while(!pq.empty()){
        //�ϴ� �Ѹ� �ٷ� ������ �ֱ�
        tie(a, t, i) = pq.top();
        pq.pop();
        if (last_time > a) {
            cout << "check!!" << endl;
            wait = max(wait, last_time - a);
            last_time = last_time + t;
        }
        else last_time = a + t;
        // �Ѹ��� ������ �����ϴ� ���� ������ ��� temp(�����)�� �ű��
        while(true){
            tie(a, t, i) = pq.top();
            if (a < last_time){
                temp.push(make_tuple(i, a, t)); // ����ܿ����� ��ȣ ������� ����
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
