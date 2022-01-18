clc;
clear all;
close all;
% real exponential

n = -5:1:50;
a = -0.1;

x = exp(a*n);

stem(n,x,'r--','MarkerSize',15);
xlim([n(1)-1 n(end)+1]);
ylim([min(x)-0.1 max(x)+1]);

xlabel('-->n');
ylabel('--> Amp');
title('Exponential sequence');
