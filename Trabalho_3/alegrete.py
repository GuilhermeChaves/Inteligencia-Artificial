def compute_mse(theta_0, theta_1, data):
    mse = 0
    num_linhas = 0

    for line in data:
        x = line[0]
        y = line[1]
        num_linhas += 1 

        mse += ((theta_0 + theta_1 * x) - y)**2 

    mse /= num_linhas

    return mse

    

def step_gradient(theta_0, theta_1, data, alpha):
    somatorio_t0 = 0
    somatorio_t1 = 0
    num_linhas = 0

    for line in data:
        x = line[0]
        y = line[1]
        num_linhas += 1 

        somatorio_t0 += (theta_0 + theta_1 * x) - y
        somatorio_t1 += ((theta_0 + theta_1 * x) - y) * x

    derivada_t0 = (2/num_linhas) * somatorio_t0
    derivada_t1 = (2/num_linhas) * somatorio_t1

    novo_t0 = theta_0 - alpha * derivada_t0
    novo_t1 = theta_1 - alpha * derivada_t1
    
    return (novo_t0, novo_t1)



def fit(data, theta_0, theta_1, alpha, num_iterations):
    list_theta0 = list()
    list_theta1 = list()
    list_aux = list()

    list_aux.append((theta_0, theta_1))
    list_theta0.append(list_aux[-1][0])
    list_theta1.append(list_aux[-1][1])

    for i in range(num_iterations):
        list_aux.append(step_gradient((list_aux[-1])[0], (list_aux[-1])[1], data, alpha))
        list_theta0.append(list_aux[-1][0])
        list_theta1.append(list_aux[-1][1])

    return list_theta0, list_theta1
