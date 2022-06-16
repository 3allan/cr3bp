.. default-role:: math
.. sectionauthor:: Matt Werner
.. codeauthor:: Matt Werner

:sd_hide_title:

Constants of Motion
********************

:Info: **Insights and Conserved Quantities:** The general 2-body problem may be simplified greatly by utilizing several special properties admitted by the system. These properties *will* enable a full solution of the general problem to be determined analytically.
:Description: Develop the two-body problem's constants of motion (`\mathbf{h}`, `\mathbf{A}`, and `E`).
:Author: Matt Werner







Angular momentum
================
.. admonition:: Recall

    #.  For any `\mathbf{x} \in \mathbb{R}^3`, the cross-product of `\mathbf{x}`
        with itself vanishes.

    .. math:: \mathbf{x} \times \mathbf{x} \equiv \mathbf{0}

    #.  For any `\mathbf{x},\mathbf{y} \in \mathbb{R}^3`, the cross-product is
        anticommutative.

    .. math:: \mathbf{x} \times \mathbf{y} = -(\mathbf{y} \times \mathbf{x})

Rewriting the Kepler problem in a convenient form,

.. math:: \ddot{\mathbf{r}} + \frac{G(m_1 + m_2)}{r^3}\mathbf{r} = \mathbf{0},

lets us immediately show

.. math::
    \mathbf{0} &= \left(\ddot{\mathbf{r}} + \frac{G(m_1 + m_2)}{r^3}\mathbf{r}\right) \!\times \mathbf{r} \\
    &= \ddot{\mathbf{r}} \times \mathbf{r} + \left(\frac{G(m_1 + m_2)}{r^3}\mathbf{r}\right) \!\times \mathbf{r} \\
    &= \ddot{\mathbf{r}} \times \mathbf{r} + \frac{G(m_1 + m_2)}{r^3}\left(\mathbf{r} \times \mathbf{r}\right) \\
    &= \ddot{\mathbf{r}} \times \mathbf{r} \\
    &= \ddot{\mathbf{r}} \times \mathbf{r} + \dot{\mathbf{r}} \times \dot{\mathbf{r}} \\
    &= \frac{d}{dt}\underbrace{(\dot{\mathbf{r}} \times \mathbf{r})}_{-\mathbf{h}}.

We conclude that the (specific) angular momentum `\mathbf{h}` is conserved under the dynamics of the 2-body problem.

.. math::
    :label: angularMomentum

    \mathbf{h} = \mathbf{r} \times \dot{\mathbf{r}} \equiv \mathrm{const.}

.. Important::
    **The motion of the two bodies must be planar, and the angular momentum is perpendicular to this plane!**

Laplace's vector
================
.. admonition:: Recall

    #.  For any `\mathbf{x},\mathbf{y},\mathbf{z} \in \mathbb{R}^3`, the vector triple product satisfies

    .. math:: \mathbf{x} \times (\mathbf{y} \times \mathbf{z}) = (\mathbf{x} \cdot \mathbf{z}) \mathbf{y} - (\mathbf{x} \cdot \mathbf{y}) \mathbf{z}.

    #. For any `\mathbf{x},\mathbf{y} \in \mathbb{R}^3`, the dot product is commutative.

    .. math:: \mathbf{x}\cdot\mathbf{y} = \mathbf{y}\cdot\mathbf{x}

Knowing that the angular momentum `\mathbf{h}` is conserved, we can do the following calculation.

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

Finally, we can combine the first and last expressions since the derivative is a linear operation. This provides the conserved quantity `\mathbf{A}`, the so-called **Laplace-Runge-Lenz** (or simply **Laplace**) **vector**\ [1]_.

.. math::
    \mathbf{A} = \dot{\mathbf{r}} \times \mathbf{h} - \frac{G(m_1 + m_2)}{r}\mathbf{r} \equiv \mathrm{const.}

.. Important::
    **There is a direction in the plane of motion of the two bodies that stays constant as a function of relative position and velocity!**

Energy
======
We can
Manipulating the relative form of the equations of motion provides

.. math::
    0 &= \left(\ddot{\mathbf{r}} + \frac{G(m_1 + m_2)}{r^3}\mathbf{r}\right) \cdot \dot{\mathbf{r}} \\
    &= \ddot{\mathbf{r}} \cdot \dot{\mathbf{r}} + \left(\frac{G(m_1 + m_2)}{r^3}\mathbf{r}\right) \cdot \dot{\mathbf{r}} \\
    &= \frac{1}{2}\frac{d}{dt}(\dot{\mathbf{r}} \cdot \dot{\mathbf{r}}) + \frac{G(m_1 + m_2)}{r^3}(\mathbf{r} \cdot \dot{\mathbf{r}}) \\
    &= \frac{1}{2}\frac{d}{dt}(\dot{\mathbf{r}} \cdot \dot{\mathbf{r}}) + \frac{G(m_1 + m_2)}{r^2}\dot{r} && \quad \left(\mathbf{r} \cdot \dot{\mathbf{r}} = r\dot{r}\right) \\
    &= \frac{1}{2}\frac{d}{dt}(\dot{\mathbf{r}} \cdot \dot{\mathbf{r}}) + \frac{d}{dt}\left(-\frac{G(m_1 + m_2)}{r}\right) \\
    &= \frac{d}{dt}\left(\frac{\dot{\mathbf{r}} \cdot \dot{\mathbf{r}}}{2} - \frac{G(m_1 + m_2)}{r}\right).

This quantity can be easily identified as a sort of total specific mechanical energy --- that is, the total mechanical energy per unit mass.

.. math::
    E = \frac{v^2}{2} - \frac{G(m_1 + m_2)}{r} \equiv \mathrm{const.}

Here, `v = |\dot{\mathbf{r}}|` is the magnitude of the (inertial) velocity. Note that the gravitational potential is appearing to come from a body of mass `m_1 + m_2`.

.. important::
    The relative motion of the two bodies **must** be such that the relative orbital velocity `v` and relative orbital radius `r` interplay with an inverse relationship for a given, fixed energy `E`.

----------------------------------------------------------------------------

.. [1] Goldstein, Poole, Safko. Classical Mechanics, 3rd Edition. Pgs. 102-103