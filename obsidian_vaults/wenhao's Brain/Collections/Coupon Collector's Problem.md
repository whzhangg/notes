# Coupon Collector’s Problem
Created: January 10, 2022 9:12 PM
Description: https://en.wikipedia.org/wiki/Coupon_collector%27s_problem

We consider the problem as follows:
>There are *n* different types of coupons that can be collected from a box. Everytime a coupons is draw with replacement: it is put back into the box so that it will appear again. 
>
>How many draw on average is needed to collect all coupons?

##### Solution
We consider we have already collected *i-1* different coupons and we want to collect the *i*-th coupons that is not yet collected. 

The probability of collecting a new coupon is therefore:
$$
p_i = \frac{n - (i-1)}{n} = \frac{n-i+1}{n}
$$

As a result, it will take on average $1/P_i = n/(n-i+1)$ attempts to draw the i-th new coupons. To draw all coupons, we have the expection value of total number of steps:
$$
\begin{align}
E(T) &= E(t_1 + t_2 + \cdots + t_n )  =E(t_1) + E(t_2) + \cdots + E(t_n) \\ 
&= \frac{1}{p_1}+ \frac{1}{p_2} + \cdots + \frac{1}{p_n} = \frac{n}{n} + \frac{n}{n-1} + \cdots + \frac{n}{1} \\ 
&= n \left(\frac{1}{1} + \frac{1}{2} + \cdots + \frac{1}{n} \right) = n H_n
\end{align}
$$
where $H_n$ is called harmonic number. The derivation is interpreted as summing up the expectation value of number of drawing required to draw a new coupons, which is *1* when it is the first draw and *n* to draw the final unseen value.

we can approximate the expectation value as:
$$
E(T) = nH_n = n\log n + \gamma n + 0.5 + O(1/n)
$$
$\gamma \approx 0.5772$  is called Euler-Mascheroni constant

reference: https://en.wikipedia.org/wiki/Coupon_collector%27s_problem