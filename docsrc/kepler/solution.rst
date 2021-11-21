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

Polar coordinates `(r, \theta)`
===============================
Knowing that the motion **must** be 2-dimensional, we can choose a more
convenient coordinate system via a coordinate rotation. Let this rotation
be denoted `\mathbf{R} \in \mathrm{SO}(3)` such that

.. math::
    \begin{pmatrix}x \\ y \\ z\end{pmatrix} = \mathbf{R} \begin{pmatrix}X \\ Y \\ Z\end{pmatrix}.

These two quantities both represent the **same** object `\mathbf{r}`.
This rotation is **not** time-dependent --- that is, `\mathbf{R}` is
a static rotation between the two coordinate systems such that

.. math::
    \dot{\mathbf{R}} \equiv \mathbf{0}.

The standard form of the equations of motion are consequently *unchanged*.

----

It is most convenient to utilize the conservation of angular momentum and
the Laplace-Runge-Lenz (LRL) vector to define the precise action of
`\mathbf{R}` on the two coordinate systems of variables
`(X, Y, Z)` and `(x, y, z)`.

By choosing to orient the `z` axis in the same direction of the
angular momentum and the `x` axis in the same direction of the
LRL vector, we reduce the solution of the Kepler problem to
determining just 2 unknown quantities. These two quantities are the
parameterizations of polar coordinates,

.. math::
    x &= r \cos\theta \\
    y &= r \sin\theta \\
    z &= 0,
    :label: polarCoordinates

where `r = |\mathbf{r}|` as usual and `\theta` is the angle made
between the reduced mass particle and the `x` axis.

.. figure:: ../../images/kepler_coordinate_rotation.svg
    :width: 362px
    :height: 207px
    :scale: 150 %
    :alt: Example of a planar trajectory taken by the reduced mass in an inertial, but specially chosen, coordinate system
    :align: center

    A "trajectory" in the new coordinates `(x, y, z)` utilizing polar
    coordinates `(r,\theta)`. Note that this trajectory is actually
    impossible since there is a change in the sign of angular momentum, a
    constant of motion.

.. Important:: The trajectory of the relative motion of the two bodies
    (`\mathbf{r}`) *in the orbital plane* is fully determined by the
    set of polar coordinates `(r, \theta)`. The 2-body problem has
    been reduced from determining all 6 variables to only 2 by using
    properties admitted by the conserved quantities.


ODEs for `r` and `\theta`
-------------------------------------------
.. admonition:: Recall

    The time rates of change of a vector `x \in \mathbb{R}^3` that's
    expressed in a coordinate system `\mathcal{B}` rotating with
    angular velocity `\Omega` relative to another coordinate system
    `\mathcal{A}` follow

    .. math::
        \sideset{}{^{\!\mathcal{A}}}{\left(\frac{dx}{dt}\right)} = \sideset{}{^{\!\mathcal{B}}}{\left(\frac{dx}{dt}\right)} + \ \Omega \times x^\mathcal{B}

With polar coordinates `(r, \theta)` being used to describe position
within the orbit, it is *extremely* convenient to develop a new set of
differential equations in the cylindrical basis. That is, exchange the
inertial basis for the noninertial cylindrical basis

.. math::
    \{\mathbf{e}_x,\mathbf{e}_y, \mathbf{e}_z\} \longrightarrow \{\mathbf{e}_r,\mathbf{e}_\theta, \mathbf{e}_z\}

and insert the resulting object describing relative positions of the two
bodies (`\mathbf{r}`) into the standard form of the 2-body problem.

This transformation is useful as the expression for the position
simplifies dramatically to

.. math::
    \mathbf{r} = r\,\mathbf{e}_r.

----

In calculating the **inertial** velocity and acceleration, the time
derivatives **must** be calculated relative to the inertial frame.
Here, the polar coordinate system is rotating with respect to the inertial
coordinate system at the rate `\dot{\theta}` along the axis of
rotation `\mathbf{e}_z`. As such,

.. math::
    \dot{\mathbf{r}} &= \dot{r}\,\mathbf{e}_r + r \dot{\theta}\,\mathbf{e}_\theta \\
    \ddot{\mathbf{r}} &= (\ddot{r} - r\dot{\theta}^2)\mathbf{e}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\mathbf{e}_\theta.

Inserting the inertial acceleration into the standard form equations of
motion provide a set of only two differential equations for the two
unknowns `r` and `\theta`.

.. math::
    \ddot{r} - r\dot{\theta}^2 &= -\frac{\mu}{r^2} \\
    r\ddot{\theta} + 2\dot{r}\dot{\theta} &= 0
    :label: polarEOM


Conserved quantities
------------------------------------------------------------------------
The angular momentum, LRL vector, and energy are expressed in the polar coordinates
`(r, \theta)`, providing useful relations for analyzing the
relative trajectory of the two bodies.

Angular momentum
~~~~~~~~~~~~~~~~
The angular momentum `\mathbf{h}` expressed in polar coordinates is

.. math::
  \mathbf{h} &= \mathbf{r} \times \dot{\mathbf{r}} \\
  &= \left(r\,\mathbf{e}_r\right) \times \left(\dot{r}\,\mathbf{e}_r + r \dot{\theta}\,\mathbf{e}_\theta\right) \\
  &= r\dot{r} (\mathbf{e}_r \times \mathbf{e}_r) + r^2\dot{\theta} (\mathbf{e}_r \times \mathbf{e}_\theta) \\
  &= r^2\dot{\theta}\,\mathbf{e}_z.

Since `\mathbf{h} = h \mathbf{e}_z` too by construction of `\mathbf{R}` (where `h = |\mathbf{h}|` is a constant of motion), the conservation of angular momentum provides

.. math::
  \boxed{r^2\dot{\theta} = h.}
  :label: AMconservation

.. important::
      - Since `h \geqslant 0` and `r^2 > 0`, we know that
        `\dot{\theta} \geqslant 0` **always**.

        - If `\dot{\theta} \equiv 0`, then `h \equiv 0` :eq:`AMconservation` and `\ddot{r} < 0` :eq:`polarEOM`,
          which means `r \to 0` in *finite* time.

      - Interesting motion therefore takes place for `\dot{\theta} > 0`.

LRL vector
~~~~~~~~~~~~~~~~~~~~~~~~~
The LRL vector `\mathbf{A}` expressed in polar
coordinates is

.. math::
    \mathbf{A} &= \dot{\mathbf{r}} \times \mathbf{h} - \frac{\mu}{r}\mathbf{r} \\
    &= (\dot{r}\,\mathbf{e}_r + r\dot{\theta}\,\mathbf{e}_\theta) \times (r^2\dot{\theta}\,\mathbf{e}_z) - \frac{\mu}{r} (r \,\mathbf{e}_r) \\
    &= r^2\dot{r}\dot{\theta}(\mathbf{e}_r \times \mathbf{e}_z) + r^3\dot{\theta}^2(\mathbf{e}_\theta \times \mathbf{e}_z) - \mu\,\mathbf{e}_r \\
    &= r^2\dot{r}\dot{\theta}(-\mathbf{e}_\theta) + r^3\dot{\theta}^2(\mathbf{e}_r) - \mu\,\mathbf{e}_r \\
    &= (r^3\dot{\theta}^2 - \mu)\mathbf{e}_r - r^2\dot{r}\dot{\theta}\,\mathbf{e}_\theta \\
    &= A \underbrace{(\cos\theta\,\mathbf{e}_r - \sin\theta\,\mathbf{e}_\theta)}_{\mathbf{e}_x}.

The last equality holds by construction of `\mathbf{R}`.

To summarize, we get two scalar equations from the invariance of the LRL vector,

.. math::
  :label: LaplaceRungeLenz

  r^2\dot{r}\dot{\theta} &= A\sin\theta, \\
  r^3\dot{\theta}^2 - \mu &= A\cos\theta,

where `A = |\mathbf{A}|` is a constant of motion.

.. important::
    Paired with the conservation of angular momentum :eq:`AMconservation`,
    these two statements provide *very* direct expressions of `r` and
    `\dot{r}`.

Energy
~~~~~~
The energy `E` expressed in polar coordinates is

.. math::
    :label: eq:energy

    E = \frac{1}{2}\underbrace{(\dot{r}^2 + r^2\dot{\theta}^2)}_{v^2 = \dot{\mathbf{r}} \cdot \dot{\mathbf{r}}} - \frac{\mu}{r}.

where `E` is a constant of motion.

.. important::
    - Paired with angular momentum :eq:`AMconservation`, this expression "integrates" the
      `\ddot{r}` equation of motion with integration constant
      `2E`.
    - Similarly, this relation provides another expression for
      `\dot{\theta}` in addition to that from the conservation of
      angular momentum using the knowledge that `\dot{\theta} > 0`
      for interesting motion.



The orbital radius `r`
======================
In this coordinate system with variables `(x, y, z)`, the orbital
radius `r` is obtainable using several different methods.
In all cases, the orbital radius is

.. math::
    :label: orbitalRadius

    \boxed{r = \frac{h^2}{\mu + A\cos\theta}.}

.. important::
    The radius `r` is a **known** function of the angle `\theta` and is
    parameterized by constants determined by the system (`\mu`) and
    initial conditions (`h` and `A`).

from the LRL vector
----------------------------------
.. admonition:: Recall

    For any `x, y, z \in \mathbb{R}^3`, the scalar triple product
    satisfies

    .. math::
        x \cdot (y \times z) = y \cdot (z \times x) = z \cdot (x \times y).

The LRL vector can be used to obtain an expression for the
orbital radius `r` as a function of the polar coordinate
`\theta` *very* directly.

Since `\theta` is measured from the `x` axis, which is aligned
with the LRL vector `\mathbf{A}`, we have

.. math::
    \mathbf{A} \cdot \mathbf{r} &= \left(\dot{\mathbf{r}} \times \mathbf{h} - \frac{\mu}{r}\mathbf{r}\right) \cdot \mathbf{r} \\
    &= (\dot{\mathbf{r}} \times \mathbf{h}) \cdot \mathbf{r} - \left(\frac{\mu}{r}\mathbf{r}\right) \cdot \mathbf{r} \\
    &= \mathbf{r} \cdot (\dot{\mathbf{r}} \times \mathbf{h}) - \frac{\mu}{r} (\mathbf{r} \cdot \mathbf{r}) \\
    &= \mathbf{h} \cdot (\mathbf{r} \times \dot{\mathbf{r}}) - \mu r \\
    &= \mathbf{h} \cdot \mathbf{h} - \mu r \\
    &= h^2 - \mu r \\
    &= A r \cos\theta.

----

Alternatively, knowing :eq:`AMconservation` and combining it with :eq:`LaplaceRungeLenz`
yields the radius `r` even more simply.

.. math::
    A\cos\theta &= r^3\dot{\theta}^2 - \mu \\
    &= \frac{h^2}{r} - \mu.

In either approach, the radius `r` is obtained as a function of the angle `\theta` in accordance with :eq:`orbitalRadius`. `\blacksquare`

from the `\ddot{r}` ODE
----------------------------
Combined with the conservation of angular momentum :eq:`AMconservation`, the `\ddot{r}` equation of motion :eq:`polarEOM` provides

.. math::
    \ddot{r} &= r\dot{\theta}^2 - \frac{\mu}{r^2} \\
    &= \frac{h^2}{r^3} - \frac{\mu}{r^2}.

We wish to convert the derivatives in time `t` to those in the angular
coordinate `\theta` to understand the geometry of the trajectory in
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
yield a useful relation by letting `\eta = 1/r`. In this case,

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
where both `\mu` and `h` are (positive) constants. We can
therefore immediately write the general solution as

.. math:: \eta = \frac{\mu}{h^2} + C \cos(\theta - \omega),

where both `C` and `\omega` are constants of integration.
Note that `C` represents an amplitude and, as such, satisfies
`C \geqslant 0`.
The orbital radius (`r = 1/\eta`) is then

.. math::
    r = \frac{h^2}{\mu + (C/h^2) \cos(\theta - \omega)}.

Since `\mathbf{A}` already provides a constant direction in the
orbital plane from which `\theta` is measured, we do not wish to
shift the angle `\theta` to be measured with respect to anything else
(yet). Thus, we can take

.. math::
    \omega = 0

without loss of generality in *this* coordinate frame.
(This quantity `\omega` is called the *argument of periapsis*, which
is naturally useful for the transformation between the `(X, Y, Z)`
and `(x, y, z)` coordinate systems.)

To determine the constant `C`, we can calculate the time derivative
of the orbital radius exactly and then turn to the invariance of the
LRL vector `\mathbf{A}` :eq:`LaplaceRungeLenz` combined with
conservation of angular momentum :eq:`AMconservation` to compare expressions
for `\dot{r}.`

.. math::
    \dot{r} &= \frac{C\sin\theta}{(\mu + (C/h^2) \cos\theta)^2}\dot{\theta} \\
    &= \left(\frac{r^2}{h^4}C\sin\theta\right)\left(\frac{h}{r^2}\right) \\
    &= \frac{C}{h^3}\sin\theta \\
    &= \frac{A}{h}\sin\theta

We therefore immediately conclude that the integration constant `C`
is expressed in terms of known quantities as

.. math::
    C = A h^2.

From an analysis of pure differential equations using only the conservation of momentum :eq:`AMconservation`, the orbital radius `r` is obtained as a function of the angle `\theta` in accordance with :eq:`orbitalRadius`. `\blacksquare`

The orbital angle `\theta`
==========================
Knowing the orbital radius `r` to be a function of `\theta`,
we would most like to know the angular coordinate `\theta` as a
function of time `t`. This would fully complete the parameterization
as then `\mathbf{r} = \mathbf{r}(t)` would be a known function for all
time.

Like the orbital radius, the angular coordinate `\theta` is
expressible using several different methods.
However, unlike the orbital radius, these expressions prove to be
difficult in obtaining `\theta = \theta(t).` Instead, we can obtain
`t = t(\theta).`
As we shall see, inverting this function `t` is, indeed, difficult.

from angular momentum
---------------------
The conservation of angular momentum states `r^2\dot{\theta} = h,`
but the orbital radius `r` is now a **known** function of **only**
`\theta.` Thus, we can write

.. math::
    \dot{\theta} &= \frac{h}{r^2} \\
    &= \frac{(\mu + A\cos\theta)^2}{h^3},

which provides a separable equation for `\theta`.
Naively integrating obtains

.. math::
    :label: eq:naiveIntegration

    \int_{\theta_0}^\theta \frac{d\theta'}{(\mu + A\cos\theta')^2} = \frac{1}{h^3}\int_{t_0}^t dt',

but this expression turns out *not* to be entirely true for *any* arbitrary
`\theta` since we only know that `\mu, A \geqslant 0` (i.e. it is
possible that `A \geqslant \mu,` in which case the integrand becomes
periodically undefined).

This relation is developed further when exploring the :ref:`trajectory's geometry <Trajectory Geometry>`.

from the `\ddot{\theta}` ODE
--------------------------------------
Equation :eq:`polarEOM` provides several different ways to go about
trying to obtain `\theta = \theta(t)`.

using angular momentum
~~~~~~~~~~~~~~~~~~~~~~

using a total derivative
~~~~~~~~~~~~~~~~~~~~~~~~
Using the known solution for the orbital radius `r` and the
conservation of the LRL vector `\mathbf{A}` along
with the conservation of angular momentum, the
`\ddot{\theta}` equation of motion provides

.. math::
    0 &= \ddot{\theta} + 2\frac{\dot{r}}{r}\dot{\theta} \\
    &= \ddot{\theta} + 2\frac{(A/h)\sin\theta}{h^2/(\mu + A\cos\theta)}\dot{\theta} \\
    &= \ddot{\theta} + 2\frac{A}{h^3}(\mu + A\cos\theta)\sin\theta\dot{\theta} \\
    &= \ddot{\theta} + 2\frac{\mu^2 e}{h^3}(1 + e\cos\theta)\sin\theta\dot{\theta} \\
    &= \frac{d}{dt}\left(\dot{\theta} - 2\frac{\mu^2}{h^3}\left(e\cos\theta + \frac{e^2}{2}\cos^2\theta\right)\right).

We have effectively integrated the equation of motion once, picking up an
integration constant `C,` which we can evaluate using the
conservation of angular momentum or the conservation of energy.

.. math::
    \dot{\theta} &= 2\frac{\mu^2}{h^3}\left(e\cos\theta + \frac{e^2}{2}\cos^2\theta\right) + C \\
    &= \frac{h}{r^2} \\
    &= \frac{\mu^2}{h^3}(1 + e\cos\theta)^2 \\
    &= \frac{\mu^2}{h^3}(1 + 2e\cos\theta + e^2\cos^2\theta) \\
    &= 2\frac{\mu^2}{h^3}\left(e\cos\theta + \frac{e^2}{2}\cos^2\theta\right) + \frac{\mu^2}{h^3}.

Thus, the constant is `C = \mu^2/h^3,` providing

.. math::
    \dot{\theta} = \frac{\mu^2}{h^3}(1 + e\cos\theta)^2.

The outcome is identical to that obtained from analyzing the conservation
of angular momentum directly.



Kepler's equation
-----------------
Unfortunately, we cannot express `\theta = \theta(t)` analytically
for any general `e` analyzing conserved quantities and the governing
differential equation. We are therefore forced to turn to other methods.

...

.. |date| date:: %D
.. |time| date:: %H:%M:%S

.. footer:: This document was generated on |date| at |time|.