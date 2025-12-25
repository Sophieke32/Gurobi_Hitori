def set_model_parameters(m):
    # Silence model, set memory limit to 8 GB and threads to 1, set seed to 32
    m.params.OutputFlag = 0
    m.params.MemLimit = 8
    m.params.Threads = 1
    m.params.Seed = 32