%power spectrum of a signal

N=1024;
fs=8000;

% signal 1
f=input('enter the frequency[1 to 5000]:');;
ts=1/fs;
t = ts*(0:N-1);
x=sin(2*pi*f*t);
subplot(4,2,1),plot(t,x),title('100hz'); 
% power spectrum of 1 
y = fft(x);
N = length(x);          % number of samples
f = (0:N-1)*(fs/N);     % frequency range
pow = abs(y).^2/N;    % power of the DFT
subplot(4,2,2),plot(f,pow), title('100hz power');

% signal 2
f1=input('enter the frequency[1 to 5000]:');;
x1=sin(2*pi*f1*t);
subplot(4,2,3),plot(t,x1),title('200hz'); 
% power spectrum of 2
y = fft(x1);
N = length(x);          % number of samples
f = (0:N-1)*(fs/N);     % frequency range
pow = abs(y).^2/N;    % power of the DFT
subplot(4,2,4),plot(f,pow), title('200hz power');  

% signal 3
f2=input('enter the frequency[1 to 5000]:');;
x2=sin(2*pi*f2*t);
subplot(4,2,5),plot(t,x2),title('300hz'); 
% power spectrum of 3
y = fft(x2);
N = length(x);          % number of samples
f = (0:N-1)*(fs/N);     % frequency range
pow = abs(y).^2/N;    % power of the DFT
subplot(4,2,6),plot(f,pow), title('300hz power');

% signal combined Hz
x3=x+x1+x2;
subplot(4,2,7),plot(t,x3),title('added freq signal'); 
% power spectrum of combined Hz
y = fft(x3);
N = length(x);          % number of samples
f = (0:N-1)*(fs/N);     % frequency range
pow = abs(y).^2/N;    % power of the DFT
subplot(4,2,8),plot(f,pow), title('combine hz power');