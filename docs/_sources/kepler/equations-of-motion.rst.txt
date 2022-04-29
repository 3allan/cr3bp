.. default-role:: math

The Two-Body World
******************

:Author: M. Werner

.. admonition:: Plan of Action

    The equations of motion for the general 2-body problem are derived
    using the Newtonian, Lagrangian, and Hamiltonian approaches, showing
    that each method provides the same system using different methods.

The simplest scenario
=====================

The **Kepler** (also called the **2-body**) **problem** is fundamental to the study of astrodynamics,
especially so for analyzing the more general 3-body problem. It consists of
determining the positions of 2 bodies under mutual Newtonian gravitational
attraction.

.. figure:: ../../images/kepler_2_particles_v2.svg
    :width: 355px
    :height: 209px
    :scale: 150 %
    :alt: Diagram of the 2-body problem with respect to a general, inertial coordinate system
    :align: center

    The most general setup of the Kepler (2-body) problem. The problem
    consists of two masses, `m_1` and `m_2`, gravitationally
    attracted to one another whose positions, `\mathbf{r}_1` and
    `\mathbf{r}_2`, are tracked in an inertial coordinate system.

Here, `m_1` and `m_2` are the body masses and a general position
vector `\mathbf{r}` is represented

.. math::

    \mathbf{r} = \begin{pmatrix}X \\ Y \\ Z\end{pmatrix}

with basis elements provided by the inertial coordinate system.

Equations of motion
===================

using Newton's laws
-------------------
Applying Newton's laws to each body under mutual Newtonian
gravitational attraction directly provides the equations of motion (6 of them)

.. math::
    :label: Newton

    \ddot{\mathbf{r}}_1 &= -\frac{G m_2}{|\mathbf{r}_1 - \mathbf{r}_2|^3}(\mathbf{r}_1 - \mathbf{r}_2) \\
    \ddot{\mathbf{r}}_2 &= -\frac{G m_1}{|\mathbf{r}_2 - \mathbf{r}_1|^3}(\mathbf{r}_2 - \mathbf{r}_1).

using the Lagrangian
--------------------

.. admonition:: Recall

    Lagrange's (conservative) equations are

    .. math::
        \frac{d}{dt}\frac{\partial L}{\partial \dot{\mathbf{q}}} - \frac{\partial L}{\partial \mathbf{q}} = 0,

    for generalized coordinates `\mathbf{q} \in \mathbb{R}^n`, where `L \in \mathbb{R}` is the Lagrangian
    and `n` is the number of degrees of freedom in the system.

We can write the system's Lagrangian as simply the difference between
total kinetic energy and total potential energy.

.. math::
    :label: Lagrangian

    L = \underbrace{    \vphantom{\frac{G m_1 m_2}{|\mathbf{r}_2 - \mathbf{r_1}|}}    \frac{1}{2}\left(m_1 |\dot{\mathbf{r}}_1|^2 + m_2|\dot{\mathbf{r}}_2|^2\right)}_{\text{kinetic}} + \underbrace{\frac{G m_1 m_2}{|\mathbf{r}_2 - \mathbf{r_1}|}}_{-\text{potential}}

Since gravity is conservative and the system is unconstrained, the
corresponding Euler-Lagrange equations (6 of them) are written

.. math::
    \mathbf{0} &= \frac{d}{dt}\frac{\partial L}{\partial\dot{\mathbf{r}}_i} - \frac{\partial L}{\partial\mathbf{r}_i} && (i = 1,2) \\
    &= \frac{d}{dt} (m_i \dot{\mathbf{r}}_i) - \frac{G m_1 m_2}{|\mathbf{r}_j - \mathbf{r}_i|^3} (\mathbf{r}_j - \mathbf{r}_i) \qquad\quad && (j \neq i) \\
    &= m_i \ddot{\mathbf{r}}_i + \frac{G m_1 m_2}{|\mathbf{r}_i - \mathbf{r}_j|^3} (\mathbf{r}_i - \mathbf{r}_j).

Writing the above result of Lagrange's equations in their most compact form
provides

.. math::
    :label: Lagrange

    \ddot{\mathbf{r}}_i = -\frac{G m_j}{|\mathbf{r}_i - \mathbf{r}_j|^3}(\mathbf{r}_i - \mathbf{r}_j).

Applying `i = 1,2` produces the equations of motion for each of the two bodies.
You can verify that these equations are the **same** as :eq:`Newton`.

using the Hamiltonian
---------------------

.. admonition:: Recall

    Hamilton's canonical equations are

    .. math::
        \dot{\mathbf{q}} = +\frac{\partial H}{\partial \mathbf{p}} \qquad \text{and} \qquad \dot{\mathbf{p}} = -\frac{\partial H}{\partial \mathbf{q}}

    for generalized coordinates and momenta `\mathbf{q},\mathbf{p} \in \mathbb{R}^n`,
    where `H \in \mathbb{R}` is the Hamiltonian and `n` is the number of degrees of freedom in the system.

Using the Lagrangian :eq:`Lagrangian`, the Hamiltonian is defined

.. math::
    H &\equiv \sum_{i = 1}^2 \dot{\mathbf{q}}_i \cdot \mathbf{p}_i - L \\
    &= \underbrace{\frac{1}{2}\left(\frac{|\mathbf{p}_1|^2}{m_1} + \frac{|\mathbf{p}_2|^2}{m_2}\right)}_{\text{kinetic}} - \underbrace{\frac{G m_1 m_2}{|\mathbf{q}_2 - \mathbf{q}_1|}}_{-\text{potential}},

where `\mathbf{q}_i = \mathbf{r}_i` are the generalized coordinates
and `\mathbf{p}_i = m_i\dot{\mathbf{r}}_i` are the generalized momenta
for each body (`i = 1,2`).
Hamilton's canonical equations (12 of them) then say

.. math::
    :label: Hamilton

    \dot{\mathbf{q}}_i &= \frac{\mathbf{p}_i}{m_i} \\
    \dot{\mathbf{p}}_i &= -\frac{G m_1 m_2}{|\mathbf{q}_i - \mathbf{q}_j|^3} (\mathbf{q}_i - \mathbf{q}_j),

for `i = 1,2` and `j \neq i`. Despite having twice as many equations, you can verify that they *are* the **same** as :eq:`Newton`.