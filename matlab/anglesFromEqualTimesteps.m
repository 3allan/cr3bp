function theta = anglesFromEqualTimesteps(dt, e)

% Define the time over which to find angles, from (0,t) with timestep dt
if (e < 1)
    halfPeriod = pi/(1 - e^2)^1.5;
    t = 0:dt:halfPeriod;
elseif (e > 1)
    t = 0:dt:0.99*acos(-1/e);
else
    t = 0:dt:10;
end

% Find the angle at each time via numerical root finding
theta = [];
for tk = t
    if (e < 1)
        % Elliptic
        f = @(th) 2*atan(sqrt((1 - e)/(1 + e))*tan(th/2))/(1 - e^2)^1.5 - e*sin(th)./((1 - e^2)*(1 + e*cos(th))) - tk;
        limits = [-pi, pi];
    elseif (e > 1)
        % Hyperbolic
        f = @(th) -2*atanh(sqrt((e - 1)/(e + 1))*tan(th/2))/(e^2 - 1)^1.5 + e*sin(th)./((e^2 - 1)*(1 + e*cos(th))) - tk;
        limits = [-acos(-1/e), acos(-1/e)]*0.99;
    else
        % Parabolic
        f = @(th) (1/12)*sec(th/2)^3*(3*sin(th/2) + sin(3*th/2)) - tk;
        limits = [-acos(-1/e), acos(-1/e)]*0.99;
    end
    % Calculate the angle theta that gives this time. Since t in (0, T/2),
    % then this answer is unique
    theta = [theta; fzero(f, limits)];
end