.. default-role:: math

Developing a General Solution
*****************************

:Author: M. Werner

The orbital radius
==================
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