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
<img style="display: block; margin: auto;" src="../images/kepler_2_particles.svg" alt="Two point masses in an inertial frame" width="700"/>

Here, we assume (without loss of generality) that $$m_1 \geqslant m_2$$ are the body masses.

The equations of motion for the general 2-body problem are derived below using a variety of methods.

[Newton's Laws](#newtons-laws)
-------------

Applying Newton's 2<sup>nd</sup> law to each body provides

$$\begin{align}
\ddot{\mathbf{r}}_1 &= -\frac{Gm_2}{|\mathbf{r}_1 - \mathbf{r}_2|^3}(\mathbf{r}_1 - \mathbf{r}_2) \\ 
\ddot{\mathbf{r}}_2 &= -\frac{Gm_1}{|\mathbf{r}_2 - \mathbf{r}_1|^3}(\mathbf{r}_2 - \mathbf{r}_1),
\end{align}$$

where $$G$$ is Newton's universal gravitational constant.

Written in vector form, this set of equations actually forms 6 2<sup>nd</sup> order equations (equivalently, 12 1<sup>st</sup> order equations). To reduce the complexity of the system, we can define the *relative* distance between each body as<br>
\begin{equation}
\boxed{\mathbf{r} = \mathbf{r}_2 - \mathbf{r}_1.}
\end{equation}

Doing this is beneficial because it exploits a symmetry, effectively halving the number of equations and decreasing the amount of coupling between them. It also provides **direct** information of **both** bodies (relative to the other) rather than relying on the origin of an arbitrarily defined (inertial) coordinate system.

With this in mind, taking 2 time derivatives of this definition directly gives

$$\begin{align}
\ddot{\mathbf{r}} &= \ddot{\mathbf{r}}_2 - \ddot{\mathbf{r}_1} \\
&= -\frac{G(m_1 + m_2)}{r^3}\mathbf{r}.
\end{align}$$

**Note**: The same result is reached had we used instead that $$-\ddot{\mathbf{r}}_1 \equiv (m_2/m_1)\ddot{\mathbf{r}}_2$$ by Newton's 3<sup>rd</sup> law.

$$\begin{align}
\ddot{\mathbf{r}} &= \ddot{\mathbf{r}}_2 + \frac{m_2}{m_1}\ddot{\mathbf{r}}_2 \\
&= \left(1 + \frac{m_2}{m_1}\right)\ddot{\mathbf{r}}_2 \\
&= \left(\frac{m_1 + m_2}{m_1}\right) \left(-\frac{Gm_1}{r^3}\mathbf{r}\right) \\
&= -\frac{G(m_1 + m_2)}{r^3}\mathbf{r}
\end{align}$$

[Lagrangian Function](#lagrangian-function)
-------------------
We can write a Lagrangian of a 2-particle system that's simply the difference between total kinetic energy and total potential energy

$$\begin{align}
\mathcal{L} &= T - V \\
&= \frac{1}{2}\left(m_1 |\dot{\mathbf{r}}_1|^2 + m_2 |\dot{\mathbf{r}}_2|^2\right) + \frac{Gm_1m_2}{|\mathbf{r}_2 - \mathbf{r}_1|}.
\end{align}$$

Since gravity is conservative, the corresponding Euler-Lagrange equations (all 6 of them) are written

$$\begin{align}
\mathbf{0} &= \frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{\mathbf{r}}_i} - \frac{\partial \mathcal{L}}{\partial\mathbf{r}_i} && (i = 1, 2) \\
&= \frac{d}{dt}(m_i\dot{\mathbf{r}}_i) - \frac{Gm_1m_2}{|\mathbf{r}_j - \mathbf{r}_i|^3}(\mathbf{r}_j - \mathbf{r}_i) && (j \neq i) \\
&= m_i\ddot{\mathbf{r}}_i + \frac{Gm_1m_2}{|\mathbf{r}_i - \mathbf{r}_j|^3}(\mathbf{r}_i - \mathbf{r}_j).
\end{align}$$

Through this Lagrangian approach, we indeed get the same equations of motion that were determined from the application of Newton's laws.

$$\begin{align}
\ddot{\mathbf{r}}_1 &= -\frac{Gm_2}{|\mathbf{r}_1 - \mathbf{r}_2|^3} (\mathbf{r}_1 - \mathbf{r}_2) \\
\ddot{\mathbf{r}}_2 &= -\frac{Gm_1}{|\mathbf{r}_2 - \mathbf{r}_1|^3} (\mathbf{r}_2 - \mathbf{r}_1)
\end{align}$$

We can therefore follow the procedure of defining $$\mathbf{r} = \mathbf{r}_2 - \mathbf{r}_1$$ generating the equation for relative position,

$$\begin{equation}
\ddot{\mathbf{r}} = -\frac{G(m_1 + m_2)}{r^3}\mathbf{r}.
\end{equation}$$

[Hamiltonian Function](#hamiltonian-function)
--------------------
Let the generalized coordinates be $$\mathbf{q}_i = \mathbf{r}_i$$ and the generalized momenta be $$\mathbf{p}_i = m_i\dot{\mathbf{r}}_i$$ for each body $$i$$ such that the Hamiltonian $$\mathcal{H}$$ is a function of both $$\mathbf{p}$$'s and $$\mathbf{q}$$'s. Applying the definition of the Hamiltonian function provides

$$\begin{align}
\mathcal{H} &= \sum_{i = 1}^2 \dot{\mathbf{q}}_i \cdot \mathbf{p}_i - \mathcal{L} \\
&= \sum_{i = 1}^2 \frac{1}{m_i}  \mathbf{p}_i\cdot \mathbf{p}_i - \left[\frac{1}{2}\left(\frac{|\mathbf{p}_1|^2}{m_1} + \frac{|\mathbf{p}_2|^2}{m_2}\right) + \frac{Gm_1m_2}{|\mathbf{q}_2 - \mathbf{q}_1|}\right] \\
&= \frac{1}{2}\left(\frac{|\mathbf{p}_1|^2}{m_1} + \frac{|\mathbf{p}_2|^2}{m_2}\right) - \frac{Gm_1m_2}{|\mathbf{q}_2 - \mathbf{q}_1|}.
\end{align}$$

Hamilton's canonical equations (for $$i = 1, 2$$) then require

$$\begin{align}
\dot{\mathbf{q}}_i &= \frac{1}{m_i}\mathbf{p}_i \\
\dot{\mathbf{p}}_i &= -\frac{Gm_1m_2}{|\mathbf{q}_i - \mathbf{q}_j|^3}(\mathbf{q}_i - \mathbf{q}_j), && (j \neq i). \\
\end{align}$$

Note that these 12 equations are identical to those found previously for $$\ddot{\mathbf{r}}_i$$, just placed into first-order form. Thus, it's possible to recover the relative distance $$\mathbf{r}$$ from here.

As this is a Hamiltonian system, however, the equations *may* be simplified more if desired, subject to the condition that the coordinate transformations are canonical.


[Summary](#summary)
-------

In ***all*** approaches (<a href="#newtons-laws">Newtonian</a>, <a href="#lagrangian-function">Lagrangian</a>, and <a href="#hamiltonian-function">Hamiltonian</a>), we arrive at the standard form of the 2-body equations of motion after defining the mass parameter

\begin{equation}
\boxed{\mu \equiv G(m_1 + m_2)}
\end{equation}

such that the equations of motion for one body about the other are

$$
\boxed{\begin{equation}\ddot{\mathbf{r}} = -\frac{\mu}{r^3}\mathbf{r}.\end{equation}}
$$


**In practical (engineering) applications of the 2-body problem, it's very often the case that $$m_1 \ggg m_2$$ for which $$\mu \approx G m_1$$.**

With this approximation, also note that the quantity $$Gm$$ is **much** more accurately known for a given body than either $$G$$ or $$m$$ are. This is due in part because of our ability to study the resulting motion of a spacecraft much more precisely than we can experimentally determine $$G$$ or "weigh" celestial bodies.

<footer>
  <strong>Related Posts</strong>
  <ul>
    <li><a href="/kepler/properties/">Properties of the Kepler Problem</a></li>
  </ul>
</footer>


