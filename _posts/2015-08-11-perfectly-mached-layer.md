---
layout:     post
title:      Perfectly-mached layer
date:       2015-08-11 3:53:19
summary:    Perfectly-mached layer
permalink:	perfectly-mached-layer
---

The ideal for an artificial absorbing layer regardless of frequency and/or incident angle, is introduced mathematically by Berenger in 1994 called perfectly matched layer (PML). The key ideal of a PML is a medium that do not reflect at the interface and then strongly absorb from the interior region. Later, another formulation of PML has been introduced and become more popular due to its simplicity and efficiently, called uniaxial PML or UPML. An UPML is a PML layer with an artificial anisotropic absorbing material. Taking advantage of UPML, we can computationally introduce an angle-independent absorber material. 

Fresel equation:

$$S_{11}^{TE} = \frac{Z_2 cos\theta_i - Z_1 cos \theta_t}{Z_2 cos\theta_i + Z_1 cos \theta_t}$$

$$S_{21}^{TE} = \frac{2 Z_2 cos\theta_i}{Z_2 cos\theta_i + Z_1 cos \theta_t}$$

$$S_{11}^{TM} = \frac{Z_2 cos\theta_t - Z_1 cos \theta_i}{Z_2 cos\theta_t + Z_1 cos \theta_i}$$

$$S_{21}^{TM} = \frac{2 Z_2 cos\theta_i}{Z_2 cos\theta_t + Z_1 cos \theta_i}.$$

We now temporary dismiss the presence of the transmission in two above Eqs., due to the fact that the transmission can be entirely absorb when we put the dissipation part in both permittivity and permeability. The next work is to prevent the reflection, we need the impedance matched for any incident angle or polarization.

![Imgur](http://i.imgur.com/fSFHBPJ.gif)

To satisfy this condition, the reflections must vanish, or in other word $$Z_2=Z_1 \frac{cos \theta_t}{cos\theta_i}$$ and $$Z_2=Z_1\frac{cos\theta_i}{cos\theta_t}$$. Unfortunately, we have both impedances and angles in this term, so we cannot assure the impedance is matched for all of the angles. To overcome this problem, Sacks introduced an anisotropic material, in which the permittivity and permeability are in form of a tensor. The impedance of the PML $$Z=\sqrt{\frac{\mu_r}{\varepsilon_r}}$$, our work is to find a reflectionless layer or $$Z=1$$. We choose $$\left [ s \right ] = \left [ \mu_r \right ] = \left [ \varepsilon_r \right ] = \begin{bmatrix}
a & 0 & 0 \\ 
0 & b & 0\\ 
0 & 0 & c
\end{bmatrix}.$$ According to magnitude and phase matching at the boundary of two surface the Snell’s law become $$\sqrt{bc} sin\theta_t = sin \theta_i ,$$ and the reflection is represented by

$$S_{11}^{TE} = \frac{cos \theta_i - \sqrt{\frac{b}{a}} cos\theta_t}{cos\theta_i + \sqrt{\frac{b}{a}}cos\theta_t}$$

$$S_{11}^{TM} = \frac{\sqrt{\frac{b}{a}} cos \theta_t - cos\theta_i}{cos\theta_i + \sqrt{\frac{b}{a}}cos\theta_t}$$

We can freely to choose $$bc=1$$, to simplify the phase matching, it leads to $$\theta_t = \theta_i$$ and the reflection coefficient are no longer a function of incident angle. By also postulation $$a=b$$, the interface will be perfectly reflectionless for any frequency, angle of incident, and polarization. Thus, we can write our UPML interms of constitution parameters:

$$\left [ s \right ] = \left [ \mu_r \right ] = \left [ \varepsilon_r \right ] = \begin{bmatrix}
s & 0 & 0 \\ 
0 & s & 0\\ 
0 & 0 & s^{-1}
\end{bmatrix}.$$

If you have any questions, please __don't__ hesitate to contact me!


### References
[1] J. -P. Berenger, _J. Comput. Phys._ __114__, 185 (1994).

[2] Z. S. Sacks, D. M. Kingsland, R. Lee, and J.-F. Lee, _IEEE Trans. Antennas. Propag._ __43__, 1460 (1995).

[3] [CEM Lectures.](https://www.youtube.com/channel/UCPC6uCfBVSK71MnPPcp8AGA)

