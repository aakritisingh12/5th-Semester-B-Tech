
t = (-10:1:10)';  %%Can change the interval time by replacing 1 with 0.1
%step1 = t>=0;  %% For u[n]
step2 = t>=5   %%For u[n-3]
x=step2*2
stem(t,x)    %%scatter can be used instead of plot
xlabel('time');
ylabel('amplitude');
title('x(n)=u(n)-u(n-3)');