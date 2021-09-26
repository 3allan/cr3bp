Orbital Elements
****************

:Author: M. Werner

.. contents:: Table of contents
   :local:
   :backlinks: none
   :depth: 3

the conservation of energy.

.. math::
    E &= \frac{1}{2}(\dot{r}^2 + r^2\dot{\theta}^2) - \frac{\mu}{r} \\
    &= \frac{1}{2}\left(\left(\frac{A}{h}\sin\theta\right)^{\!2} + \frac{h^2}{r^2}\right) - \frac{\mu}{r} \\
    &= \frac{1}{2}\left(\frac{A^2}{h^2}\sin^2\theta + \frac{(\mu + A\cos\theta)^2}{h^2}\right) - \frac{\mu}{r} \\
    &= \frac{1}{2}\left(\frac{A^2}{h^2}\sin^2\theta + \frac{\mu^2 + 2\mu A\cos\theta + A^2\cos^2\theta}{h^2}\right) - \frac{\mu}{r} \\
    &= \frac{1}{2}\left(\frac{A^2}{h^2}(\sin^2\theta + \cos^2\theta) + \frac{2\mu A\cos\theta}{h^2} + \frac{\mu^2}{h^2}\right) - \frac{\mu}{r} \\
    &= \frac{1}{2}\left(\frac{A^2}{h^2} + \frac{\mu^2}{h^2}\right) + \frac{\mu A \cos\theta}{h^2} - \frac{\mu}{r} \\
    &= \frac{1}{2}\left(\frac{A^2}{h^2} + \frac{\mu^2}{h^2}\right) + \frac{\mu A \cos\theta}{h^2} - \mu\left(\frac{\mu + A\cos\theta}{h^2}\right) \\
    &= \frac{1}{2}\left(\frac{A^2}{h^2} + \frac{\mu^2}{h^2}\right) + \frac{\mu A \cos\theta}{h^2} - \frac{\mu^2}{h^2} - \frac{\mu A\cos\theta}{h^2} \\
    &= \frac{1}{2}\left(\frac{A^2}{h^2} - \frac{\mu^2}{h^2}\right).

Thus, we see that the integration constant is related to the energy
according to

.. math::
    A = \mu \sqrt{1 + \frac{2Eh^2}{\mu^2}}.

We choose the positive branch (as opposed to the negative branch) of the
square root since :math:`A = |\mathbf{A}|` --- an explicitly nonnegative
quantity. For brevity, we write :math:`A = \mu e`, where

.. math::
    e = \sqrt{1 + \frac{2Eh^2}{\mu^2}}.

This quantity :math:`e` is called the orbital eccentricity.

.. important::
    The orbital radius :math:`r` found directly from solving the governing
    differential equation, utilizing the conservation of angular momentum
    and energy, and evaluating the two constants of integration yields

    .. math::
        r = \frac{h^2/\mu}{1 + e\cos\theta},

    where :math:`e = A/\mu` is dependent upon the energy :math:`E` of
    the relative motion of the two bodies.