%Generate Unit Impulse Function
clc;
clear all;
close all;
%========================================
N = input('Length of the sequence = ');
n = -N :1: N;
%========================================
Y = [zeros(1,N),1,zeros(1,N)];
stem(n,Y);
%========================================
xlabel('Time in n');
ylabel('Amplitude in Y');
title('Generating Unit Impulse Signal');
