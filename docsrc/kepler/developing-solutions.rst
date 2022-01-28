.. default-role:: math

Developing a General Solution
*****************************

:Author: M. Werner

.. admonition:: Plan of Action

    Write down the **solution** to the 2-body problem in terms of `r` and
    `\theta` using the previously developed properties of the system.


We're finally ready to solve the 2-body problem! Well, kind of...
==================================================================

A full solution of the radius `r = r(\theta)` is achievable, but
we fall *just* short of knowing `\theta(t).` The grim reality of the problem
is that the angle `\theta` has to be calculated **numerically**.

The results are summarized below.

----

**The radius** `r` **is a known function of the angle** `\theta` **and is**
**parameterized by the system's characterization** (`\mu = \mathrm{const.}`) **and**
**initial conditions** (`h = \mathrm{const.}` and `A = \mathrm{const.}`).

.. math::
    :label: orbitalRadius

    r = \frac{h^2}{\mu + A\cos\theta}

- We know exactly what path the reduced mass must trace out


**The angle** `\theta`` **is NOT a known function of time.**
**It must be obtained numerically and depends on the system's**
**characterization and initial conditions as well as time.**

.. math::
    :label: orbitalAngle

    \tan\frac{\theta}{2} = \sqrt{\frac{\mu + A}{\mu - A}} \tan\frac{E}{2}
    \qquad \text{with} \qquad
    M = E - \frac{A}{\mu} \sin E

- We don't know *exactly* where the reduced mass is in its trajectory at any given time `t` (but we will be able to get "close enough").

----

Note two things:
    1. New symbols `M` and `E` have been introduced and will be explained later.
    2. `r` and `\theta` can be slightly more simplified, but we won't touch on this until the next page.

Deriving the radius
===================

from the LRL vector
-------------------
.. admonition:: Recall

    For any `\mathbf{x}, \mathbf{y}, \mathbf{z} \in \mathbb{R}^3`, the scalar triple product
    satisfies

    .. math::
        \mathbf{x} \cdot (\mathbf{y} \times \mathbf{z}) = \mathbf{y} \cdot (\mathbf{z} \times \mathbf{x}) = \mathbf{z} \cdot (\mathbf{x} \times \mathbf{y}).

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

In either approach, the radius `r` is obtained as a function of the angle `\theta` written as :eq:`orbitalRadius`. `\blacksquare`

from the radial dynamics
------------------------
The `\ddot{r}` equation of motion :eq:`polarEOM` combined with the conservation of angular momentum :eq:`AMconservation` is

.. math::
    \ddot{r} &= r\dot{\theta}^2 - \frac{\mu}{r^2} \\
    &= \frac{h^2}{r^3} - \frac{\mu}{r^2}.

We can convert the derivatives in time `t` to those in the angle
`\theta` to understand the geometry of the trajectory in
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

This equation still proves to be formidable in obtaining a solution. However, a final, clever change of variables *will*
yield a useful relation by letting `\eta = 1/r`. In this case,

.. math::
    \frac{d^2\eta}{d\theta^2} &= \frac{d}{d\theta}\left(\frac{d\eta}{d\theta}\right) \\
    &= \frac{d}{d\theta}\left(-\frac{1}{r^2}\frac{dr}{d\theta}\right) \\
    &= -\frac{1}{r^2}\frac{d^2r}{d\theta^2} + \frac{2}{r^3}\left(\frac{dr}{d\theta}\right)^{\!2} \\
    &= -\frac{1}{r^2}\left(\frac{2}{r}\left(\frac{dr}{d\theta}\right)^{\!2} - \frac{\mu r^2}{h^2} + r\right) + \frac{2}{r^3}\left(\frac{dr}{d\theta}\right)^{\!2} \\
    &= \frac{\mu}{h^2} - \eta.

**This is a linear oscillator with constant forcing**,
where both `\mu` and `h` are (positive) constants.
We can therefore immediately write the general solution as

.. math:: \eta = \frac{\mu}{h^2} + C \cos(\theta - \phi),

where both `C` and `\phi` are constants of integration.
Note that `C` represents an amplitude and, as such, satisfies
`C \geqslant 0`.
The orbital radius (`r = 1/\eta`) is then

.. math::
    r = \frac{h^2}{\mu + (C/h^2) \cos(\theta - \phi)}.

Since `\mathbf{A}` already provides a constant direction in the
orbital plane from which `\theta` is measured, we do not wish to
shift the angle `\theta` to be measured with respect to anything else
(yet). Thus, without loss of generality in *this* coordinate frame, we can set
`\phi = 0.`

To determine the constant `C`, we can calculate `\dot{r}` exactly and then
use the conservation of angular momentum :eq:`AMconservation` and the
LRL vector :eq:`LaplaceRungeLenz` to compare expressions.

.. math::
    \dot{r} &= \frac{C\sin\theta}{(\mu + (C/h^2) \cos\theta)^2}\dot{\theta} \\
    &= \left(\frac{r^2}{h^4}C\sin\theta\right)\left(\frac{h}{r^2}\right) \\
    &= \frac{C}{h^3}\sin\theta \\
    &= \frac{A}{h}\sin\theta

From this, we obtain that the integration constant `C` is given in terms of known quantities as `C = A h^2.`

The final form of `r` is :eq:`orbitalRadius`. `\blacksquare`

Trying to derive the angle
==========================
Knowing the orbital radius `r` to be a function of `\theta`,
we would most like to know the angle `\theta` as a
function of time `t`. This would fully complete the parameterization
as then `\mathbf{r} = \mathbf{r}(t)` would be a known function for all
time.

Like the orbital radius, the angle `\theta` is
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

from the angular dynamics
-------------------------
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