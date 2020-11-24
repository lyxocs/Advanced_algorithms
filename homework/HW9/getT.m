function [t w_num] = getT(n,w)
tic
N = n;
w = w;
One = ones(N,1);
rng(1)
w_num = 0;
A = zeros(N,N);
for i = 1:N
    for j = i+1 : N
        if rand() < w
            A(i,j) = -1;
            A(j,i) = -1;
            w_num = w_num + 1;
        end
    end
end
b = -ones(1,N);
w = ceil(rand(1,N));
lb = zeros(1,N);
ub = ones(1,N);
x = linprog(w,A,b,[],[],lb,ub);
t = toc;

        