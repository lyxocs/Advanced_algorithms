t_w = [];
w_num = [];
w = 0.05;
n = 3:50:2000
for i = 1:length(n)
    [t_1 w_1] = getT(n(i),w);
    t_w = [t_w t_1];
    w_num = [w_num w_1];
    n(i)
end
plot2(n,t_w)