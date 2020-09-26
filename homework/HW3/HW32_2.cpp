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
    int m = 3,n = 9;
    vector<int> vec;
    dfs(m,n,vec);
    vector<vector<int> > jobs;
    for(int i = 1; i <= n; i++)
    {
        vec.push_back(2 * i);
    }
    jobs.push_back(vec);
    jobs.push_back(vec);
    vec.clear();
    for(int i = 1; i <= n; i++)
    {
        vec.push_back(i);
    }
    jobs.push_back(vec);
    for(int  i = 0; i < jobs.size(); i++)
    {
        for(int j = 0; j < jobs[i].size(); j++)
        {
            cout<<jobs[i][j]<<"---";
        }
        cout<<endl;
    }
    int best_time = INT_MAX;
    vector<int> best_order;
    for (int i = 0; i < order.size(); i++)
    {
        vector<int> t(m);
        for(int j = 0; j < order[i].size(); j++) //分配第J个任务
        {
            t[order[i][j] - 1] += jobs[order[i][j] - 1][j];
        }
        int Max = t[0];
        for(int k = 0; k < n;k++)
        {
            if(t[k] > Max)
            {
                Max = t[k];
            }
        }
//        cout<<Max<<endl;
        if(Max < best_time)
        {
            best_time = Max;
            best_order = order[i];
        }

    }
    cout<<"best time:"<<best_time<<endl;
    for(auto i : best_order)
        cout<<i<<"---";
    return 0;
}

