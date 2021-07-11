---
layout: page
title: The Kepler Problem
date:   2021-07-10 19:26:48 -0400
permalink: /kepler/
sidebar_link: true
---

<header>
  <strong>Contents</strong>
    <ul>
      <li><a href="#newtons-laws">Newton's Laws</a></li>
      <li><a href="#lagrangian-function">Lagrangian Function</a></li>
      <li><a href="#hamiltonian-function">Hamiltonian Function</a></li>
      <li><a href="#summary">Summary</a></li>
    </ul>
</header>

[//]: # (Include MathJax on this page)
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

[//]: # (Page content)
The *Kepler* (2-body) problem is fundamental to the study of astrodynamics, especially so for analyzing the more general 3-body problem.

It consists of determining the positions of 2 bodies under mutual Newtonian gravitational attraction with respect to an inertial frame.

[//]: # Draw inertial coordinate frame with masses
<img style="display: block; margin: auto;" src="../latex/kepler_2_particles.svg" alt="Two point masses in an inertial frame" width="700"/>

Here, we assume $$m_1 \geqslant m_2$$ (without loss of generality) are the body masses.

[Newton's Laws](#newtons-laws)
-------------

Applying Newton's 2<sup>nd</sup> law to each body provides

$$\begin{align}
\ddot{\vec{r}}_1 &= -\frac{Gm_2}{|\vec{r}_1 - \vec{r}_2|^3}(\vec{r}_1 - \vec{r}_2) \\ 
\ddot{\vec{r}}_2 &= -\frac{Gm_1}{|\vec{r}_2 - \vec{r}_1|^3}(\vec{r}_2 - \vec{r}_1),
\end{align}$$

where $$G$$ is Newton's universal gravitational constant.

Written in vector form, this set of equations actually forms 6 2<sup>nd</sup> order equations (equivalently, 12 1<sup>st</sup> order equations). To reduce the complexity of the system, we can define the *relative* distance between each body as<br>
\begin{equation}
\boxed{\vec{r} = \vec{r}_2 - \vec{r}_1.}
\end{equation}

Doing this is beneficial because it exploits a symmetry, effectively halving the number of equations and decreasing the amount of coupling between them. It also provides **direct** information of **both** bodies (relative to the other) rather than relying on an arbitrarily defined inertial coordinate system.

With this in mind, taking 2 time derivatives of this definition directly gives

$$\begin{align}
\ddot{\vec{r}} &= \ddot{\vec{r}}_2 - \ddot{\vec{r}_1} \\
&= -\frac{G(m_1 + m_2)}{r^3}\vec{r}.
\end{align}$$

**Note**: The same result is reached had we used instead that $$-\ddot{\vec{r}}_1 \equiv (m_2/m_1)\ddot{\vec{r}}_2$$ by Newton's 3<sup>rd</sup> law.

$$\begin{align}
\ddot{\vec{r}} &= \ddot{\vec{r}}_2 + \frac{m_2}{m_1}\ddot{\vec{r}}_2 \\
&= \left(1 + \frac{m_2}{m_1}\right)\ddot{\vec{r}}_2 \\
&= \left(\frac{m_1 + m_2}{m_1}\right) \left(-\frac{Gm_1}{r^3}\vec{r}\right) \\
&= -\frac{G(m_1 + m_2)}{r^3}\vec{r}
\end{align}$$

[Lagrangian Function](#lagrangian-function)
-------------------
We can write a Lagrangian of a 2-particle system that's simply the difference between total kinetic energy and total potential energy

$$\begin{align}
\mathcal{L} &= T - V \\
&= \frac{1}{2}\left(m_1 |\vec{v}_1|^2 + m_2 |\vec{v}_2|^2\right) + \frac{Gm_1m_2}{|\vec{r}_2 - \vec{r}_1|},
\end{align}$$

where $$\vec{v}_i \equiv \dot{\vec{r}}_i$$ is the inertial velocity of body $$i$$ (either 1 or 2).

Since gravity is conservative, the corresponding Euler-Lagrange equations (all 6 of them) provide

$$\begin{align}
\vec{0} &= \frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \vec{v}_i} - \frac{\partial \mathcal{L}}{\partial\vec{r}_i} && (i = 1, 2) \\
&= \frac{d}{dt}(m_i\vec{v}_i) - \frac{Gm_1m_2}{|\vec{r}_j - \vec{r}_i|^3}(\vec{r}_j - \vec{r}_i) && (j \neq i) \\
&= m_i\ddot{\vec{r}}_i - \frac{Gm_1m_2}{|\vec{r}_j - \vec{r}_i|^3}(\vec{r}_j - \vec{r}_i).
\end{align}$$

Through this Lagrangian approach, we indeed get the same equations of motion determined by application of Newton's laws.

$$\begin{align}
\ddot{\vec{r}}_1 &= -\frac{Gm_2}{|\vec{r}_1 - \vec{r}_2|^3} (\vec{r}_1 - \vec{r}_2) \\
\ddot{\vec{r}}_2 &= -\frac{Gm_1}{|\vec{r}_2 - \vec{r}_1|^3} (\vec{r}_2 - \vec{r}_1)
\end{align}$$

We can therefore follow the same procedure of defining $$\vec{r} = \vec{r}_2 - \vec{r}_1$$ generating the equation

$$\begin{equation}
\ddot{\vec{r}} = -\frac{G(m_1 + m_2)}{r^3}\vec{r}.
\end{equation}$$

[Hamiltonian Function](#hamiltonian-function)
--------------------
Let the generalized coordinates be $$\vec{q}_i = \vec{r}_i$$ and the generalized momenta be $$\vec{p}_i = m_i\vec{v}_i$$ for each body $$i$$ such that the Hamiltonian $$\mathcal{H}$$ is a function of both $$\vec{p}$$'s and $$\vec{q}$$'s. Applying the definition of the Hamiltonian function provides

$$\begin{align}
\mathcal{H} &= \sum_{i = 1}^2 \dot{\vec{q}}_i \cdot \vec{p}_i - \mathcal{L} \\
&= \sum_{i = 1}^2 \frac{1}{m_i}  \vec{p}_i\cdot \vec{p}_i - \left[\frac{1}{2}\left(\frac{|\vec{p}_1|^2}{m_1} + \frac{|\vec{p}_2|^2}{m_2}\right) + \frac{Gm_1m_2}{|\vec{q}_2 - \vec{q}_1|}\right] \\
&= \frac{1}{2}\left(\frac{|\vec{p}_1|^2}{m_1} + \frac{|\vec{p}_2|^2}{m_2}\right) - \frac{Gm_1m_2}{|\vec{q}_2 - \vec{q}_1|}.
\end{align}$$

Hamilton's canonical equations (for $$i = 1, 2$$) then require

$$\begin{align}
\dot{\vec{q}}_i &= \frac{1}{m_i}\vec{p}_i \\
\dot{\vec{p}}_i &= -\frac{Gm_1m_2}{|\vec{q}_j - \vec{q}_i|^3}(\vec{q}_j - \vec{q}_i), && (j \neq i). \\
\end{align}$$

Note that these 12 equations are identical to those found previously for $$\ddot{\vec{r}}$$, just placed into first-order form. As this is a Hamiltonian system, however, they *may* be simplified more if desired, granted the coordinate transformations are canonical.


[Summary](#summary)
-------

In ***all*** approaches (<a href="#newtons-laws">Newtonian</a>, <a href="#lagrangian-function">Lagrangian</a>, and <a href="#hamiltonian-function">Hamiltonian</a>), we arrive at the standard form of the 2-body equations of motion after defining the mass parameter

\begin{equation}
\boxed{\mu \equiv G(m_1 + m_2)}
\end{equation}

such that the equations of motion become<br>

$$
\boxed{\begin{equation}\ddot{\vec{r}} = -\frac{\mu}{r^3}\vec{r}.\end{equation}}
$$


**In practical (engineering) applications of the 2-body problem, it's very often the case that $$m_1 \ggg m_2$$ for which $$\mu \approx G m_1$$.**

With this approximation, also note that the quantity $$Gm$$ is **much** more accurately known for a given body than either $$G$$ or $$m$$ are. This is due in part because of our ability to study the motion of spacecraft much more precisely than we can "weigh" Earth or other bodies.

<footer>
  <strong>Related Posts</strong>
  <ul>
    <li><a href="/kepler/properties/">Properties of the Kepler Problem</a></li>
  </ul>
</footer>


