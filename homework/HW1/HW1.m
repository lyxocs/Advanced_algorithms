clear;
format long
clf;
n = 10; %所取点数
point = [];
x = [];
y = [];
for i = 1:n
    x = rand() * n;
    y = rand() * n;
    point = [point;[x y]];
end


% TSP Optimal solution
arc = zeros(n);
for i = 1 : n
    for j = 1 : n
        arc(i,j) = norm(point(i)-point(j));
    end
end

edges = zeros(1,n);
for i = 1 : n
    edges(i) = i;
end
P = perms(edges);
P = [P P(:,1)];
cost = sum(arc(:));
Max = sum(arc(:).^2);
Minsort = P(1,:);
[m n1] = size(P);
for i = 1 : m
    tot = 0;
    totnorm = 0;
    for j  = 1 : n1 - 1 
        tot = tot + (point(P(i,j),1) - point(P(i,j + 1),1))^2 + (point(P(i,j),2) - point(P(i,j + 1),2))^2;
        totnorm = totnorm + norm(point(P(i,j)) - point(P(i,j + 1)));
    end
    if tot < Max
        Max = tot;
        cost = totnorm ;
        Minsort = P(i,:);
    end
end
cost
draw(point,Minsort,n,' Optimal',cost)

%K-near TSP
startK = ceil(rand() * n);
flag = zeros(1,n);
flag(startK) = 1;
path = [startK];
pre = startK;
cost_knear = 0

for i = 1 : n - 1
    Min = max(arc(pre,:)) + 1;
    loc = 0;
    for j = 1 : n
        if flag(j) == 0 & arc(pre,j) < Min
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
draw(point,path,n,'nearest',cost_knear);
save HW1
    