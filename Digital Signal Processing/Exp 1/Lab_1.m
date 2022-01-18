clc ; 
clear all ; 
close all ;

% PROGRAM for the generation of unit impulse signal 

t=-2:1:2 ; 
y=[zeros(1,2),ones(1,1),zeros(1,2)] ; 
subplot(3,2,1) ; 
stem(t,y) ; 
ylabel('amplitude ---->') ; 
xlabel('(a)n ---->') ; 
title(' unit impulse signal ') ; 

% PROGRAM for the generation of unit step 

n=input('enter the N value ') ; 
t=0:1:n-1 ; 
y=ones(1,n) ; 
subplot(3,2,2) ; 
stem(t,y) ; 
ylabel('amplitude ---->') ; 
xlabel('(b)n ---->') ; 
title(' unit step sequence ') ; 

% PROGRAM for the generation of ramp sequence 

n=input('enter the length of ramp sequence ') ; 
t=0:n-1 ; 
subplot(3,2,3) ; 
stem(t,t) ; 
ylabel('amplitude ---->') ; 
xlabel('(c)n ---->') ; 
title(' ramp sequence ') ; 


% PROGRAM for the generation of exponential sequence

n=input('enter the length of exponential sequence') ; 
t=0:n ; 
a=input('enter the value of a ') ; 
y=exp(a*t) ; 
subplot(3,2,4) ; 
stem(t,y) ; 
ylabel('amplitude ---->') ; 
xlabel('(d)n ---->') ; 
title(' exponential sequence ') ;


% PROGRAM for the generation of sinusoidal sequence

t=0:0.01:pi ; 
y=sin(2*pi*t) ; 
subplot(3,2,5) ; 
plot(t,y) ; 
ylabel('amplitude ---->') ; 
xlabel('(e)n ---->') ; 
title(' sine sequence ') ; 


% PROGRAM for the generation of cosine sequence

t=0:0.01:pi ; 
y=cos(2*pi*t) ; 
subplot(3,2,6) ; 
plot(t,y) ; 
ylabel('amplitude ---->') ; 
xlabel('(f)n ---->') ; 
title (' cosine sequence ') ; 

