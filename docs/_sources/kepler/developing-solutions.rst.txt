.. default-role:: math

Developing a General Solution
*****************************

:Author: M. Werner

.. admonition:: Plan of Action

    Write down the **solution** to the 2-body problem in terms of `r` and
    `\theta` using the previously developed properties of the system.


We're finally ready to solve the 2-body problem! Well, kind of...
==================================================================

A solution of the radius `r = r(\theta)` is achievable, but
we fall *just* short of knowing `\theta(t).` The grim reality of the problem
is that the angle `\theta` has to be calculated **numerically**.

The results are summarized below.

.. important::

    **The radius** `r` **is a known function of the angle** `\theta` **and is**
    **parameterized by the system's characterization** (`\mu = \mathrm{const.}`) **and**
    **initial conditions** (`h = \mathrm{const.}` and `A = \mathrm{const.}`).

    .. math::
        :label: orbitalRadius

        r = \frac{h^2}{\mu + A\cos\theta}

    - We know exactly what path the reduced mass must trace out in the orbital plane.

    **The angle** `\theta`` **is NOT a known function of time.**
    **It must be obtained numerically and depends on the system's**
    **characterization and initial conditions as well as time.**

    - We don't know *exactly* where the reduced mass is in its trajectory at any given time (but we will be able to get "close enough").

Finding the radius as a function of the angle
=============================================

**Fact:** The distance between the two bodies measured with respect to
the angle subtended from the LRL vector in the orbital plane is given by
:eq:`orbitalRadius`.

..  admonition:: Proof using the LRL vector
    :class: toggle

    The LRL vector can be used to obtain an expression for the
    radius `r` as a function of the angle
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
        &= A r \cos\theta. \square

    ----

    Alternatively, knowing :eq:`AMconservation` and combining it with :eq:`LaplaceRungeLenz`
    yields the radius `r` even more simply.

    .. math::
        A\cos\theta &= r^3\dot{\theta}^2 - \mu \\
        &= \frac{h^2}{r} - \mu. \square

..  admonition:: Proof using the radial dynamics
    :class: toggle

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

    The final form of `r` is :eq:`orbitalRadius`. `\square`

Rewriting the radius in terms of the eccentricity
-------------------------------------------------

The radius `r` can be more simplified if we define the new variable
`e = A/\mu` called the **eccentricity.**
Doing this allows us to write the radius :eq:`orbitalRadius` as

.. math::
    :label: orbitalRadius_e

    r = \frac{h^2/\mu}{1 + e\cos\theta}

- This reduces the amount of parameters needed to study the trajectory from two (`\mu` and `A`) to one (`e`)
    - (There were only two parameters because we didn't actually need `h` to determine the trajectory's behavior)

Plotting the trajectory
-----------------------

Because the trajectory in the orbital plane is simply

.. math::

    \mathbf{r} = \begin{pmatrix}r\cos\theta \\ r\sin\theta \\ 0\end{pmatrix} = \frac{h^2}{\mu} \begin{pmatrix}\frac{\cos\theta}{1 + e\cos\theta} \\ \frac{\sin\theta}{1 + e\cos\theta} \\ 0\end{pmatrix},

we can easily visualize what the trajectory will do as the parameter `e` is varied.

- We do **not** need to vary the angular momentum `h` in this case because the behavior is simply scaled by `h^2/\mu.`

.. figure:: ../../images/kepler_trajectories_in_e_v2.svg
    :width: 471px
    :height: 237px
    :scale: 150 %
    :alt: Variation of trajectories in the orbital plane as `e` varies.
    :align: center

    Variation of trajectories in the orbital plane;
    each curve is labelled with its corresponding eccentricity value `e.`
    **Closed trajectories (red) are ellipses and open trajectories (green) are hyperbolas.**
    **The trajectory separating the two cases is shown in black.**

The above plot can shortly be summarized by the following table.

.. list-table:: Limits of the angle `\theta`
    :widths: 1 1 2
    :header-rows: 1
    :stub-columns: 1
    :align: center

    * - Class
      - Condition
      - Limits
    * - Closed
      - `e < 1`
      - `|\theta| < \pi`
    * - Open
      - `e \geqslant 1`
      - `|\theta| < \cos^{-1}(-e^{-1})`

- Closed trajectories are also called **elliptic**
- Open trajectories are also called **hyperbolic** (unless `e \equiv 1`, then the trajectory is called **parabolic**).

Finding the time as a function of the angle
===========================================
Knowing `r = r(\theta)`,
we would most like to know the angle `\theta = \theta(t)`.
This would fully complete the parameterization
as then `\mathbf{r} = \mathbf{r}(x(t), y(t), 0)` would be a known function for all
time.

**However, we're not so fortunate.**
Instead, we can obtain `t = t(\theta),` but inverting this function `t` is difficult.

**Fact:** The time since the reduced mass crossed the `x` axis (`\theta = 0`) is

.. math::
    :label: orbitTime

    t = \frac{h^3}{\mu^2}\left(\frac{2}{(1 - e^2)^{3/2}}\,\tan^{-1}\!\left(\sqrt{\frac{1 - e}{1 + e}}\tan\frac{\theta}{2}\right) - \frac{e\sin\theta}{(1 - e^2)(1 + e\cos\theta)}\right)

where `\theta` is limited according to the parameter `e.`

- This result is written for `e < 1,` but it is **still valid** when `e \geqslant 1` (where equality is taken in the sense of a limit).



..  admonition:: Proof using the angular momentum
    :class: toggle

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

    Taking `t_0 = \theta_0 = 0` yields the above result. `\square`

The orbital period
------------------

Looking closer at :eq:`orbitTime` shows that the time `t` is **odd** in the angle `\theta.`
(That is, `t(-\theta) = -t(\theta).`) This is useful because we can (more) easily calculate the
**period** (`T`) for a **closed** trajectory.
(An open trajectory can't have a period since it simply doesn't repeat itself.)
The period is

.. math::

    T = 2\pi \frac{h^3/\mu^2}{(1 - e^2)^{3/2}}, \qquad (e < 1).

..  admonition:: Proof
    :class: toggle

    Assume `e < 1` (so that a period exists). Using the fact that `t` is odd, calculate

    .. math::
        T &= \lim_{\theta\to\pi^-}t - \lim_{\theta\to-\pi^+}t \\
          &= 2\lim_{\theta\to\pi^-}t.

    The result comes out directly. `\square`

The (normalized) orbital period is plotted below as a function of the eccentricity `e.`

.. figure:: ../../images/kepler_trajectories_period_in_e.svg
    :width: 522px
    :height: 414px
    :scale: 100 %
    :alt: Variation of trajectory times of flight in the orbital plane as `e` varies.
    :align: center

    The orbital period `T` (scaled to a constant) of varying **closed** orbit trajectories characterized by eccentricity.

- **A circular orbit has (constant) angular velocity** `h^3/\mu^2.`

- The period is valid over one cycle of the orbit, but `t(\theta = 0) = 0` and
  `|\theta| < \pi.`

  - **We say the time over an orbit occurs between** `-T/2 < t < T/2.`

Plotting the time of flight
---------------------------
Using modern computational tools makes it "easy" to visualize what a typical
flight path looks like for any given eccentricity `e` as seen below.

- We do **not** need to know what `h^3/\mu^2` is since this is simply a
  constant that scales the actual behavior that we're interested in.

.. figure:: ../../images/kepler_trajectories_in_e_v2_dt=1.svg
    :width: 471px
    :height: 237px
    :scale: 150 %
    :alt: Variation of trajectory times of flight in the orbital plane as `e` varies.
    :align: center

    Plotting position on the orbit in equal timesteps of `\Delta t = 1.`
    **The motion is slowest at the furthest distances and fastest at the closest distances.**
    Note that the hyperbolic trajectory with `e=5` is moving so fast that it only shows 1 data point - the next is already out of frame.

This plot is obtained using **numerical root-finding** to determine the angle
`\theta` given equally spaced times `t.`
