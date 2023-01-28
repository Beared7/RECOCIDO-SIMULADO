import numpy as np
from matplotlib import pyplot

#def funchion (x):
#    return x**3

#def plot ():
#    limites = (-30,30)
#    x_inputs = np.arange(limites[0], limites[1],0.1)
#    y_inputs = [funchion(x) for x in x_inputs]
#    pyplot.plot(x_inputs, y_inputs,'--')
#    pyplot.show()

class HillClimbing:
    def __init__(self, objetivo, limites, step_size, n_iter):
        """
        """
        self.objetivo = objetivo
        self.limites = limites
        self.step_size = step_size
        self.n_iter = n_iter

    def show(self):
        """
        """
        best, best_eval, soluciones = self.solve()
        print("!Done")
        print("BEST = ",best, best_eval)
        x_inputs = np.arange(self.limites[0], self.limites[1],0.1)
        y_inputs = [self.objetivo(x) for x in x_inputs]
        pyplot.plot(x_inputs, y_inputs,'--')
        pyplot.plot(soluciones,[self.objetivo(x) for x in soluciones],'o',color="black")
        pyplot.show()

    def solve(self):
        soluciones = []
        solucion = np.random.uniform(low=self.limites[0], high=self.limites[1])
        eval = self.objetivo(solucion)
        t=100000
        print("Solucion inicial = ", solucion,eval)
        soluciones.append(solucion)
        while t > 0.5:
            for i in range(self.n_iter):
                vecino = np.random.uniform(low=self.limites[0], high=self.limites[1]) #solucion + np.random.uniform(low=0, high=10) * self.step_size
                eval_v = self.objetivo(vecino)
            if eval_v <= eval or np.exp(-(eval_v - eval)/t):
                solucion, eval = vecino, eval_v
                soluciones.append(solucion)
                print(str(i)+".- x= "+str(solucion)+ " f(x)= "+ str(eval))
            t=t*0.90
        return (solucion,eval, soluciones)