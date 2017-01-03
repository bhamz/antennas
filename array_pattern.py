from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt

#assumes antenna operating wavelength is 1 unit length
class rad_pattern(object):
# member variables

    def __init__(self, number_of_antennas, spacing_in_wavelengths, phase_difference,\
    discretization_num):
        wavelength = 1 # using units of antenna wavelength
        self.N = number_of_antennas
        self.spacing = spacing_in_wavelengths
        self.d_phi = phase_difference
        self.n = discretization_num
        self.k = 2*np.pi/wavelength

    def polar_plot(self):
        theta = np.linspace(0,2*np.pi,self.n)
        psi = self.spacing * self.k * np.cos(theta) + self.d_phi # from Stutzman
        f = abs((np.sin(self.N*psi/2))/(self.N*np.sin(psi/2)))  #    p. 279
        plt.figure(1)
        ax1 = plt.subplot(projection = 'polar')
        ax1.plot(theta,f)

    def wave_plot(self):
        L = 50*self.N*self.spacing # plenty to see contructive pattern
        axes = np.linspace(-L/2,L/2,self.n)
        X,Y = np.meshgrid(axes,axes) # ortho axes for wave fn
        phase = 0; position = 0; wavePattern = 0*X
        for ii in range(self.N): # add this many waves atop ea other
            dist = np.sqrt(((X+position)**2)+(Y**2)) # sorta yucky to have in same line as blow
            wavePattern += np.exp(1j*(self.k*dist-phase))
            position += self.spacing  # incr antenna position
            phase += self.d_phi         # and feed phase

        fig2 = plt.figure(2)
        ax2 = fig2.gca(projection = '3d')
        surf = ax2.plot_surface(X,Y,np.real(wavePattern),cmap = cm.coolwarm,linewidth=0,\
        rstride = 1, cstride = 1)
        ax2.view_init(60,90) # similar orientation to polar graph

lil_fella = rad_pattern(10,0.75,3*np.pi/5,101)
lil_fella.wave_plot()
plt.show()
