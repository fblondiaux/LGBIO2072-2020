# Solution to Ex3
def simple_LIF(input_current,t,  tau= 20e-3 , urest= -60e-3 , r= 100e6, ureset = -70e-3 \
               ,theta = -50e-3 ):
    """
    Authors : Antoine de Comite and Florence Blondiaux
    Simulate the integration of the membrane potential and the generation of spikes
    in response to an external input current

    Args:
      input_current   : Vector containing the input current [A].
      t               : Vector containing the discretized time points [s]
      tau             : Membrane time constant. Default value: 20e-3 [s]
      urest           : Leak potential. Default value: -60e-3 [V]
      r               : Leak resistance. Default value: 100e6 [Ohm]
      ureset          : Reset potential. Default value: -70e-3[V]
      theta           : Firing threashold. -50e-3 [V]
    Returns:
      u               : membrane potential [V]
      ts              : spike times [s]
    """
    ts = []
    dt = t[1]-t[0]
    u = np.zeros(len(input_current))
    u[0]=urest
    for step in range(0,len(input_current)-1):
        if u[step] > theta:
            u[step] = theta/1.2
            u[step+1] = ureset
            ts.append(t[step])
        else:
            u[step+1]=u[step] -dt/tau * (u[step]-urest) + r*dt/tau * input_current[step]
    return u, ts

t_max = 150e-3   # second
dt = .1e-3       # second
t_range = np.arange(0,t_max,dt)
input_current = syn_in(t_range)
u ,ts = simple_LIF(input_current, t_range)

fig, axs = plt.subplots(2)
axs[0].plot(t_range,input_current)
axs[0].set(title = "Input current", ylabel = "I [A]")
axs[1].plot(t_range,u)
axs[1].plot(ts,np.ones(len(ts))*theta/1.2,'r.',markersize=12)
axs[1].set(title = "Membrane potential", ylabel = "u [V]", xlabel= "Time [S]")
plt.show()