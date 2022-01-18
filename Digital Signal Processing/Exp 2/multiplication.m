clc;
clear all;
close all;

%MULTIPLICATION SCRIPT
N=69;
n=0:3:N-1;
yn=cos(0.2*pi*n).*cos(0.9*pi*n);
subplot(2,1,1),stem(n,yn);
subplot(2,1,2),plot(n,yn);
xlabel('n--------------->');ylabel('xn--------------->');
title('Multiplication of two cosine sequences');
