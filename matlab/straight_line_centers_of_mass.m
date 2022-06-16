clear, clc

% Examples of systems whose center of mass moves in a straight line
%% Free rolling balls
t = linspace(0,1.2);
% Specify linear paths which means force-free motion
x10 = 0.1;    vx10 = 1;
y10 = 0.025;  vy10 = 0.4;
x1 = x10 + vx10*t;
y1 = y10 + vy10*t;

x20 = 0.05;    vx20 = 0.4;
y20 = 0.2;  vy20 = 1;
x2 = x20 + vx20*t;
y2 = y20 + vy20*t;

% x2 = 1+0.1 - 0.2*t;
% y2 = y1;

m1 = 1;
m2 = 2;

xcm = (m1*x1 + m2*x2)/(m1 + m2);
ycm = (m1*y1 + m2*y2)/(m1 + m2);
plot(xcm, ycm, 'k')

% x = x2 - x1;
% y = y2 - y1;
% r = sqrt(x.^2 + y.^2);
% plot(t,r)
% return

% Make gif
hold off
c1 = [128,128,191]/255;
c2 = [191,128,128]/255;
quiver(x1(1), y1(1), vx10, vy10, 'k', 'LineWidth', 3, 'MaxHeadSize', 0.5, 'AutoScaleFactor', 0.2), hold on
quiver(x2(1), y2(1), vx20, vy20, 'k', 'LineWidth', 3, 'MaxHeadSize', 0.5, 'AutoScaleFactor', 0.2)
plot(x1(1), y1(1), '.', 'color', c1, 'markersize', 20)
plot(x2(1), y2(1), '.', 'color', c2, 'markersize', 20*(m2/m1))
plotCenterOfMassSymbol(xcm(1),ycm(1),2.5,gca)
xlim([0,1])
ylim([0,1])
axis square
xlabel("$X$")
ylabel("$Y$")
% return
for k = 1:24
    pause(0.001)
    if (k == 1)
        gif('force free 5.gif', 'DelayTime', 1/24)
    else
        gif
    end
end
for k = 1:numel(t)
    plot(x1(1:k), y1(1:k), '-', 'Color', [1,1,1]*220/255),    hold on
    plot(x1(k), y1(k), '.', 'color', c1, 'markersize', 20)
    
    plot(x2(1:k), y2(1:k), '-', 'Color', [1,1,1]*220/255)
    plot(x2(k), y2(k), '.', 'color', c2, 'markersize', 20*(m2/m1))
    
    plot(xcm(1:k), ycm(1:k), '-', 'Color', [1,1,1]*220/255)
    plotCenterOfMassSymbol(xcm(k),ycm(k),2.5,gca)
    
    hold off
    xlim([0,1])
    ylim([0,1])
    axis square
    xlabel("$X$")
    ylabel("$Y$")
%     xticks([])
%     yticks([])
    pause(0.001)
    gif
end
% Fade out the traces
for a = 220:5:255
    hold on
    plot(x1, y1, '-', 'Color', [1,1,1]*a/255)
    plot(x2, y2, '-', 'Color', [1,1,1]*a/255)
    plot(xcm,ycm, '-', 'Color', [1,1,1]*a/255)
    xlim([0,1])
    ylim([0,1])
    axis square
    xlabel("$X$")
    ylabel("$Y$")
%     xticks([])
%     yticks([])
    pause(0.001)
    hold off
    gif
end
hold off

%% Springs
% Two masses m1 and m2 connected to each other by a spring of constant k
% and equilibrium length l)
%   m1 * \ddot{x1} = -k*(x1 - x2 + l)
%   m2 * \ddot{x2} = -k*(x2 - x1 - l)
global m1 m2 k l
m1 = 1;
m2 = 5;
k = 5;
l = 0.5;

x10 = 0.3;
u10 = 0.1;
x20 = 0.8;
u20 = -0.05;

tspan = [0,10];
y0 = [x10, x20, u10, u20];
[t, x] = ode45(@springs, tspan, y0);

x1 = x(:,1);
x2 = x(:,2);
u1 = x(:,3);
u2 = x(:,4);

for p = 1:numel(t)
    plot(x1(p), 0, '.', 'markersize', 20)
    hold on
    plot(x2(p), 0, '.', 'markersize', 20)
    hold off
    xlim([0,1])
    ylim([0,1])
    axis square
    xlabel("$X$")
    ylabel("$Y$")
    pause(0.001)
end

function f = springs(t, x)
    global m1 m2 k l
    f = zeros(4,1);
    f(1) = x(3);
    f(2) = x(4);
    f(3) = -k/m1*(x(1) - x(2) + l);
    f(4) = -k/m2*(x(2) - x(1) - l);
end