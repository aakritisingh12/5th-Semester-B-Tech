clc;
clear all;
close all;
%Shifting a non-function Discrete-time signal
n = -8:8;
x = [0 0 0 0 0 3 -3 2 -2 1 -1 0.5 -0.5 0 0 0 0];
subplot(2,1,1);stem(n,x); title('x(n) signal');
xlabel('n ------>'); ylabel('x(n) --->');
 
m=n+2; y=x;
subplot(2,1,2);stem(m,y); title('y(n)=x(n-2) signal');
xlabel('n ------>'); ylabel('y(n) --->');
