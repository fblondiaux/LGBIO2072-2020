# Solution of Ex2
def membranePot(input_current, t, tau= 20e-3 , urest= -60e-3 , r= 100e6):
    """
    Authors : Antoine de Comite and Florence Blondiaux
    Simulate the integration of the membrane potential with external input current

    Args:
      input_current   : Vector containing the input current [A].
      t               : Vector containing the discretized time points [s].
      tau             : Membrane time constant. Default value: 20e-3 [s]
      urest           : Leak potential. Default value: -60e-3 [V]
      r               : Leak resistance. Default value: 100e6 [Ohm]
    Returns:
      u               : membrane potential [V]
    """
    dt = t[1]-t[0]
    u = np.zeros(len(input_current))
    u[0]=urest
    for step in range(len(input_current)-1):
        u[step+1]=u[step] + dt/tau * ( -u[step] + urest +r* input_current[step+1])
    return u

#Generates a random input current
t_max = 150e-3   # second
dt = .1e-3        # second
t_range = np.arange(0,t_max,dt)
input_current = syn_in(t_range)
u = membranePot(input_current, t_range)

fig, axs = plt.subplots(2)
axs[0].plot(t_range,input_current)
axs[0].set(title = "Input current", ylabel = "I [A]")
axs[1].plot(t_range,u)
axs[1].set(title = "Membrane potential", ylabel = "u [V]", xlabel= "Time [S]")
plt.show()