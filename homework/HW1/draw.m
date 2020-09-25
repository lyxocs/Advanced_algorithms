function draw(point,path,n,Title,cost)
fig = figure();
hold on;
axis([0 n 0 n]);
flag = 1 : n;
for i = 1 : n
    text(point(i,1) + 0.1,point(i,2),num2str(flag(i)),'FontSize',26);
end
scatter(point(:,1),point(:,2));
line(point(path,1),point(path,2));
title([Title '  cost = ' num2str(cost)]);
xlabel('x')
ylabel('y')
saveas(fig,Title,'pdf')