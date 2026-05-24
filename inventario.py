"""
Para desarrollar el problema del inventario.

"""

from MDPs import MDP, iteracion_valor

class Inventario(MDP):
    """
    Clase que representa un MDP para el problema del camión mágico.
    
    Si caminas, avanzas 1 con coso 1
    Si usas el camion, con probabilidad rho avanzas el doble de donde estabas
    y con probabilidad 1-rho te quedas en el mismo lugar. Todo con costo 2.
    
    El objetivo es llegar a la meta en el menor costo posible
    
    """    
    
    def __init__(self, gama, lambda_):
        # inicializamos el descuento y la media de la demanda
        self.gama = gama
        self.gamma = gama # por compatibilidad
        self.lambda_ = lambda_
        
        # los estados van desde el backlog maximo (-10) hasta la capacidad (20)
        self.estados = tuple(range(-10, 21))
        
        # los costos y precios para las recompensas
        self.precio_venta = 150.0
        self.costo_compra = 80.0
        self.costo_fijo_pedido = 40.0
        self.costo_almacenamiento = 5.0
        self.costo_backlog = 15.0
        self.perdida_oportunidad = 70.0 # margen de venta perdido (150 - 80)
        
        # se precalculan las probabilidades de poisson de la demanda de 0 a 50
        import math
        self.probs_poisson = {}
        for k in range(51):
            self.probs_poisson[k] = (math.exp(-self.lambda_) * (self.lambda_**k)) / math.factorial(k)
    
    def acciones_legales(self, s):
        #TODO: Completar este método
        pass
    
    def recompensa(self, s, a, s_):
        #TODO: Completar este método
        pass
        
    def prob_transicion(self, s, a, s_):
        #TODO: Completar este método
        pass
                
    def es_terminal(self, s):
        #TODO: Completar este método
        pass


if __name__ == "__main__":

    inventario = Inventario(0.9, 0.5, ...)  #TODO:

    pi_star, V = iteracion_valor(inventario, ...) #TODO:

    print("-" * 60)
    print("Estado".center(20) + "Acción".center(20) + "Valor".center(20))
    print("-" * 60 )
    for s in pi_star:
        print(f"{s:^20}{pi_star[s]:^20}{V[s]:^20.2f}")
    print("-" * 60)


"""
Contesta las preguntas aquí mismo (has espacio entre las preguntas):

1. ¿Cómo se comporta las transiciones y las ganancias para casos específicos de $s$ y $a$? 
2. ¿Qué psa si hay mucho almacen? 
3. ¿Que pasa si hay muy poco o estamos sin almacen? 
4. ¿Existe un punto donde la ganancia sea máxima?  
---
5. ¿Cómo se ve la política óptima? ¿Tiene sentido?
6. ¿Como se comporta la función de valor de estado V(s)?
7. ¿Cómo cambiaría la política si la variabilidad de la demanda (lambda) aumenta de 4 a 8?

"""