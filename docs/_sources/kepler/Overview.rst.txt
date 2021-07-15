Overview
========

.. admonition:: Plan of Action

    The equations of motion for the general 2-body problem are derived
    using a variety of methods. Finally, the full equations are placed
    into their "relative" and "standard" forms, providing a simpler and more
    direct expression for each body's position relative to one another.

Introduction
------------

The *Kepler* (2-body) problem is fundamental to the study of astrodynamics,
especially so for analyzing the more general 3-body problem. It consists of
determining the positions of 2 bodies under mutual Newtonian gravitational
attraction with respect to an inertial frame.

.. image:: ../../images/kepler_2_particles.svg
   :width: 422px
   :height: 255px
   :scale: 150 %
   :alt: Diagram of the 2-body problem with respect to an inertial frame
   :align: center

Here, we assume (without loss of generality) that :math:`m_1 \geqslant m_2`
are the body masses and a general position vector :math:`\mathbf{r}` is
represented

.. math::

    \mathbf{r} = \begin{pmatrix}x & y & z\end{pmatrix}^T

with basis elements provided by the inertial coordinate system.

Equations of Motion
-------------------

Newton's Laws
~~~~~~~~~~~~~
Applying Newton's 2\ :sup:`nd` law to each body under mutual Newtonian
gravitational attraction directly provides

.. math::
    :label: Newton

    \ddot{\mathbf{r}}_1 &= -\frac{G m_2}{|\mathbf{r}_1 - \mathbf{r}_2|^3}(\mathbf{r}_1 - \mathbf{r}_2) \\
    \ddot{\mathbf{r}}_2 &= -\frac{G m_1}{|\mathbf{r}_2 - \mathbf{r}_1|^3}(\mathbf{r}_2 - \mathbf{r}_1),

where :math:`G` is the gravitational constant.

Lagrangian Function
~~~~~~~~~~~~~~~~~~~

We can write the system's Lagrangian as simply the difference between
total kinetic energy and total potential energy.

.. math::
    :label: Lagrangian

    \mathcal{L} &= T - V \\
    &= \frac{1}{2}\left(m_1 |\dot{\mathbf{r}}_1|^2 + m_2|\dot{\mathbf{r}}_2|^2\right) + \frac{G m_1 m_2}{|\mathbf{r}_2 - \mathbf{r_1}|}

Since gravity is conservative and the system is unconstrained, the
corresponding Euler-Lagrange equations (6 of them) are written

.. math::
    \mathbf{0} &= \frac{d}{dt}\frac{\partial\mathcal{L}}{\partial\dot{\mathbf{r}}_i} - \frac{\partial\mathcal{L}}{\partial\mathbf{r}_i} && (i = 1,2) \\
    &= \frac{d}{dt} (m_i \dot{\mathbf{r}}_i) - \frac{G m_1 m_2}{|\mathbf{r}_j - \mathbf{r}_i|^3} (\mathbf{r}_j - \mathbf{r}_i) \qquad\quad && (j \neq i) \\
    &= m_i \ddot{\mathbf{r}}_i + \frac{G m_1 m_2}{|\mathbf{r}_i - \mathbf{r}_j|^3} (\mathbf{r}_i - \mathbf{r}_j).

Applying :math:`i = 1,2` produces the equations of motion for each of the
two bodies.

.. math::
    :label: Lagrange

    \ddot{\mathbf{r}}_1 &= -\frac{G m_2}{|\mathbf{r}_1 - \mathbf{r}_2|^3}(\mathbf{r}_1 - \mathbf{r}_2) \\
    \ddot{\mathbf{r}}_2 &= -\frac{G m_1}{|\mathbf{r}_2 - \mathbf{r}_1|^3}(\mathbf{r}_2 - \mathbf{r}_1),

Hamiltonian Function
~~~~~~~~~~~~~~~~~~~~

Using the Lagrangian :eq:`Lagrangian`, the Hamiltonian function is defined

.. math::
    \mathcal{H} &= \sum_{i = 1}^2 \dot{\mathbf{q}}_i \cdot \mathbf{p}_i - \mathcal{L} \\
    &= \sum_{i = 1}^2 \frac{\mathbf{p}_i}{m_i} \cdot \mathbf{p}_i - \left[\frac{1}{2}\left(\frac{|\mathbf{p}_1|^2}{m_1} + \frac{|\mathbf{p}_2|^2}{m_2}\right) + \frac{G m_1 m_2}{|\mathbf{q}_2 - \mathbf{q}_1|}\right] \\
    &= \frac{1}{2}\left(\frac{|\mathbf{p}_1|^2}{m_1} + \frac{|\mathbf{p}_2|^2}{m_2}\right) - \frac{G m_1 m_2}{|\mathbf{q}_2 - \mathbf{q}_1|},

where :math:`\mathbf{q}_i = \mathbf{r}_i` are the generalized coordinates
and :math:`\mathbf{p}_i = m_i\dot{\mathbf{r}}_i` are the generalized momenta
for each body (:math:`i = 1,2`).
Hamilton's canonical equations (12 of them) then require

.. math::
    :label: Hamilton

    \dot{\mathbf{q}}_i &= \frac{\mathbf{p}_i}{m_i} \\
    \dot{\mathbf{p}}_i &= -\frac{G m_1 m_2}{|\mathbf{q}_i - \mathbf{q}_j|^3} (\mathbf{q}_i - \mathbf{q}_j),

for :math:`j \neq i = 1,2`.

.. admonition:: Recall

    Hamilton's canonical equations are

    .. math::
        \dot{q} = +\frac{\partial\mathcal{H}}{\partial p} \qquad \text{and} \qquad \dot{p} = -\frac{\partial\mathcal{H}}{\partial q}

    for generalized coordinates and momenta :math:`q,p \in \mathbb{R}^n`,
    where :math:`n` is the number of degrees of freedom in the system.
    (Here, :math:`n = 6`.)

.. Note:: Hamilton's equations :eq:`Hamilton` are the first-order form of
    :eq:`Newton` and :eq:`Lagrange` as seen by

    .. math::
        \ddot{\mathbf{q}}_i = \frac{\dot{\mathbf{p}}_i}{m_i} = -\frac{G m_j}{|\mathbf{q}_i - \mathbf{q}_j|^3} (\mathbf{q}_i - \mathbf{q}_j),

    where :math:`\mathbf{q}_i \equiv \mathbf{r}_i`.

Relative Form
~~~~~~~~~~~~~

The Newtonian, Lagrangian, and Hamiltonian formalisms all provide the same
system of equations for the motion of two particles under mutual Newtonian
gravitational attraction. To reduce the complexity of the system (as we
will see), we can define the *relative* distance between each body as

.. math::
    \boxed{\mathbf{r} = \mathbf{r}_2 - \mathbf{r}_1}.

Doing this is beneficial because it exploits a symmetry in the full system,
halving the number of equations by creating a new coordinate system aligned
with the inertial coordinate system but whose origin is always located at
:math:`\mathbf{r}_1`.
That is, this definition provides **direct** information of **both** bodies
(relative to each other) rather than relying on the position of the
otherwise arbitrarily defined (inertial) coordinate system's origin.

The equations of motion for :math:`\mathbf{r}` may be calculated directly
since

.. math::
    \ddot{\mathbf{r}} &= \ddot{\mathbf{r}}_2 - \ddot{\mathbf{r}}_1 \\
    &= -\frac{G(m_1 + m_2)}{r^3}\mathbf{r},

where :math:`r = |\mathbf{r}|`.

.. Note:: The same result is achieved had we used Newton's 3\ :sup:`rd` law
    since

    .. math::
        \ddot{\mathbf{r}} &= \ddot{\mathbf{r}}_2 - \ddot{\mathbf{r}}_1 \\
        &= \ddot{\mathbf{r}}_2 + \frac{m_2}{m_1}\ddot{\mathbf{r}}_2 \\
        &= \left(1 + \frac{m_2}{m_1}\right) \ddot{\mathbf{r}}_2 \\
        &= \left(\frac{m_1 + m_2}{m_1}\right)\left(-\frac{G m_1}{r^3}\mathbf{r}\right) \\
        &= -\frac{G(m_1 + m_2)}{r^3}\mathbf{r}.

Standard Form
~~~~~~~~~~~~~

The standard form of the Kepler problem is achieved after defining the
*mass parameter*

.. math::
    \boxed{\mu = G(m_1 + m_2)}

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