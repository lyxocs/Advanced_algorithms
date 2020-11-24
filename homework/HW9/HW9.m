% Running time and w
t_w = [];
w_num = [];
w = 0.05:0.05:1;
n = 1000;
for i = 1:length(w)
    [t_1 w_1] = getT(n,w(i));
    t_w = [t_w t_1];
    w_num = [w_num w_1]
end