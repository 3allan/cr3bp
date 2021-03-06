Properties
==========
.. admonition:: Plan of Action

    The general 2-body problem may be simplified greatly by utilizing
    several special properties admitted by the system. These properties
    *will* enable a full solution of the general problem to be determined
    analytically.

.. admonition:: Recall

    The equations of motion of the general 2-body problem determined by the
    Newtonian, Lagrangian, and Hamiltonian formalisms are

    .. math::
        :label: general2bp

        \ddot{\mathbf{r}}_1 &= -\frac{G m_2}{|\mathbf{r}_1 - \mathbf{r}_2|^3}(\mathbf{r}_1 - \mathbf{r}_2) \\
        \ddot{\mathbf{r}}_2 &= -\frac{G m_1}{|\mathbf{r}_2 - \mathbf{r}_1|^3}(\mathbf{r}_2 - \mathbf{r}_1).

Amazingly, this system :eq:`general2bp` has a closed-form solution. Obtaining this solution,
however, is made significantly easier once several properties are known.

Relative Form
-------------
The Newtonian, Lagrangian, and Hamiltonian formalisms all provide the same
system of equations for the motion of two particles under mutual Newtonian
gravitational attraction with respect to the origin of the inertial
coordinate system given by :eq:`general2bp`. To reduce the complexity of
this system (as we will see), we can define the *relative* distance between
each body as

.. math::
    :label: relative

    \mathbf{r} = \mathbf{r}_2 - \mathbf{r}_1.

The equations of motion may be calculated directly since

.. math::
    :label: relativeEOM

    \ddot{\mathbf{r}} &= \ddot{\mathbf{r}}_2 - \ddot{\mathbf{r}}_1 \\
    &= -\frac{G(m_1 + m_2)}{r^3}\mathbf{r},

where :math:`r = |\mathbf{r}|`.

.. Note:: The same result is achieved had we used Newton's 3\ :sup:`rd` law
    since :math:`m_1 \ddot{\mathbf{r}}_1 = -m_2\ddot{\mathbf{r}}_2`, i.e.

    .. math::
        \ddot{\mathbf{r}} &= \ddot{\mathbf{r}}_2 - \ddot{\mathbf{r}}_1 \\
        &= \ddot{\mathbf{r}}_2 + \frac{m_2}{m_1}\ddot{\mathbf{r}}_2 \\
        &= \left(1 + \frac{m_2}{m_1}\right) \ddot{\mathbf{r}}_2 \\
        &= \left(\frac{m_1 + m_2}{m_1}\right)\left(-\frac{G m_1}{r^3}\mathbf{r}\right) \\
        &= -\frac{G(m_1 + m_2)}{r^3}\mathbf{r}.

.. Important:: Doing this is beneficial because it exploits a symmetry in
    the full system of equations, essentially **halving** the number of
    equations to be solved in order to obtain *any* information about
    *either* body.

Conserved Quantities
--------------------
Energy
~~~~~~
.. admonition:: Recall

    For :math:`q,p \in \mathbb{R}^n`, a canonical Hamiltonian system
    satisfies :math:`\dot{q} = \mathcal{H}_p` and
    :math:`\dot{p} = -\mathcal{H}_q` for which, along a trajectory,

    .. math::
        \frac{d\mathcal{H}}{dt} = \frac{\partial\mathcal{H}}{\partial t}.

The Hamiltonian is explicitly independent of time :math:`t`. That is,

.. math::
    \mathcal{H} \equiv \mathrm{const.}

along trajectories of the system.

.. Important::
    The Hamiltonian itself is conserved under the dynamics of the 2-body
    problem.

Linear Momentum
~~~~~~~~~~~~~~~
.. admonition:: Recall

    For any :math:`x_1, x_2 \in \mathbb{R}^3`, the center of mass for a
    system of two particles with respect to an inertial coordinate system is

    .. math::
        x_{cm} \equiv \frac{m_1 x_1 + m_2 x_2}{m_1 + m_2},

    where :math:`m_1` and :math:`m_2` are the masses of each body located
    (instantaneously) at :math:`x_1` and :math:`x_2`, respectively.


The two bodies are *isolated* -- that is, the center of mass satisfies

.. math:: \mathbf{r}_{cm} = \dot{\mathbf{r}}_{cm}(0) t + \mathbf{r}_{cm}(0)

since there is no external forcing to the system.
As such, the center of mass moves in a straight line (or not at all) in
accordance with Newton's 1\ :sup:`st` law. Further, we have *explicitly*
that

.. math::
    :label: positionsFromCenterOfMass

    \mathbf{r}_1 = \mathbf{r}_{cm} - \frac{m_2}{m_1 + m_2}\mathbf{r} \qquad \text{and} \qquad \mathbf{r}_2 = \mathbf{r}_{cm} + \frac{m_1}{m_1 + m_2}\mathbf{r}.

.. Important::
    :eq:`relative` provides **direct**
    information of both bodies (relative to each other) through
    :eq:`relativeEOM` *and* enables the inertial positions of both bodies to
    be *calculated* from :eq:`positionsFromCenterOfMass` rather than directly
    solved from :eq:`general2bp`.

    This solidifies the idea that only half of the amount of equations
    have to be solved with :eq:`relativeEOM`, but now *all* information about
    *both* bodies is known.

Angular Momentum
~~~~~~~~~~~~~~~~
.. admonition:: Recall

    #. For any :math:`x \in \mathbb{R}^3`, the cross-product of :math:`x`
       with itself vanishes (i.e., :math:`x \times x \equiv 0`).

    #. For any :math:`x,y \in \mathbb{R}^3`, the cross-product is
       anticommutative (i.e. :math:`x \times y + y \times x \equiv 0`).

Rewriting the Kepler problem in a convenient form,

.. math::
    \ddot{\mathbf{r}} + \frac{G(m_1 + m_2)}{r^3}\mathbf{r} = \mathbf{0},

lets us immediately show

.. math::
    \mathbf{0} &= \left(\ddot{\mathbf{r}} + \frac{G(m_1 + m_2)}{r^3}\mathbf{r}\right) \!\times \mathbf{r} \\
    &= \ddot{\mathbf{r}} \times \mathbf{r} + \left(\frac{G(m_1 + m_2)}{r^3}\mathbf{r}\right) \!\times \mathbf{r} \\
    &= \ddot{\mathbf{r}} \times \mathbf{r} + \frac{G(m_1 + m_2)}{r^3}\left(\mathbf{r} \times \mathbf{r}\right) \\
    &= \ddot{\mathbf{r}} \times \mathbf{r} \\
    &= \ddot{\mathbf{r}} \times \mathbf{r} + \dot{\mathbf{r}} \times \dot{\mathbf{r}} \\
    &= \frac{d}{dt}\underbrace{(\dot{\mathbf{r}} \times \mathbf{r})}_{-\mathbf{h}}.

Consequently, we conclude that the (specific) angular momentum
:math:`\mathbf{h}` is conserved under the dynamics of the 2-body problem.

.. math::
    \mathbf{h} = \mathbf{r} \times \dot{\mathbf{r}} \equiv \mathrm{const.}

.. Important::
    The motion of the two bodies **must** be **planar**.

The Laplace-Runge-Lenz Vector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Recall

    For any :math:`x,y,z \in \mathbb{R}^3`, the vector triple product
    satisfies

    .. math::
        x \times (y \times z) = (x \cdot z) y - (x \cdot y) z.

Knowing that the angular momentum :math:`h` is conserved, consider the
following.

.. math::
    \frac{d}{dt}(\dot{\mathbf{r}} \times  \mathbf{h}) &= \ddot{\mathbf{r}} \times \mathbf{h} \\
    &= \left(-\frac{G(m_1 + m_2)}{r^3} \mathbf{r}\right) \times (\mathbf{r} \times \dot{\mathbf{r}}) \\
    &= -\frac{G(m_1 + m_2)}{r^3} \big(\mathbf{r} \times (\mathbf{r} \times \dot{\mathbf{r}})\big) \\
    &= -\frac{G(m_1 + m_2)}{r^3} \big((\mathbf{r} \cdot \dot{\mathbf{r}})\mathbf{r} - (\mathbf{r} \cdot \mathbf{r})\dot{\mathbf{r}}\big) \\
    &= -\frac{G(m_1 + m_2)}{r^3} \big(r\dot{r} \mathbf{r} - r^2 \dot{\mathbf{r}}\big) && \quad \left(\mathbf{r} \cdot \dot{\mathbf{r}} = \frac{1}{2}\frac{d}{dt}(\mathbf{r} \cdot \mathbf{r})\right)\\
    &= -G(m_1 + m_2) \left(\frac{\dot{r}}{r^2} \mathbf{r} - \frac{1}{r}\dot{\mathbf{r}}\right) \\
    &= G(m_1 + m_2) \left(\frac{r \dot{\mathbf{r}} - \dot{r} \mathbf{r}}{r^2}\right) \\
    &= G(m_1 + m_2) \frac{d}{dt}\left(\frac{\mathbf{r}}{r}\right) \\
    &= \frac{d}{dt}\left(\frac{G(m_1 + m_2)}{r}\mathbf{r}\right).

Finally, exploiting linearity of the differential operator provides the
conserved quantity, :math:`\mathbf{A}`, referred to as the
Laplace-Runge-Lenz vector.

.. math::
    \mathbf{A} = \dot{\mathbf{r}} \times \mathbf{h} - \frac{G(m_1 + m_2)}{r}\mathbf{r} \equiv \mathrm{const.}

.. Important::
    The Laplace-Runge-Lenz vector provides a **constant direction** *in the plane of motion of the two bodies.*

The Reduced Mass
----------------
The system :eq:`relativeEOM` is writable as

.. math::
    \underbrace{\frac{m_1 m_2}{m_1 + m_2}}_{\mu^*}\ddot{\mathbf{r}} = \underbrace{-\frac{G m_1 m_2}{r^3}\mathbf{r}}_{-\nabla V(r)},

which is in the form of Newton's 2\ :sup:`nd` law for a **single** particle
of mass :math:`\mu^*` being tracked in an inertial coordinate system with
position :math:`\mathbf{r}` under the influence of a potential :math:`V`.
More clearly, we can write

.. math::
    \mu^* \ddot{\mathbf{r}} = -\frac{G(m_1 + m_2)\mu^*}{r^3}\mathbf{r}

The 2-body system :eq:`relativeEOM` *can* therefore be treated like it
describes a **single** particle\ :sup:`[`\ [1]_:sup:`]`.
(The quantity :math:`\mu^*` that makes this purely mathematical
simplification possible is called the *reduced mass*.)

.. image:: ../../images/reduced_mass_system.svg
   :width: 422px
   :height: 255px
   :scale: 150 %
   :alt: Example of a trajectory taken by the reduced mass in a general system
   :align: center

.. admonition:: Fact

    For any :math:`m_1, m_2 > 0`,

    .. math::
        \mu^* < m_1 + m_2.

    *Proof:* Suppose the opposite. Then
    :math:`(m_1 + m_2)^2 = m_1^2 + 2m_1 m_2 + m_2^2 < m_1 m_2`, but this
    means :math:`m_1^2 + m_2^2 < -m_1 m_2` --- a contradiction.
    :math:`\blacksquare`

.. Important:: The resulting trajectory of a **single** body of mass
    :math:`\mu^*` under the influence of the potential from a *static* body
    of mass :math:`m_1 + m_2` is the **same** trajectory experienced by the
    **relative motion** of two bodies under mutual Newtonian gravitational
    attraction. This trajectory for both cases is :math:`\mathbf{r}`.

Standard Form
-------------
The standard form of the Kepler problem is achieved after defining the
*gravitational parameter*

.. math::
    \mu = G(m_1 + m_2)

such that the equations of motion for the relative motion of one body about
the other are

.. math::
    \ddot{\mathbf{r}} = -\frac{\mu}{r^3}\mathbf{r}

.. Important:: In astrophysical applications, :math:`\mu` can be viewed as
    a quantity of two (generally) unknown parameters :math:`m_1` and
    :math:`m_2` whose values are to be determined.

.. Important:: In some dynamical astronomy and nearly all engineering
    applications, :math:`\mu` can be easily regarded as being identified
    exactly with

    .. math::
        \mu = GM,

    where :math:`M = m_1` is the mass of a central body much more massive
    than the other, i.e. :math:`m_1 \ggg m_2`. (This is the case where
    :math:`m_2` represents spacecraft, comets, etc.)

    The effective statement of taking :math:`\mu` this way is that the
    central body of mass :math:`m_1` moves in a *straight line* (or not at
    all) relative to the inertial frame (all in accordance with Newton's
    1\ :sup:`st` law), but the motion of the smaller body of mass
    :math:`m_2` *is still affected by the presence of the central body*.
    (This scenario **is** that of the reduced mass, where
    :math:`\mu^* \approx m_2` is the mass of the particle in motion and
    :math:`m_1 + m_2 \approx M` is the central body's mass.)

.. Warning:: Do **not** confuse the 2-body gravitational parameter
    :math:`\mu` with the 3-body mass parameter :math:`\mu`.

    .. centered::
        **These quantities, though sharing the same symbol, are different**.

Sources
-------
.. [1] `The Two-Body Problem - UCSB Physics <http://web.physics.ucsb.edu/~fratus/phys103/LN/TBP.pdf>`_

.. [2] Goldstein, Poole, Safko. Classical Mechanics, 3rd Edition. Pgs. 102-103