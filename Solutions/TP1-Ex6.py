#Solution of Ex6
def rand_syn(t,sigma = 0.1, imean = 25e-11):
    """
    Function that produces random input current

    Args:
      t          : vector of discretized time points 
      imean      : current mean amplitude [A]
      sigma      : variance of the random input current

    Returns:
      sin_i       : Sinusoidal input current
    """
    dt = t[1]-t[0]
    rand_i = imean * (1 + 0.1 * (np.sqrt(np.max(t)/dt)) * np.random.normal(0,sigma,len(t)))
    return rand_i

t_max = 150e-3   # second
dt = .1e-3        # second
t_range = np.arange(0,t_max,dt)

plt.plot(t_range,rand_syn(t_range))
plt.title('Input current')
plt.ylabel('I [A]')
plt.xlabel('T [S]')
plt.show()
    