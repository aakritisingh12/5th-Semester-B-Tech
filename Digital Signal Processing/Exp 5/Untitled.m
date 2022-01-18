%KAISER WINDOW
m=input('Enter the value of M=');
w=input('Enter the normalised cutoff frequency=')'
a=(m-1)/2;
n=[0:(a-1)*(a+1):(m-1)];
f=w*sinc(w*(-a:a));
lp=f.*kaiser(m)'
fvtool(lp);