%% unit ramp sequence

n = -5:5;

x = n.*(n>=0);

stem(n,x,'go-','MarkerSize',15);
xlim([n(1)-1 n(end)+1]);
ylim([min(x)-0.1 max(x)+1]);
xlabel('--> n');
ylabel('--> Amp');
title('Ramp sequence');
grid on;