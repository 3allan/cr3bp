---
layout: post
title:  "Testing MathJax"
date:   2021-07-10 16:48:17 -0400
categories: jekyll testing
---

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

Hello! Here is my first attempt to use $$\LaTeX$$ in Jekyll

$$f(x) = \int_0^x \sin(s^2)\,ds$$

Here's an equation environment
\begin{equation}
a^2 + b^2 = c^2
\end{equation}
Another one

$$
\begin{align}
1 &= 1 \\
2 &= 2.
\end{align}
$$

My own code snippit in Python
{% highlight python %}
def print_hi(name)
  print "Hi" + name
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}

My own code snippit in Matlab
{% highlight matlab %}
function z = f(x, y)
z = sinpi(x) + y;
end
{% endhighlight %}

-----
