#Solution to Ex7
def my_OU(range_t, tau_ou, mu, sig, myseed=2072):
    """
    Function that produces Ornstein-Uhlenbeck input
    Args:
        tau_ou     : time constant [s]
        mu         : mean noise [A]
        sig        : noise amplitude [A]
        myseed     : random seed. int or boolean

    Returns:
        I_ou       : Ornstein-Uhlenbeck input current [A]
    """
    # set random seed
    if myseed:
      np.random.seed(seed=myseed)
    else:
      np.random.seed()
    # Retrieve simulation parameters
    dt=range_t[1]-range_t[0]
    Lt = range_t.size
    

    # Initialize
    noise = np.random.randn(Lt)
    I_ou = np.zeros(Lt)
    I_ou[0] = noise[0] * sig

    # generate OU
    for it in range(Lt-1):
        I_ou[it+1] = I_ou[it] + (dt / tau_ou) * (mu - I_ou[it]) + np.sqrt(2 * dt / tau_ou) * sig * noise[it + 1]

    return I_ou
t_max = 1000e-3   # second
dt = .1e-3        # second
range_t = np.arange(0,t_max,dt)
I_ou = my_OU(range_t=range_t,tau_ou=20e-3,mu=100e-12, sig=20e-12)
plt.plot(range_t,I_ou)
plt.title('Input current')
plt.ylabel('I [A]')
plt.xlabel('T [S]')
plt.show()