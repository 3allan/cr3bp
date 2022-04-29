clear, clc

% Define eccentricities of orbits to show
eccentricities = [0, 0.5, 0.7, 0.8, 0.9, 1, 1.5, 5];
% eccentricities = [1, 1.5, 5];

% Loop through each orbit and add markers that are equally spaced in time,
% but lie on periapse and apoapse (the x axis).
% 
% By symmetry, we need only to place dots on θ in [0,π]
% - The first dot and last dot are easy; just place them.
%   - The problem is therefore finding timesteps dt such that
%                       mod(T/2, dt) = 0,
%     where T is the period.
%                  T = 2π (h³/μ²) / (1 - e²)³/²
% - For visualization, all trajectories pass through (x,y) = (0,1) so it
%   would look nice to put a point there as well.
%   - Thus, we want timesteps that
t = @(th, e) 2*atan(sqrt((1 - e)/(1 + e))*tan(th/2))/(1 - e^2)^1.5 - e*sin(th)/((1 - e^2)*(1 + e*cos(th)));
plot(nan,nan), hold on, xline(0), yline(0)
colors = ['r', 'k', 'g'];
for e = (eccentricities)
    % We're going to find the next closest spacing of dt to pi/4 such
    % that the angular points are located on the x-axis and at (0,1).
    % 
    % When plotting the orbit, only define half for y > 0 (we can simply 
    % reflect over y = 0 since we know the motion is symmetric about the 
    % x axis)
    if (e == 0)
        % Set time spacing for a circular orbit
        dt = pi/6;
        th = linspace(0,pi,100000);
    elseif (e == 1)
        % t(pi/2,1) -> 2/3, so dt can 2/3/n, where n is natural
        dt = 2/3;
        th = linspace(0,acos(-0.99/e),100000);
    else
        if (e < 1)
            % ============================
            %          Elliptic
            % ============================
            DT = linspace(0.68,0.81,1000000);
            f = mod(t(pi,e), DT) + mod(t(pi/2,e), DT);
            th = linspace(0,pi,100000);
        else
            % ============================
            %         Hyperbolic
            % ============================
            DT = linspace(0.15,0.52,1000000);
            f = mod(t(pi/2,e), DT);
            th = linspace(0,acos(-0.99/e),100000);
        end        
        d2fd2DT = gradient(gradient(f,DT),DT);
        % Find the points of discontinuity
        I = find(abs(d2fd2DT) > 100);
        DT = DT(I);
        f = f(I);
        % Find the point that minimizes the constraint
        [~, I] = min(f);
        DT = DT(I);
        f = f(I);
        dt = DT
    end
    
    % Plot orbit
    color = colors(1+2*heaviside(e-1));
    r = 1./(1 + e*cos(th));
    x = r.*cos(th);
    y = r.*sin(th);
    plot(x,y,x,-y,'color', color)
    axis equal
    % Plot the equal time markers
    % Note: The markers are equal time on each orbit, but not constant
    %       across each orbit. They are picked so that a marker is placed
    %       at theta=0,pi and pi/2
    theta = anglesFromEqualTimesteps(dt, e);
    r = 1./(1 + e*cos(theta));
    x = r.*cos(theta);
    y = r.*sin(theta);
    plot(x,y,'k.',x,-y,'k.')
end

grid on
xlim([-10, 1.25])
ylim([-3,3])
hold off

% α β δ ε θ λ μ π φ ψ Ω ⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹