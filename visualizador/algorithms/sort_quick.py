phase = "idle"      # idle, partitioning, pushing
low = 0             # Inicio del rango actual
high = 0            # Fin del rango actual
def init(vals):
    global items, length, stack, i, j, pivot, phase, low, high
    items = list(vals)
    length = len(items)
    stack = []
    if length > 1:
        stack.append((0, length - 1))  # Primer rango
    phase = "idle"
    i = 0
    j = 0
    pivot = None
    low = 0
    high = 0
def step():
    global items, length, stack, i, j, pivot, phase, low, high
    # Si no hay rangos pendientes y estamos en idle, terminamos
    if not stack and phase == "idle":
        return {"done": True}
    # Inicializar rango si estamos en idle
    if phase == "idle":
        if not stack:
            return {"done": True}
        low, high = stack.pop()
        if low >= high:
            # Rango trivial, continuar
            return {"a": 0, "b": 0, "swap": False, "done": False}
        pivot = items[high]  # Pivote: último elemento
        i = low - 1
        j = low
        phase = "partitioning"
 # Fase de partición: paso a paso
    if phase == "partitioning":
        if j <= high - 1:
            swap = False
            a = j
            b = j  # Por defecto, b es j (para mostrar movimiento)
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
                swap = True
                b = i  # Mostrar el swap con i
            j += 1
            return {"a": a, "b": b, "swap": swap, "done": False}
        else:
            # Colocar pivote en su lugar
            items[i + 1], items[high] = items[high], items[i + 1]
            phase = "pushing"
            return {"a": i + 1, "b": high, "swap": True, "done": False}
    # Fase de pushing: empujar subrangos (un paso por subrango)
    if phase == "pushing":
        pivot_index = i + 1
        # Subrango izquierdo
        if low < pivot_index:
            stack.append((low, pivot_index - 1))
        # Subrango derecho
        if pivot_index + 1 < high:
            stack.append((pivot_index + 1, high))
        phase = "idle"
        return {"a": 0, "b": 0, "swap": False, "done": False}
    return {"done": True}
