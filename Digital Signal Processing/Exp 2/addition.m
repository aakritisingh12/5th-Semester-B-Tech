clc;
clear all;
close all;
%ADDITION SCRIPT
N=69;
n=0:2:N-1;
xn=cos(0.4*pi*n)+cos(0.5*pi*n);
subplot(2,1,1),stem(n,xn);
subplot(2,1,2),plot(n,xn);
xlabel('n--------------->');ylabel('xn-------->');
title('Addition of two cosine sequences');
