.. default-role:: math

.. sectnum::
    :start: 3
    :depth: 3

========
Solution
========

:Author: M. Werner

.. admonition:: Plan of Action

    The solution of the *general* 2-body problem is developed several
    different ways utilizing the now known special
    :ref:`properties<Properties>` admitted by the system.

.. contents:: Table of Contents
    :local:
    :backlinks: none
    :depth: 3

Defining a New Coordinate System
================================
Knowing that the motion **must** be 2-dimensional, we can choose a more
convenient coordinate system via a coordinate rotation. Let this rotation
be denoted :math:`\mathbf{R} \in \mathrm{SO}(3)` such that

.. math::
    \begin{pmatrix}x \\ y \\ z\end{pmatrix} = \mathbf{R} \begin{pmatrix}X \\ Y \\ Z\end{pmatrix}.

These two quantities both represent the **same** object :math:`\mathbf{r}`.
This rotation is **not** time-dependent --- that is, :math:`\mathbf{R}` is
a static rotation between the two coordinate systems such that

.. math::
    \dot{\mathbf{R}} \equiv \mathbf{0}.

The standard form of the equations of motion are consequently *unchanged*.



Polar Coordinates `(r, \theta)`
===============================
It is most convenient to utilize the conservation of angular momentum and
the Laplace-Runge-Lenz vector to define the precise action of
:math:`\mathbf{R}` on the two coordinate systems of variables
:math:`(X, Y, Z)` and :math:`(x, y, z)`.

By choosing to orient the :math:`z` axis in the same direction of the
angular momentum and the :math:`x` axis in the same direction of the
Laplace-Runge-Lenz vector, we reduce the solution of the Kepler problem to
determining just 2 unknown quantities. These two quantities are the
parameterizations of polar coordinates,

.. math::
    x &= r \cos\theta \\
    y &= r \sin\theta \\
    z &= 0,
    :label: polarCoordinates

where :math:`r = |\mathbf{r}|` as usual and :math:`\theta` is the angle made
between the reduced mass particle and the :math:`x` axis.

.. figure:: ../../images/kepler_coordinate_rotation.svg
    :width: 362px
    :height: 207px
    :scale: 150 %
    :alt: Example of a planar trajectory taken by the reduced mass in an inertial, but specially chosen, coordinate system
    :align: center

    A "trajectory" in the new coordinates :math:`(x, y, z)` utilizing polar
    coordinates :math:`(r,\theta)`. Note that this trajectory is actually
    impossible since there is a change in the sign of angular momentum, a
    constant of motion.

.. Important:: The trajectory of the relative motion of the two bodies
    (:math:`\mathbf{r}`) *in the orbital plane* is fully determined by the
    set of polar coordinates :math:`(r, \theta)`. The 2-body problem has
    been reduced from determining all 6 variables to only 2 by using
    properties admitted by the conserved quantities.


Differential Equations for `r` and `\theta`
-------------------------------------------
.. admonition:: Recall

    The time rates of change of a vector :math:`x \in \mathbb{R}^3` that's
    expressed in a coordinate system :math:`\mathcal{B}` rotating with
    angular velocity :math:`\Omega` relative to another coordinate system
    :math:`\mathcal{A}` follow

    .. math::
        \frac{dx^\mathcal{A}}{dt} = \frac{dx^\mathcal{B}}{dt} + \Omega \times x^\mathcal{B}

With polar coordinates :math:`(r, \theta)` being used to describe position
within the orbit, it is *extremely* convenient to develop a new set of
differential equations in the cylindrical basis. That is, exchange the
inertial basis for the noninertial cylindrical basis

.. math::
    \{\mathbf{e}_x,\mathbf{e}_y, \mathbf{e}_z\} \longrightarrow \{\mathbf{e}_r,\mathbf{e}_\theta, \mathbf{e}_z\}

and insert the resulting object describing relative positions of the two
bodies (:math:`\mathbf{r}`) into the standard form of the 2-body problem.

This transformation is useful as the expression for the position
simplifies dramatically to

.. math::
    \mathbf{r} = r\,\mathbf{e}_r.

In calculating the **inertial** velocity and acceleration, the time
derivatives **must** be calculated relative to the inertial frame.
Here, the polar coordinate system is rotating with respect to the inertial
coordinate system at the rate :math:`\dot{\theta}` along the axis of
rotation :math:`\mathbf{e}_z`. As such,

.. math::
    \dot{\mathbf{r}} &= \dot{r}\,\mathbf{e}_r + r \dot{\theta}\,\mathbf{e}_\theta \\
    \ddot{\mathbf{r}} &= (\ddot{r} - r\dot{\theta}^2)\mathbf{e}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\mathbf{e}_\theta.

Inserting the inertial acceleration into the standard form equations of
motion provide a set of only two differential equations for the two
unknowns :math:`r` and :math:`\theta`.

.. math::
    \ddot{r} - r\dot{\theta}^2 &= -\frac{\mu}{r^2} \\
    r\ddot{\theta} + 2\dot{r}\dot{\theta} &= 0
    :label: polarEOM


Rewriting the Conserved Quantities `\mathbf{h}`, `\mathbf{A}`, and `E`
----------------------------------------------------------------------
The angular momentum :math:`\mathbf{h}`,
the Laplace-Runge-Lenz vector :math:`\mathbf{A}`, and
the energy :math:`E` are expressed in the polar coordinates
:math:`(r, \theta)`, providing useful relations for analyzing the
relative trajectory of the two bodies.

Angular Momentum `\mathbf{h}`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The angular momentum :math:`\mathbf{h}` expressed in polar coordinates is

  .. math::
      \mathbf{h} &= \mathbf{r} \times \dot{\mathbf{r}} \\
      &= \left(r\,\mathbf{e}_r\right) \times \left(\dot{r}\,\mathbf{e}_r + r \dot{\theta}\,\mathbf{e}_\theta\right) \\
      &= r\dot{r} (\mathbf{e}_r \times \mathbf{e}_r) + r^2\dot{\theta} (\mathbf{e}_r \times \mathbf{e}_\theta) \\
      &= r^2\dot{\theta}\,\mathbf{e}_z.

Since :math:`\mathbf{h} = h \mathbf{e}_z` by construction of `\mathbf{R}`, the conservation of angular momentum provides

    .. math::
        r^2\dot{\theta} = h,
        :label: AMconservation

where :math:`h = |\mathbf{h}|` is a constant of motion.

.. important::
      - Since :math:`h \geqslant 0` and :math:`r^2 > 0`, we know that
        :math:`\dot{\theta} \geqslant 0` **always**.

        - If `\dot{\theta} \equiv 0`, then `h \equiv 0` :eq:`AMconservation` and `\ddot{r} < 0` :eq:`polarEOM`,
          which means :math:`r \to 0` in *finite* time.

      - Interesting motion therefore takes place for :math:`\dot{\theta} > 0`.

Laplace-Runge-Lenz Vector `\mathbf{A}`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Laplace-Runge-Lenz vector :math:`\mathbf{A}` expressed in polar
  coordinates is

.. math::
    \mathbf{A} &= \dot{\mathbf{r}} \times \mathbf{h} - \frac{\mu}{r}\mathbf{r} \\
    &= (\dot{r}\,\mathbf{e}_r + r\dot{\theta}\,\mathbf{e}_\theta) \times (r^2\dot{\theta}\,\mathbf{e}_z) - \frac{\mu}{r} (r \,\mathbf{e}_r) \\
    &= r^2\dot{r}\dot{\theta}(\mathbf{e}_r \times \mathbf{e}_z) + r^3\dot{\theta}^2(\mathbf{e}_\theta \times \mathbf{e}_z) - \mu\,\mathbf{e}_r \\
    &= r^2\dot{r}\dot{\theta}(-\mathbf{e}_\theta) + r^3\dot{\theta}^2(\mathbf{e}_r) - \mu\,\mathbf{e}_r \\
    &= (r^3\dot{\theta}^2 - \mu)\mathbf{e}_r - r^2\dot{r}\dot{\theta}\,\mathbf{e}_\theta \\
    &= A \underbrace{(\cos\theta\,\mathbf{e}_r - \sin\theta\,\mathbf{e}_\theta)}_{\mathbf{e}_x}.

The last equality holds by construction of `\mathbf{R}`.

To summarize, we get two scalar equations from the invariance of the Laplace-Runge-Lenz vector,

.. math::
  :label: LaplaceRungeLenz

  r^3\dot{\theta}^2 - \mu &= A\cos\theta \\
  r^2\dot{r}\dot{\theta} &= A\sin\theta,

where :math:`A = |\mathbf{A}|` is a constant of motion.

.. important::
    Paired with the conservation of angular momentum :eq:`AMconservation`,
    these two statements provide *very* direct expressions of :math:`r` and
    :math:`\dot{r}`.

Energy `E`
~~~~~~~~~~
The energy :math:`E` expressed in polar coordinates is

.. math::
    :label: eq:energy

    E = \frac{1}{2}\underbrace{(\dot{r}^2 + r^2\dot{\theta}^2)}_{v^2 = \dot{\mathbf{r}} \cdot \dot{\mathbf{r}}} - \frac{\mu}{r}.

where :math:`E` is a constant of motion.

.. important::
    - Paired with angular momentum :eq:`AMconservation`, this expression "integrates" the
      :math:`\ddot{r}` equation of motion with integration constant
      :math:`2E`.
    - Similarly, this relation provides another expression for
      :math:`\dot{\theta}` in addition to that from the conservation of
      angular momentum using the knowledge that :math:`\dot{\theta} > 0`
      for interesting motion.



The Orbital Radius `r`
======================
In this coordinate system with variables :math:`(x, y, z)`, the orbital
radius :math:`r` is obtainable using several different methods.
In all cases, the orbital radius is

.. math::
    :label: orbitalRadius

    r = \frac{h^2}{\mu + A\cos\theta},

where `\mu` depends only on the masses of the two bodies and `h`, `A` are
constants of motion.

.. important::
    The radius `r` is a **known** function of the angle `\theta` and is
    parameterized by constants determined by the system (`\mu`) and
    initial conditions (`h` and `A`).

From the Laplace-Runge-Lenz Vector `\mathbf{A}`
-----------------------------------------------
.. admonition:: Recall

    For any :math:`x, y, z \in \mathbb{R}^3`, the scalar triple product
    satisfies

    .. math::
        x \cdot (y \times z) = y \cdot (z \times x) = z \cdot (x \times y).

The Laplace-Runge-Lenz vector can be used to obtain an expression for the
orbital radius :math:`r` as a function of the polar coordinate
:math:`\theta` *very* directly.

Since :math:`\theta` is measured from the :math:`x` axis, which is aligned
with the Laplace-Runge-Lenz vector `\mathbf{A}`, one can see that

.. math::
    \mathbf{A} \cdot \mathbf{r} &= \left(\dot{\mathbf{r}} \times \mathbf{h} - \frac{\mu}{r}\mathbf{r}\right) \cdot \mathbf{r} \\
    &= (\dot{\mathbf{r}} \times \mathbf{h}) \cdot \mathbf{r} - \left(\frac{\mu}{r}\mathbf{r}\right) \cdot \mathbf{r} \\
    &= \mathbf{r} \cdot (\dot{\mathbf{r}} \times \mathbf{h}) - \frac{\mu}{r} (\mathbf{r} \cdot \mathbf{r}) \\
    &= \mathbf{h} \cdot (\mathbf{r} \times \dot{\mathbf{r}}) - \mu r \\
    &= \mathbf{h} \cdot \mathbf{h} - \mu r \\
    &= h^2 - \mu r \\
    &= A r \cos\theta.

Alternatively, knowing :eq:`AMconservation` and combining it with :eq:`LaplaceRungeLenz`
yields the radius `r` even more simply.

.. math::
    A\cos\theta &= r^3\dot{\theta}^2 - \mu \\
    &= \frac{h^2}{r} - \mu.

In either approach, the radius `r` is obtained as a function of the angle `\theta` in accordance with :eq:`orbitalRadius`. `\blacksquare`

From the `\ddot{r}` Equation
----------------------------
Combined with the conservation of angular momentum :eq:`AMconservation`, the :math:`\ddot{r}` equation of motion :eq:`polarEOM` provides

.. math::
    \ddot{r} &= r\dot{\theta}^2 - \frac{\mu}{r^2} \\
    &= \frac{h^2}{r^3} - \frac{\mu}{r^2}.

We wish to convert the derivatives in time :math:`t` to those in the angular
coordinate :math:`\theta` to understand the geometry of the trajectory in
polar coordinates. Using the conservation of angular momentum :eq:`AMconservation` repeatedly, we see

.. math::
    \frac{d^2 r}{d\theta^2} &= \frac{d}{d\theta}\left(\frac{dr}{d\theta}\right) \\
    &= \frac{d}{d\theta}\left(\frac{\dot{r}}{\dot{\theta}}\right) \\
    &= \frac{d}{d\theta}\left(\frac{r^2\dot{r}}{h}\right) \\
    &= \frac{1}{\dot{\theta}}\frac{d}{dt}\left(\frac{r^2\dot{r}}{h}\right) \\
    &= \frac{r^2}{h^2}(2r\dot{r}^2 + r^2 \ddot{r}) \\
    &= \frac{r^2}{h^2}\left(2r\left(\frac{h}{r^2}\frac{dr}{d\theta}\right)^{\!2} + r^2 \left(\frac{h^2}{r^3} - \frac{\mu}{r^2}\right)\right) \\
    &= \frac{r^2}{h^2}\left(2\frac{h^2}{r^3}\left(\frac{dr}{d\theta}\right)^{\!2} + \frac{h^2}{r} - \mu\right) \\
    &= \frac{2}{r}\left(\frac{dr}{d\theta}\right)^{\!2} - \frac{\mu r^2}{h^2} + r.

Despite offering a description of the trajectory's geometry in space as
opposed to time, *this* differential equation still proves to be formidable
in obtaining a solution. However, a final, clever change of variables *will*
yield a useful relation by letting :math:`\eta = 1/r`. In this case,

.. math::
    \frac{d^2\eta}{d\theta^2} &= \frac{d}{d\theta}\left(\frac{d\eta}{d\theta}\right) \\
    &= \frac{d}{d\theta}\left(-\frac{1}{r^2}\frac{dr}{d\theta}\right) \\
    &= -\frac{1}{h}\frac{d\dot{r}}{d\theta} \\
    &= -\frac{1}{h}\frac{d}{d\theta}\left(\frac{dr}{d\theta}\dot{\theta}\right) \\
    &= -\frac{1}{h}\frac{d}{d\theta}\left(\frac{dr}{d\theta}\frac{h}{r^2}\right) \\
    &= -\frac{1}{r^2}\frac{d^2r}{d\theta^2} + \frac{2}{r^3}\left(\frac{dr}{d\theta}\right)^{\!2} \\
    &= -\frac{1}{r^2}\left(\frac{2}{r}\left(\frac{dr}{d\theta}\right)^{\!2} - \frac{\mu r^2}{h^2} + r\right) + \frac{2}{r^3}\left(\frac{dr}{d\theta}\right)^{\!2} \\
    &= \frac{\mu}{h^2} - \frac{1}{r} \\
    &= \frac{\mu}{h^2} - \eta.

With this transformation, we see that we are offered something describing
a linear oscillator,
where both :math:`\mu` and :math:`h` are (positive) constants. We can
therefore immediately write the general solution as

.. math:: \eta = \frac{\mu}{h^2} + C \cos(\theta - \omega),

where both :math:`C` and :math:`\omega` are constants of integration.
Note that :math:`C` represents an amplitude and, as such, satisfies
:math:`C \geqslant 0`.
The orbital radius (:math:`r = 1/\eta`) is then

.. math::
    r = \frac{h^2}{\mu + (C/h^2) \cos(\theta - \omega)}.

Since :math:`\mathbf{A}` already provides a constant direction in the
orbital plane from which :math:`\theta` is measured, we do not wish to
shift the angle :math:`\theta` to be measured with respect to anything else
(yet). Thus, we can take

.. math::
    \omega = 0

without loss of generality in *this* coordinate frame.
(This quantity :math:`\omega` is called the *argument of periapsis*, which
is naturally useful for the transformation between the :math:`(X, Y, Z)`
and :math:`(x, y, z)` coordinate systems.)

To determine the constant :math:`C`, we can calculate the time derivative
of the orbital radius exactly and then turn to the invariance of the
Laplace-Runge-Lenz vector `\mathbf{A}` :eq:`LaplaceRungeLenz` combined with
conservation of angular momentum :eq:`AMconservation` to compare expressions
for :math:`\dot{r}.`

.. math::
    \dot{r} &= \frac{C\sin\theta}{(\mu + (C/h^2) \cos\theta)^2}\dot{\theta} \\
    &= \left(\frac{r^2}{h^4}C\sin\theta\right)\left(\frac{h}{r^2}\right) \\
    &= \frac{C}{h^3}\sin\theta \\
    &= \frac{A}{h}\sin\theta

We therefore immediately conclude that the integration constant :math:`C`
is expressed in terms of known quantities as

.. math::
    C = A h^2.

From an analysis of pure differential equations using only the conservation of momentum :eq:`AMconservation`, the orbital radius `r` is obtained as a function of the angle `\theta` in accordance with :eq:`orbitalRadius`. `\blacksquare`

The Orbital Angle `\theta`
==========================
Knowing the orbital radius :math:`r` to be a function of :math:`\theta`,
we would most like to know the angular coordinate :math:`\theta` as a
function of time :math:`t`. This would fully complete the parameterization
as then :math:`\mathbf{r} = \mathbf{r}(t)` would be a known function for all
time.

Like the orbital radius, the angular coordinate :math:`\theta` is
expressible using several different methods.
However, unlike the orbital radius, these expressions prove to be
difficult in obtaining :math:`\theta = \theta(t).` Instead, we can obtain
:math:`t = t(\theta).`
As we shall see, inverting this function :math:`t` is, indeed, difficult.

From Angular Momentum `\mathbf{h}`
----------------------------------
The conservation of angular momentum states :math:`r^2\dot{\theta} = h,`
but the orbital radius :math:`r` is now a **known** function of **only**
:math:`\theta.` Thus, we can write

.. math::
    \dot{\theta} &= \frac{h}{r^2} \\
    &= \frac{(\mu + A\cos\theta)^2}{h^3},

which provides a separable equation for `\theta`.
Naively integrating obtains

.. math::
    :label: eq:naiveIntegration

    \int_{\theta_0}^\theta \frac{d\theta'}{(\mu + A\cos\theta')^2} = \frac{1}{h^3}\int_{t_0}^t dt',

but this expression turns out *not* to be entirely true for *any* arbitrary
:math:`\theta` since we only know that :math:`\mu, A \geqslant 0` (i.e. it is
possible that :math:`A \geqslant \mu,` in which case the integrand becomes
periodically undefined).

This relation is developed further when exploring the :ref:`trajectory's geometry <Trajectory Geometry>`.

From the `\ddot{\theta}` Equation
--------------------------------------
Equation :eq:`polarEOM` provides several different ways to go about
trying to obtain `\theta = \theta(t)`.

Using Angular Momentum `\mathbf{h}`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using a Total Derivative
~~~~~~~~~~~~~~~~~~~~~~~~
Using the known solution for the orbital radius :math:`r` and the
conservation of the Laplace-Runge-Lenz vector :math:`\mathbf{A}` along
with the conservation of angular momentum, the
:math:`\ddot{\theta}` equation of motion provides

.. math::
    0 &= \ddot{\theta} + 2\frac{\dot{r}}{r}\dot{\theta} \\
    &= \ddot{\theta} + 2\frac{(A/h)\sin\theta}{h^2/(\mu + A\cos\theta)}\dot{\theta} \\
    &= \ddot{\theta} + 2\frac{A}{h^3}(\mu + A\cos\theta)\sin\theta\dot{\theta} \\
    &= \ddot{\theta} + 2\frac{\mu^2 e}{h^3}(1 + e\cos\theta)\sin\theta\dot{\theta} \\
    &= \frac{d}{dt}\left(\dot{\theta} - 2\frac{\mu^2}{h^3}\left(e\cos\theta + \frac{e^2}{2}\cos^2\theta\right)\right).

We have effectively integrated the equation of motion once, picking up an
integration constant :math:`C,` which we can evaluate using the
conservation of angular momentum or the conservation of energy.

.. math::
    \dot{\theta} &= 2\frac{\mu^2}{h^3}\left(e\cos\theta + \frac{e^2}{2}\cos^2\theta\right) + C \\
    &= \frac{h}{r^2} \\
    &= \frac{\mu^2}{h^3}(1 + e\cos\theta)^2 \\
    &= \frac{\mu^2}{h^3}(1 + 2e\cos\theta + e^2\cos^2\theta) \\
    &= 2\frac{\mu^2}{h^3}\left(e\cos\theta + \frac{e^2}{2}\cos^2\theta\right) + \frac{\mu^2}{h^3}.

Thus, the constant is :math:`C = \mu^2/h^3,` providing

.. math::
    \dot{\theta} = \frac{\mu^2}{h^3}(1 + e\cos\theta)^2.

The outcome is identical to that obtained from analyzing the conservation
of angular momentum directly.

Trajectory Geometry
===================

Closed Orbits `(0 \leqslant e < 1)`
-----------------------------------
With this restriction in mind (:math:`e < 1`), we can evaluate this integral
in terms of elementary functions.

.. math::
    \int^\theta\frac{d\theta}{(1 + e\cos\theta)^2} = \underbrace{\frac{2}{(1 - e^2)^{3/2}}\,\tan^{-1}\!\left(\sqrt{\frac{1 - e}{1 + e}}\tan\frac{\theta}{2}\right) - \frac{e\sin\theta}{(1 - e^2)(1 + e\cos\theta)}}_{\large\chi_e(\theta)}

Since :math:`\chi` is an odd function in :math:`\theta,` it's
convenient to choose :math:`\theta_0 = 0` at time :math:`t_0 = 0`. That is,
begin counting positive time the instant that the (positive) :math:`x` axis
is crossed.
Using this choice, we can now safely integrate the conservation of
angular momentum and write for :math:`|\theta| < \pi` and :math:`e < 1`,

.. math::
    \chi_e(\theta) = \frac{\mu^2}{h^3}t.

In this case, :math:`\chi` being odd also implies that the time
:math:`t` to transit over :math:`[0, \vartheta]` is exactly the same amount
of time (in absolute value) to transit :math:`[-\vartheta, 0]`, where
:math:`\vartheta \in (0, \pi).`
Thus, **motion is both spatially and temporally symmetric about the** :math:`x` **axis.**
Consequently, we now know that *all* trajectories with :math:`e < 1` are
*closed* and complete an orbit with period

.. math::
    T = \lim_{\theta \to \pi^-} 2t = \frac{2\pi h^3/\mu^2}{(1 - e^2)^{3/2}}.

Our objective would be accomplished *if* we could so easily write

.. math::
    \theta = \chi_e^{-1}\!\left(\frac{\mu^2}{h^3}t\right),

but unfortunately, we cannot find an analytical expression for such an
inverse function for *any* :math:`e < 1`.
It is, however, possible (very easy in fact) in the special case of
:math:`e = 0` since :math:`\chi_0(\theta) = \theta,` which indeed abides by
the conservation of angular momentum.
The motion in this case has a constant radius (:math:`h^2/\mu`) and
a constant angular rate (:math:`\mu^2/h^3`) --- a circle.

Open Orbits `(e > 1)`
---------------------
For other trajectories (:math:`e \geqslant 1`), the domain of :math:`\theta`
is necessarily restricted to maintain physical meaning such that

.. math::
    1 + e\cos\theta > 0 \implies |\theta| < \cos^{-1}(-e^{-1})

With this restriction in mind, we can still use the same function
:math:`\chi_e` that was developed for closed orbits, though it would be
convenient to rewrite it to make sense for :math:`e \geqslant 1.`

.. math::
    \chi_e(\theta) = \frac{e\sin\theta}{(e^2 - 1)(1 + e\cos\theta)} - \frac{2}{(e^2 - 1)^{3/2}}\tanh^{-1}\left(\sqrt{\frac{e - 1}{e + 1}}\tan\frac{\theta}{2}\right)

Similarly to the closed orbits, we can choose to define :math:`\theta_0 = 0`
at time :math:`t_0 = 0` such that the motion obeys

.. math::
    \chi_e(\theta) = \frac{\mu^2}{h^3} t.

Since this really is the same function :math:`\chi` that described closed
orbits, **the trajectory is spatially and temporally symmetric about the** :math:`x` **axis.**
That said, it is still impossible to solve analytically for the angular
coordinate as a function of time, even when :math:`e` uniformly approaches
unity.

.. math::
    \lim_{e \to 1} \chi_e(\theta) = \frac{1}{12}\sec^3\frac{\theta}{2}\left(3\sin\frac{\theta}{2} + \sin\frac{3\theta}{2}\right)

Note that since the trajectory is open, it takes *infinite* time to reach
the maximum angle (corresponding to an infinite distance from the origin)
starting from the :math:`x` axis. *However,*

.. math::
    \lim_{e\to\infty}\chi_e(\theta) = 0.

This means that as :math:`e` gets very large, the elapsed time to cover the
interval :math:`(-\pi/2, \pi/2)` is *nothing.* This happens because
trajectories with finite :math:`e` approach the maximum angles
*asymptotically* whereas those with very large :math:`e` basically start
at one limit, :math:`\theta = -\pi/2,` and pass through immediately to the
other limit, :math:`\theta = \pi/2.` Such a trajectory is characteristic of
a *straight line along the* :math:`y` *axis.* (Like having :math:`h = 0`,
this trajectory results in a collision --- a finite-time singularity.)

.. important::
    The trajectory of the reduced mass can be either **closed** or **open**
    depending on the (nonnegative) parameter :math:`e = A/\mu.`

    #. Closed orbits occur when :math:`e < 1.`
        #. **Period**: :math:`T = 2\pi h^3/\big(\mu^2(1 - e^2)^{3/2}\big)`
        #. **Simplest**: Circle
    #. Open orbits occur when :math:`e \geqslant 1.`
        #. **Period**: :math:`T = \infty` if :math:`e < \infty.` Otherwise, :math:`T = 0.`
        #. **Simplest**: Straight line (collision)

    In both cases, we cannot obtain an analytical expression for
    :math:`\theta = \theta(t),` but we can obtain an expression for
    :math:`t = t(\theta).`

Kepler's Equation
=================
Unfortunately, we cannot express :math:`\theta = \theta(t)` analytically
for any general :math:`e` analyzing conserved quantities and the governing
differential equation. We are therefore forced to turn to other methods.

...

.. |date| date:: %D
.. |time| date:: %H:%M:%S

.. footer:: This document was generated on |date| at |time|.