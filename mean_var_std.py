import numpy as np

def calculate(values):
    
    if len(values) != 9:
        raise ValueError("List must contain nine numbers.")

    
    m = np.array(values).reshape(3, 3)

    calculations = {
        "mean": [ 
            m.mean(axis=0).tolist(),
            m.mean(axis=1).tolist(),
            float(m.mean())
            #média
        ],
        'variance': [
            m.var(axis=0).tolist(),
            m.var(axis=1).tolist(),
            float(m.var())
            #variança
        ],
        'standard deviation': [
            m.std(axis=0).tolist(),
            m.std(axis=1).tolist(),
            float(m.std())
            #desvio padrão
        ],
        'max': [
            m.max(axis=0).tolist(),
            m.max(axis=1).tolist(),
            int(m.max())
            #maximo de x,y
        ],
        'min': [
            m.min(axis=0).tolist(),
            m.min(axis=1).tolist(),
            int(m.min())
            #minimo de x e y
        ],
        'sum': [
            m.sum(axis=0).tolist(),
            m.sum(axis=1).tolist(),
            int(m.sum())
            # soma total
        ],
    }

    return calculations

