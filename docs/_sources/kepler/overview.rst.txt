.. default-role:: math



============
Introduction
============

:Author: M. Werner

What is gravity anyway?
=======================
**Gravity**, also called **gravitational acceleration** or **gravitational attraction**, in its
*simplest* description is the attraction of two (or more) objects due to their **mass**.

Sir Isaac Newton developed a **model** for the attraction of two such objects
in his *Principia*. It says that two objects, one having mass `m_1` and the
other mass `m_2`, separated by a distance `r` exert a **force** on each
other. This force has a **magnitude** that can be written as

.. math::

    \frac{G m_1 m_2}{r^2},

where `G` is the gravitational constant, an experimentally determined number
that is true for *any* two objects being considered.

Theories of gravity have been floating around for centuries. This
particular one was published in 1687; since then, it has been well-studied,
tested, and developed into the modern day where it *still* serves as a
workhorse for *many* astrodynamics applications.

Einstein would like a word
==========================
Newton's description of gravity hung around for 230 years until it was
seriously challenged. After all, Newton's gravity is **not** perfect; it
simply offers a (very good) description of motion from a mechanical
perspective.

The contender was Albert Einstein's general theory of relativity, which came
to light in 1916. It not only describes the motion of objects that have
mass (like Newton did), but it describes the motion of objects that have *a
lot* of mass (black holes) and also objects that have *no* mass (photons).

Newton's description of "motion" would be position as a function of time,
but Einstein's description of "motion" includes position *and* time.
One takeaway from GR is that space and time are actually interwoven.
There is no such thing as absolute time, and there are no inertial
reference frames (which are necessary to use Newton's laws).

The implications coming from general relativity were *shattering* to all of
physics, but it since *vastly* improved our understanding and has not only
stood, but *completely dominated* the tests of time.

So which one do we use?
=======================
General relativity is widely accepted as correct. However, it gets
complicated *fast*. There aren't really that many analytic solutions, and
integrating its equations of motion on a computer can be slow.

**We use Newtonian gravity** despite it being fundamentally **wrong**!
We do this because it's much easier than GR in terms of comprehension and
computability, and it's "close enough" for almost *all* practical
applications. Any spacecraft we launch will most likely not be interacting
near black holes or travelling at any appreciable fraction of the
speed of light.

With that, it's time to dive into orbital mechanics!