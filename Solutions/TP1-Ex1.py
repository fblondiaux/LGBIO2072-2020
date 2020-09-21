#Ex1 - Solution
def syn_in(t, imean = 25e-11):
    """
    Function that produces sinusoidal input

    Args:
      t          : Vector of discretized time points 
      imean      : current mean amplitude [A]

    Returns:
      sin_i       : Sinusoidal input current
    """
    ########################
    #### Your code here ####
    ########################
    sin_i = imean * (1 + np.sin((t * 2 * np.pi) / 0.01))
    return sin_i

t_max = 150e-3   # second
dt = .1e-3        # second
t_range = np.arange(0,t_max, dt)

#Plot here
plt.plot(t_range,syn_in(t_range))
plt.title("Synaptic Input I(t)")
plt.xlabel('T [s]')
plt.ylabel('I(t) [A]')
plt.show()