%K-near TSP
Path = [];
Costtot = [];
greedytime = [];
for k = 1 : n
    tic
    startK = k
    flag = zeros(1,n);
    flag(startK) = 1;
    path = [startK];
    pre = startK;
    cost_knear = 0
    
    for i = 1 : n - 1
        [Min loc] = max(arc(pre,:))
        for j = 1 : n
            if flag(j) == 0 && arc(pre,j) < Min
                Min = arc(pre,j);
                loc = j;
            end
        end
        flag(loc) = 1;
        cost_knear = cost_knear + Min;
        pre = loc;
        path = [path loc];
    end
    cost_knear = cost_knear + arc(path(n),path(1));
    path = [path startK];
    toc
    NearestTime = toc
    Path = [Path;path];
    Costtot = [Costtot;cost_knear];
    greedytime = [greedytime toc];
end
