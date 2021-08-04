Solution
********
.. admonition:: Plan of Action

    The solution of the *general* 2-body problem is developed several
    different ways utilizing the now known special
    :ref:`properties<Properties>` admitted by the system.

Coordinate Rotation
===================
Knowing that the motion **must** be 2-dimensional, we can choose a more
convenient coordinate system via a coordinate rotation. Let this rotation
be denoted :math:`\mathbf{R} \in \mathrm{SO}(3)` such that

.. math::
    \begin{pmatrix}x \\ y \\ z\end{pmatrix} = \mathbf{R} \begin{pmatrix}X \\ Y \\ Z\end{pmatrix}.

These two quantities both represent the **same** object :math:`\mathbf{r}`.
This rotation is **not** time-dependent --- that is, :math:`\mathbf{R}` is
a static rotation between the two coordinate systems such that

.. math::
    \dot{\mathbf{R}} \equiv 0.

As such, the standard form of the equations of motion are *unchanged*.

Defining New Coordinates
------------------------
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

Cylindrical Coordinates
-----------------------
With polar coordinates :math:`(r, \theta)` being used to describe position
within the orbit, it is *extremely* convenient to develop a new set of
differential equations in the cylindrical basis. That is, exchange the
inertial basis for the noninertial cylindrical basis

.. math::
    \{\hat{\mathbf{e}}_x,\hat{\mathbf{e}}_y, \hat{\mathbf{e}}_z\} \longrightarrow \{\hat{\mathbf{e}}_r,\hat{\mathbf{e}}_\theta, \hat{\mathbf{e}}_z\}

and insert the resulting object describing relative positions of the two
bodies (:math:`\mathbf{r}`) into the standard form of the 2-body problem.

This transformation is useful as the expression for the position
simplifies dramatically to

.. math::
    \mathbf{r} = r\,\hat{\mathbf{e}}_r.

Differential Equations
~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Recall

    The time rates of change of a vector :math:`x \in \mathbb{R}^3` that's
    expressed in a coordinate system :math:`\mathcal{B}` rotating with
    angular velocity :math:`\Omega` relative to another coordinate system
    :math:`\mathcal{A}` follow

    .. math::
        \frac{dx^\mathcal{A}}{dt} = \frac{dx^\mathcal{B}}{dt} + \Omega \times x^\mathcal{B}

In calculating the **inertial** velocity and acceleration, the time
derivatives **must** be calculated relative to the inertial frame.
Here, the polar coordinate system is rotating with respect to the inertial
coordinate system at the rate :math:`\dot{\theta}` along the axis of
rotation :math:`\hat{\mathbf{e}}_z`. As such,

.. math::
    \dot{\mathbf{r}} &= \dot{r}\,\hat{\mathbf{e}}_r + r \dot{\theta}\,\hat{\mathbf{e}}_\theta \\
    \ddot{\mathbf{r}} &= (\ddot{r} - r\dot{\theta}^2)\hat{\mathbf{e}}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\hat{\mathbf{e}}_\theta.

.. important::
    Inserting the inertial acceleration into the standard form equations of
    motion provide a set of only two differential equations for the two
    unknowns :math:`r` and :math:`\theta`.

    .. math::
        \ddot{r} - r\dot{\theta}^2 &= -\frac{\mu}{r^2} \\
        r\ddot{\theta} + 2\dot{r}\dot{\theta} &= 0

Conserved Quantities
~~~~~~~~~~~~~~~~~~~~
The angular momentum :math:`\mathbf{h}`,
the Lorenz-Runge-Lenz vector :math:`\mathbf{A}`, and
the energy :math:`E` are expressed in the polar coordinates
:math:`(r, \theta)`, providing useful relations for analyzing the
relative trajectory of the two bodies.

Angular Momentum
^^^^^^^^^^^^^^^^
The angular momentum :math:`\mathbf{h}` expressed in polar coordinates is

.. math::
    \mathbf{h} &= \mathbf{r} \times \dot{\mathbf{r}} \\
    &= \left(r\,\hat{\mathbf{e}}_r\right) \times \left(\dot{r}\,\hat{\mathbf{e}}_r + r \dot{\theta}\,\hat{\mathbf{e}}_\theta\right) \\
    &= r\dot{r} (\hat{\mathbf{e}}_r \times \hat{\mathbf{e}}_r) + r^2\dot{\theta} (\hat{\mathbf{e}}_r \times \hat{\mathbf{e}}_\theta) \\
    &= r^2\dot{\theta}\,\hat{\mathbf{e}}_z.

.. important::
    The conservation of angular momentum provides

    .. math::
        r^2\dot{\theta} = h,

    where :math:`h = |\mathbf{h}|` is a constant of motion.

    Since :math:`h \geqslant 0` and :math:`r^2 > 0`, we know that
    :math:`\dot{\theta} \geqslant 0` **always**. Note that if
    :math:`\dot{\theta} \equiv 0`, then :math:`\ddot{r} < 0`, which means
    :math:`r \to 0` in *finite* time --- a finite-time singularity.
    Interesting motion therefore takes place for :math:`\dot{\theta} > 0`.

The Laplace-Runge-Lenz Vector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Lorenz-Runge-Lenz vector :math:`\mathbf{A}` expressed in polar
coordinates is

.. math::
    \mathbf{A} &= \dot{\mathbf{r}} \times \mathbf{h} - \frac{\mu}{r}\mathbf{r} \\
    &= (\dot{r}\,\hat{\mathbf{e}}_r + r\dot{\theta}\,\hat{\mathbf{e}}_\theta) \times (r^2\dot{\theta}\,\hat{\mathbf{e}}_z) - \frac{\mu}{r} (r \,\hat{\mathbf{e}}_r) \\
    &= r^2\dot{r}\dot{\theta}(\hat{\mathbf{e}}_r \times \hat{\mathbf{e}}_z) + r^3\dot{\theta}^2(\hat{\mathbf{e}}_\theta \times \hat{\mathbf{e}}_z) - \mu\,\hat{\mathbf{e}}_r \\
    &= r^2\dot{r}\dot{\theta}(-\hat{\mathbf{e}}_\theta) + r^3\dot{\theta}^2(\hat{\mathbf{e}}_r) - \mu\,\hat{\mathbf{e}}_r \\
    &= (r^3\dot{\theta}^2 - \mu)\hat{\mathbf{e}}_r - r^2\dot{r}\dot{\theta}\,\hat{\mathbf{e}}_\theta \\
    &= A\,\hat{\mathbf{e}}_x \\
    &= A (\cos\theta\,\hat{\mathbf{e}}_r - \sin\theta\,\hat{\mathbf{e}}_\theta).

.. important::
    The Lorenz-Runge-Lenz vector provides

    .. math::
        r^3\dot{\theta}^2 - \mu &= A\cos\theta \\
        r^2\dot{r}\dot{\theta} &= A\sin\theta,

    where :math:`A = |\mathbf{A}|` is a constant of motion.

    Paired with the conservation of angular momentum, these two
    expressions provide *very* direct expressions of :math:`r` and
    :math:`\dot{r}`.

Energy
^^^^^^
The energy :math:`E` expressed in polar coordinates is

.. math::
    E &= \frac{v^2}{2} - \frac{\mu}{r} \\
    &= \frac{\dot{\mathbf{r}} \cdot \dot{\mathbf{r}}}{2} - \frac{\mu}{r} \\
    &= \frac{1}{2}(\dot{r}^2 + r^2\dot{\theta}^2) - \frac{\mu}{r}.

.. important::
    The conservation of energy provides

    .. math::
        E = \frac{1}{2}(\dot{r}^2 + r^2\dot{\theta}^2) - \frac{\mu}{r},

    where :math:`E` is a constant of motion.

    Paired with angular momentum, this expression "integrates" the
    :math:`\ddot{r}` equation of motion with integration constant
    :math:`2E`.
    Similarly, this relation provides another expression for
    :math:`\dot{\theta}` in addition to that from the conservation of
    angular momentum using the knowledge that :math:`\dot{\theta} > 0`
    for interesting motion.

The Orbital Radius
==================
In this coordinate system with variables :math:`(x, y, z)`, the orbital
radius :math:`r` is obtainable using several different methods.

From the Laplace-Runge-Lenz Vector
----------------------------------
.. admonition:: Recall

    #.  For any :math:`x,y \in \mathbb{R}^3`, the scalar product satisfies

        .. math::
            x \cdot y = |x| |y| \cos\theta,

        where :math:`\theta` is the angle between :math:`x` and :math:`y`.

    #.  For any :math:`x, y, z \in \mathbb{R}^3`, the scalar triple product
        satisfies

        .. math::
            x \cdot (y \times z) = y \cdot (z \times x) = z \cdot (x \times y).

The Laplace-Runge-Lenz vector can be used to obtain an expression for the
orbital radius :math:`r` as a function of the polar coordinate
:math:`\theta` *very* directly.

Since :math:`\theta` is measured from the :math:`x` axis, which is aligned
with the Laplace-Runge-Lenz vector, then one can see that

.. math::
    \mathbf{A} \cdot \mathbf{r} &= \left(\dot{\mathbf{r}} \times \mathbf{h} - \frac{\mu}{r}\mathbf{r}\right) \cdot \mathbf{r} \\
    &= (\dot{\mathbf{r}} \times \mathbf{h}) \cdot \mathbf{r} - \left(\frac{\mu}{r}\mathbf{r}\right) \cdot \mathbf{r} \\
    &= \mathbf{r} \cdot (\dot{\mathbf{r}} \times \mathbf{h}) - \frac{\mu}{r} (\mathbf{r} \cdot \mathbf{r}) \\
    &= \mathbf{h} \cdot (\mathbf{r} \times \dot{\mathbf{r}}) - \mu r \\
    &= \mathbf{h} \cdot \mathbf{h} - \mu r \\
    &= h^2 - \mu r \\
    &= A r \cos\theta.

.. important::
    The orbital radius :math:`r` found directly from manipulating the
    expression of the Laplace-Runge-Lenz vector expressed in polar
    coordinates is

    .. math::
        r = \frac{h^2}{\mu + A\cos\theta}.

From Conserved Quantities
-------------------------
Knowing from the conservation of angular momentum that
:math:`r^2\dot{\theta} = h`, the :math:`\hat{\mathbf{e}}_r` component of
the Laplace-Runge-Lenz vector allows one to algebraically solve for the
radius. That is,

.. math::
    0 &= r^3\dot{\theta}^2 - \mu - A\cos\theta \\
    &= \frac{h^2}{r} - \mu - A\cos\theta.

.. important::
    The orbital radius :math:`r` found from analyzing a conserved component
    of the Laplace-Runge-Lenz vector expressed in polar coordinates,
    combined with the conservation of angular momentum in polar
    coordinates, is

    .. math::
        r = \frac{h^2}{\mu + A\cos\theta}.

From Differential Equations
---------------------------
Using the conservation of angular momentum, the :math:`\ddot{r}` equation
of motion provides

.. math::
    \ddot{r} &= r\dot{\theta}^2 - \frac{\mu}{r^2} \\
    &= \frac{h^2}{r^3} - \frac{\mu}{r^2}.

We wish to convert the derivatives in time :math:`t` to those in the angular
coordinate :math:`\theta` to understand the geometry of the trajectory in
polar coordinates. Using the conservation of angular momentum again, we see

.. math::
    \frac{d^2 r}{d\theta^2} &= \frac{d}{d\theta}\left(\frac{dr}{d\theta}\right) \\
    &= \frac{d}{d\theta}\left(\frac{\dot{r}}{\dot{\theta}}\right) \\
    &= \frac{d}{d\theta}\left(\frac{r^2\dot{r}}{h}\right) \\
    &= \frac{1}{\dot{\theta}}\frac{d}{dt}\left(\frac{r^2\dot{r}}{h}\right) \\
    &= \frac{r^2}{h^2}(2r\dot{r}^2 + r^2 \ddot{r}) \\
    &= \frac{r^2}{h^2}\left(2r\left[\frac{h}{r^2}\frac{dr}{d\theta}\right]^2 + r^2 \left[\frac{h^2}{r^3} - \frac{\mu}{r^2}\right]\right) \\
    &= \frac{r^2}{h^2}\left(2\frac{h^2}{r^3}\left[\frac{dr}{d\theta}\right]^2 - \mu + \frac{h^2}{r}\right) \\
    &= \frac{2}{r}\left[\frac{dr}{d\theta}\right]^2 - \frac{\mu r^2}{h^2} + r.

Despite offering a description of the trajectory's geometry in space as
opposed to time, *this* differential equation still proves to be formidable
in obtaining a solution. However, a final, clever change of variables *will*
yield a useful relation. Let :math:`\eta = 1/r`. Then

.. math::
    \frac{d^2\eta}{d\theta^2} &= \frac{d}{d\theta}\left(\frac{d\eta}{d\theta}\right) \\
    &= \frac{d}{d\theta}\left(-\frac{1}{r^2}\frac{dr}{d\theta}\right) \\
    &= \frac{d}{d\theta}\left(-\frac{1}{r^2}\left[\frac{r^2\dot{r}}{h}\right]\right) \\
    &= -\frac{1}{h}\frac{d\dot{r}}{d\theta} \\
    &= -\frac{1}{h}\frac{d}{d\theta}\left(\frac{dr}{d\theta}\dot{\theta}\right) \\
    &= -\frac{1}{h}\frac{d}{d\theta}\left(\frac{dr}{d\theta}\frac{h}{r^2}\right) \\
    &= -\frac{1}{r^2}\frac{d^2r}{d\theta^2} + \frac{2}{r^2}\left[\frac{dr}{d\theta}\right]^2 \\
    &= -\frac{1}{r^2}\left[\frac{2}{r}\left[\frac{dr}{d\theta}\right]^2 - \frac{\mu r^2}{h^2} + r\right] + \frac{2}{r^3}\left[\frac{dr}{d\theta}\right]^2 \\
    &= \frac{\mu}{h^2} - \frac{1}{r} \\
    &= \frac{\mu}{h^2} - \eta.

With this transformation, we see that we are offered an equation describing
a linear oscillator as

.. math::
    \frac{d^2\eta}{d\theta^2} + \eta = \frac{\mu}{h^2},

where both :math:`\mu` and :math:`h` are constants. We can therefore
immediately write the general solution as

.. math:: \eta = \frac{\mu}{h^2} + C \cos(\theta - \omega),

where both :math:`C` and :math:`\omega` are new constants of integration.
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

Note that derivatives of :math:`r` may now be evaluated exactly.

.. math::
    \dot{r} &= \frac{C\sin\theta}{(\mu + (C/h^2) \cos\theta)^2}\dot{\theta} \\
    &= \left(\frac{r^2}{h^4}C\sin\theta\right)\left(\frac{h}{r^2}\right) \\
    &= \frac{C}{h^3}\sin\theta.

To determine the constant :math:`C`, we can turn to the conservation of
energy.

.. math::
    E &= \frac{1}{2}(\dot{r}^2 + r^2\dot{\theta}^2) - \frac{\mu}{r} \\
    &= \frac{1}{2}\left(\left[\frac{C}{h^3}\sin\theta\right]^2 + \frac{h^2}{r^2}\right) - \frac{\mu}{r} \\
    &= \frac{1}{2}\left(\frac{C^2}{h^6}\sin^2\theta + \left[\frac{(C\cos\theta + \mu h^2)^2}{h^6}\right]\right) - \frac{\mu}{r} \\
    &= \frac{1}{2}\left(\frac{C^2}{h^6}\sin^2\theta + \frac{C^2\cos^2\theta + 2\mu h^2 C\cos\theta + \mu^2 h^4}{h^6}\right) - \frac{\mu}{r} \\
    &= \frac{1}{2}\left(\frac{C^2}{h^6}(\sin^2\theta + \cos^2\theta) + \frac{2\mu C\cos\theta}{h^4} + \frac{\mu^2}{h^2}\right) - \frac{\mu}{r} \\
    &= \frac{1}{2}\left(\frac{C^2}{h^6} + \frac{\mu^2}{h^2}\right) + \frac{\mu C \cos\theta}{h^4} - \frac{\mu}{r} \\
    &= \frac{1}{2}\left(\frac{C^2}{h^6} + \frac{\mu^2}{h^2}\right) + \frac{\mu C \cos\theta}{h^4} - \mu\left[\frac{\mu + (C/h^2)\cos\theta}{h^2}\right] \\
    &= \frac{1}{2}\left(\frac{C^2}{h^6} + \frac{\mu^2}{h^2}\right) + \frac{\mu C \cos\theta}{h^4} - \frac{\mu^2}{h^2} - \frac{\mu C\cos\theta}{h^4} \\
    &= \frac{1}{2}\left(\frac{C^2}{h^6} - \frac{\mu^2}{h^2}\right).

Thus, we see that the integration constant is related to the energy
according to

.. math::
    C = \mu h^2 \sqrt{1 + \frac{2Eh^2}{\mu^2}}.

We choose the positive branch (as opposed to the negative branch) of the
square root since :math:`C` represents an amplitude --- an explicitly
nonnegative quantity. For brevity, we write :math:`C = \mu h^2 e`, where

.. math::
    e = \sqrt{1 + \frac{2Eh^2}{\mu^2}}.

.. important::
    The orbital radius :math:`r` found directly from solving the governing
    differential equation, utilizing the conservation of angular momentum
    and energy, and evaluating the two constants of integration yields

    .. math::
        r = \frac{h^2/\mu}{1 + e\cos\theta},

    where :math:`e = C/\mu h^2` is dependent upon the energy :math:`E` of
    the relative motion of the two bodies.