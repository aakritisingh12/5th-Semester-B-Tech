clc ;
clear all ;
close all ;
x=[1,-2,0,1];
N1=length(x);
n1=0:1:N1-1;
subplot(2,2,1),
stem(n1,x);
xlabel('n1');
ylabel('x(n1)');
title('input sequence 1');
x2=[1,-2,-3,4];
N2=length(x2);
n2=0:1:N2-1;
subplot(2,2,2),
stem(n2,x2);
xlabel('n2');
ylabel('x(n2)');
title('input sequence 2');
y=conv(x,x2);
n=0:1:length(y)-1;
subplot(2,1,2),stem(n,y);
xlabel('n');
ylabel('y(n)');
title('convolution of x(n)*x2(n)');

% x(n)= [1,1,0|,1,1]-------(-2 to 2)
% h(n)= [1,-2,-3,4|]........(-3 to 0)