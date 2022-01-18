% Matlab Program to generate "Unit ramp" Signal
clc;
clear all;
close all;
% Defining the Time Limits and sampling time
% Here we would like to define the time from -4 to +6 with a time spacing
% of 0.5, you may change the time space to any value
t1 = input('enter the starting time =    ');
t2 = input('enter the ending time =      ');
t3 = input('enter the sampling time =     ');
t = t1:t3:t2;
% size of the time varialbe "t"
[m,n] = size(t);
% Lets initialize a null array 'r' with the same size of 't'  using 'zeros'
% command
r = zeros(m,n);
% the concept of Unit impulse is :
% r(t) = t at t >= 0
%      = 0 else
for i = 1:n
    if t(i) >= 0 
        r(i) = t(i);
    else
        r(i) = 0;
    end
end
% now "u" is the unit impulse signal, and "t" is the time
% Lets see how is our signal is 
stem(t,r);
xlabel('time');
ylabel('amplitude');
title('Discrete Unit ramp signal');
% Note1: the meaning of Unit Ramp Signal = the slope of the rample signal
% is unity i.e., the slope will be at an angle of 45 degrees
% Note2: If you would like to change the starting and ending time, you need
% to change in the program itself, otherwise you may modify the program to
% give the keyboard inputs. please check my matlab repository for the same
% program using keyboard/manual inputs
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

