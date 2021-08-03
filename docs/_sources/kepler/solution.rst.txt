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

Polar Coordinates
-----------------
With polar coordinates :math:`(r, \theta)` being used to describe position
within the orbit, it is *extremely* convenient to develop a new set of
differential equations in the polar basis. That is, exchange the inertial
basis for the noninertial polar basis

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
    :math:`\theta`.

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
    :math:`E`.
    Similarly, this relation provides another expression for
    :math:`\dot{\theta}` in addition to that from the conservation of
    angular momentum using the knowledge that :math:`\dot{\theta} > 0`
    for interesting motion.

The Orbital Radius
------------------
In this coordinate system with variables :math:`(x, y, z)`, the orbital
radius :math:`r` is obtainable using several different methods.

From the Laplace-Runge-Lenz Vector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

Thus, the orbital radius is expressed

.. math::
    r = \frac{h^2}{\mu + A \cos\theta} = \frac{h^2/\mu}{1 + (A/\mu) \cos\theta}.

From Differential Equations
~~~~~~~~~~~~~~~~~~~~~~~~~~~


