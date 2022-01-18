%Generate and Plot Ramp Signal

%Ramp=t*u(t)

t = -10:10;                         % time renge

u = [zeros(1,10) ones(1,11)];       % unit step sequence

r = t.*u;
plot(t,r,'g');
axis([-12 12 -1 2])