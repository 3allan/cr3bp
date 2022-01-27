.. default-role:: math

Trajectory Geometry
*******************

:Author: M. Werner


`r` and `\theta` can be slightly more simplified if we define `e = A/\mu.`

Why define another new variable, and why `e`?
---------------------------------------------

To answer the first question, we want to consider a more mathematical approach.
From a dynamicist's perspective, it's useful to define `e` because it reduces
the amount of parameters needed to study `r` and `\theta` from two (`\mu` and `A`) to one (`e`).
**This means that by studying** `e` **from, say, 0 to 1, we're actually studying**
**all systems** `\mu` **and initial conditions** `A` **such that** `\mu/A = e.`

- For example, if we picked a value of `e`, say `e = 0.1`, and study `A/\mu = 0.1`,
  then we're also studying all the other systems that have `kA/k\mu = 0.1`
  where `k > 0` is just some constant.


We call this quantity `e` because it's short for **eccentricity.**
As we will see in the next section, the radius `r` traces out an ellipse
on the orbital plane; `e` is a parameter that determines the shape of the
ellipse.

With the eccentricity defined, the radius and angle take on the following
forms.

.. math::
    :label: orbitalRadiusWithe

    r = \frac{h^2/\mu}{1 + e\cos\theta}

and

.. math::
    :label: orbitalAngleWithe

    \tan\frac{\theta}{2} = \sqrt{\frac{1 + e}{1 - e}} \tan\frac{E}{2}
    \qquad \text{with} \qquad
    M = E - e \sin E


Closed Orbits `(0 \leqslant e < 1)`
-----------------------------------
With this restriction in mind (`e < 1`), we can evaluate this integral
in terms of elementary functions.

.. math::
    \int^\theta\frac{d\theta}{(1 + e\cos\theta)^2} = \underbrace{\frac{2}{(1 - e^2)^{3/2}}\,\tan^{-1}\!\left(\sqrt{\frac{1 - e}{1 + e}}\tan\frac{\theta}{2}\right) - \frac{e\sin\theta}{(1 - e^2)(1 + e\cos\theta)}}_{\large\chi_e(\theta)}

Since `\chi` is an odd function in `\theta,` it's
convenient to choose `\theta_0 = 0` at time `t_0 = 0`. That is,
begin counting positive time the instant that the (positive) `x` axis
is crossed.
Using this choice, we can now safely integrate the conservation of
angular momentum and write for `|\theta| < \pi` and `e < 1`,

.. math::
    \chi_e(\theta) = \frac{\mu^2}{h^3}t.

In this case, `\chi` being odd also implies that the time
`t` to transit over `[0, \vartheta]` is exactly the same amount
of time (in absolute value) to transit `[-\vartheta, 0]`, where
`\vartheta \in (0, \pi).`
Thus, **motion is both spatially and temporally symmetric about the** `x` **axis.**
Consequently, we now know that *all* trajectories with `e < 1` are
*closed* and complete an orbit with period

.. math::
    T = \lim_{\theta \to \pi^-} 2t = \frac{2\pi h^3/\mu^2}{(1 - e^2)^{3/2}}.

Our objective would be accomplished *if* we could so easily write

.. math::
    \theta = \chi_e^{-1}\!\left(\frac{\mu^2}{h^3}t\right),

but unfortunately, we cannot find an analytical expression for such an
inverse function for *any* `e < 1`.
It is, however, possible (very easy in fact) in the special case of
`e = 0` since `\chi_0(\theta) = \theta,` which indeed abides by
the conservation of angular momentum.
The motion in this case has a constant radius (`h^2/\mu`) and
a constant angular rate (`\mu^2/h^3`) --- a circle.

Open Orbits `(e > 1)`
---------------------
For other trajectories (`e \geqslant 1`), the domain of `\theta`
is necessarily restricted to maintain physical meaning such that

.. math::
    1 + e\cos\theta > 0 \implies |\theta| < \cos^{-1}(-e^{-1})

With this restriction in mind, we can still use the same function
`\chi_e` that was developed for closed orbits, though it would be
convenient to rewrite it to make sense for `e \geqslant 1.`

.. math::
    \chi_e(\theta) = \frac{e\sin\theta}{(e^2 - 1)(1 + e\cos\theta)} - \frac{2}{(e^2 - 1)^{3/2}}\tanh^{-1}\left(\sqrt{\frac{e - 1}{e + 1}}\tan\frac{\theta}{2}\right)

Similarly to the closed orbits, we can choose to define `\theta_0 = 0`
at time `t_0 = 0` such that the motion obeys

.. math::
    \chi_e(\theta) = \frac{\mu^2}{h^3} t.

Since this really is the same function `\chi` that described closed
orbits, **the trajectory is spatially and temporally symmetric about the** `x` **axis.**
That said, it is still impossible to solve analytically for the angular
coordinate as a function of time, even when `e` uniformly approaches
unity.

.. math::
    \lim_{e \to 1} \chi_e(\theta) = \frac{1}{12}\sec^3\frac{\theta}{2}\left(3\sin\frac{\theta}{2} + \sin\frac{3\theta}{2}\right)

Note that since the trajectory is open, it takes *infinite* time to reach
the maximum angle (corresponding to an infinite distance from the origin)
starting from the `x` axis. *However,*

.. math::
    \lim_{e\to\infty}\chi_e(\theta) = 0.

This means that as `e` gets very large, the elapsed time to cover the
interval `(-\pi/2, \pi/2)` is *nothing.* This happens because
trajectories with finite `e` approach the maximum angles
*asymptotically* whereas those with very large `e` basically start
at one limit, `\theta = -\pi/2,` and pass through immediately to the
other limit, `\theta = \pi/2.` Such a trajectory is characteristic of
a *straight line along the* `y` *axis.* (Like having `h = 0`,
this trajectory results in a collision --- a finite-time singularity.)

.. important::
    The trajectory of the reduced mass can be either **closed** or **open**
    depending on the (nonnegative) parameter `e = A/\mu.`

    #. Closed orbits occur when `e < 1.`
        #. **Period**: `T = 2\pi h^3/\big(\mu^2(1 - e^2)^{3/2}\big)`
        #. **Simplest**: Circle
    #. Open orbits occur when `e \geqslant 1.`
        #. **Period**: `T = \infty` if `e < \infty.` Otherwise, `T = 0.`
        #. **Simplest**: Straight line (collision)

    In both cases, we cannot obtain an analytical expression for
    `\theta = \theta(t),` but we can obtain an expression for
    `t = t(\theta).`
