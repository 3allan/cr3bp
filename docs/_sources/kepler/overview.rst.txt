.. default-role:: math

========
Overview
========

:Author: M. Werner

.. admonition:: Plan of Action

    The equations of motion for the general 2-body problem are derived
    using the Newtonian, Lagrangian, and Hamiltonian approaches, showing
    that each method provides the same system using different methods.

Introduction
============

The *Kepler* (2-body) problem is fundamental to the study of astrodynamics,
especially so for analyzing the more general 3-body problem. It consists of
determining the positions of 2 bodies under mutual Newtonian gravitational
attraction with respect to an inertial frame.

.. figure:: ../../images/kepler_2_particles.svg
    :width: 355px
    :height: 209px
    :scale: 150 %
    :alt: Diagram of the 2-body problem with respect to a general, inertial coordinate system
    :align: center

    The most general setup of the Kepler (2-body) problem. The problem
    consists of two masses, :math:`m_1` and :math:`m_2`, gravitationally
    attracted to one another whose positions, :math:`\mathbf{r}_1` and
    :math:`\mathbf{r}_2`, are tracked in an inertial coordinate system.

Here, :math:`m_1` and :math:`m_2` are the body masses and a general position
vector :math:`\mathbf{r}` is represented

.. math::

    \mathbf{r} = \begin{pmatrix}X & Y & Z\end{pmatrix}^T

with basis elements provided by the inertial coordinate system.

Equations of Motion
===================

Newton's Laws
-------------
Applying Newton's 2\ :sup:`nd` law to each body under mutual Newtonian
gravitational attraction directly provides

.. math::
    :label: Newton

    \ddot{\mathbf{r}}_1 &= -\frac{G m_2}{|\mathbf{r}_1 - \mathbf{r}_2|^3}(\mathbf{r}_1 - \mathbf{r}_2) \\
    \ddot{\mathbf{r}}_2 &= -\frac{G m_1}{|\mathbf{r}_2 - \mathbf{r}_1|^3}(\mathbf{r}_2 - \mathbf{r}_1),

where :math:`G` is the gravitational constant.

Lagrangian Function
-------------------

.. admonition:: Recall

    Lagrange's (conservative) equations are

    .. math::
        \frac{d}{dt}\frac{\partial\mathcal{L}}{\partial \dot{q}} - \frac{\partial\mathcal{L}}{\partial q} = 0,

    for generalized coordinates :math:`q \in \mathbb{R}^n`, where :math:`n`
    is the number of degrees of freedom in the system. (Here,
    :math:`n = 6`.)

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

Writing the the above result of Lagrange's in their most compact form
provides

.. math::
    \ddot{\mathbf{r}}_i = -\frac{G m_j}{|\mathbf{r}_i - \mathbf{r}_j|^3}(\mathbf{r}_i - \mathbf{r}_j).

Applying :math:`i = 1,2` produces the equations of motion for each of the
two bodies.

.. math::
    :label: Lagrange

    \ddot{\mathbf{r}}_1 &= -\frac{G m_2}{|\mathbf{r}_1 - \mathbf{r}_2|^3}(\mathbf{r}_1 - \mathbf{r}_2) \\
    \ddot{\mathbf{r}}_2 &= -\frac{G m_1}{|\mathbf{r}_2 - \mathbf{r}_1|^3}(\mathbf{r}_2 - \mathbf{r}_1),

Hamiltonian Function
--------------------

.. admonition:: Recall

    Hamilton's canonical equations are

    .. math::
        \dot{q} = +\frac{\partial\mathcal{H}}{\partial p} \qquad \text{and} \qquad \dot{p} = -\frac{\partial\mathcal{H}}{\partial q}

    for generalized coordinates and momenta :math:`q,p \in \mathbb{R}^n`,
    where :math:`n` is the number of degrees of freedom in the system.
    (Here, :math:`n = 6`.)

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

.. Note:: Hamilton's equations :eq:`Hamilton` are the first-order form of
    :eq:`Newton` and :eq:`Lagrange` as seen by

    .. math::
        \ddot{\mathbf{q}}_i = \frac{\dot{\mathbf{p}}_i}{m_i} = -\frac{G m_j}{|\mathbf{q}_i - \mathbf{q}_j|^3} (\mathbf{q}_i - \mathbf{q}_j),

    where :math:`\mathbf{q}_i \equiv \mathbf{r}_i`.
