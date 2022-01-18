% Generate of Sinusoidal Signal
% Sinusoidal Signal in Discrete Time Case
n = [-10:0.5:10];
x_n = sin(n);
stem(n,x_n);
title('sinusoidal signal in discrete time')
xlabel('n')
ylabel('amplitude')
axis([-10 10 -3 3])