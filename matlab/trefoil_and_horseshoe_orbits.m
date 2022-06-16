clear, clc

orbit = 'horseshoe'; % horseshoe or trefoil


% Don't edit below here
mu = 1e-4;

Tover2 = 67.05634232*2*pi;
x0 = -0.864394016091;
y0 = 0;
xdot0 = 0;
ydot0 = -0.288028401448;

switch orbit
    case 'horseshoe'
        % Change nothing
    case 'trefoil'
        mu = 100*mu;
        ydot0 = -ydot0;
end


% x0 = -1.214480026998;
% y0 = -0.401585865744;

r10 = sqrt((x0 + mu)^2 + y0^2);
r20 = sqrt((x0 + mu - 1)^2 + y0^2);
v0 = sqrt(xdot0^2 + ydot0^2);
JacobiC(mu, r10, r20, v0)

opts = odeset('AbsTol', 1e-12, 'RelTol', 1e-13, 'Refine', 1);
[t, x] = integrateCR3BP(mu, [x0,y0,xdot0,ydot0], Tover2, 'formalism', 'lagrangian', 'model', 'pcr3bp', 'odeset', opts);

%%
plot(x(:,1), x(:,2))
hold on
plot(-mu,0,'k.','markersize', 75)
plot(1-mu,0,'k.','markersize', 25)
hold off
axis equal
