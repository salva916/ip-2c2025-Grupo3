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
