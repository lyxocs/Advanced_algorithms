#include <bits/stdc++.h>
using namespace std;
vector<vector<int> > order;
void dfs(int m,int n,vector<int> vec)
{
    if(n==0)
    {
        order.push_back(vec);
        return;
    }
    for (int i = 1; i <= m; i++)
    {
        vec.push_back(i);
        dfs(m,n - 1,vec);
        vec.pop_back();
    }
}
int main()
{
    int m = 3,n = 7;
    vector<int> vec;
//    optimal solution
    vector<int> best_jobs,best_orders;
    int best_T,best_greedy;
    dfs(m,n,vec);
    double MaxT = 0.0;
    srand((unsigned)time(NULL));
    for(int i = 0; i < 100000; i++)
    {
        vector<int> jobs;
        for(int i = 0; i < n; i++)
        {
            jobs.push_back(rand() % 10 + 1);
        }
        sort(jobs.begin(),jobs.end(),greater<int>());
//        for(auto i : jobs)
//        {
//            cout<<i<<"---";
//        }
//        cout<<endl;
        int optimal_t = INT_MAX;
        vector<int> optimal_jobs,optimal_order;
        for(int i = 0; i < order.size(); i++)
        {
            vector<int> t(m);
            for(int j = 0; j < order[i].size(); j++)
            {
                t[order[i][j] - 1] += jobs[j];
            }
            int Max = 0;
            for(int i = 0; i < m; i++)
            {
                if(t[i] > Max)
                {
                    Max = t[i];
                }
            }
            if(Max < optimal_t)
            {
                optimal_jobs = jobs;
                optimal_order = order[i];
                optimal_t = Max;
            }
        }
//        cout<<"Optimal_t:"<<optimal_t<<endl;
//        cout<<"optimal_order"<<endl;
//        for(auto i : optimal_order)
//        {
//            cout<<i<<"---";
//        }
//        cout<<endl;
//        cout<<"optimal_t:"<<endl;
//        for(auto i : optimal_jobs)
//        {
//            cout<<i<<"---";
//        }

        //greedy
        vector<int> greedy_t(m);
        for(int i = 0; i < n; i++)
        {
            int Mint = 0;
            for(int i = 0; i < m; i++)
            {
                if(greedy_t[i] < greedy_t[Mint])
                {
                    Mint = i;
                }
            }
            greedy_t[Mint] += jobs[i];
        }
        int greedy_Max = 0;
        for(int i = 0; i < m; i++)
        {
            if(greedy_t[i] > greedy_Max)
            {
                greedy_Max = greedy_t[i];
            }
        }
//        cout<<"\ngreedy_Max:"<<greedy_Max<<endl;
        double percent = (double)(greedy_Max * 1.0/optimal_t * 1.0);
//        cout<<greedy_Max<<"---"<<optimal_t<<endl;
//        cout<<percent<<endl;
        if(percent > MaxT)
        {
            MaxT = percent;
            best_jobs = optimal_jobs;
            best_orders = optimal_order;
            best_T = optimal_t;
            best_greedy = greedy_Max;
        }
    }
    cout<<MaxT<<endl;
    cout<<"best_T:"<<best_T<<endl;
    cout<<"best_greedy:"<<best_greedy<<endl;
    for(auto i : best_orders)
    {
        cout<<i<<"---";
    }
    cout<<endl;
    cout<<"optimal_t:"<<endl;
    for(auto i : best_jobs)
    {
        cout<<i<<"---";
    }
    return 0;
}

