function Cacucost(path,arc)
tot = 0;
for i = 1 : length(path) - 1
    tot = tot + arc(path(i),path(i + 1));
end
tot