
# merge_sort_step.py
# Merge Sort paso a paso compatible con template GitHub

items = []
n = 0
stack = []

def init(vals):
    global items, n, stack
    items = list(vals)
    n = len(items)
    stack = []

    if n <= 1:
        return

    stack.append({
        "l": 0, "r": n - 1,
        "stage": "call_left",
        "mid": None,
        "temp": [],
        "i": None, "j": None, "k": None
    })

def step():
    global items, stack

    if not stack:
        return {"done": True}

    f = stack[-1]

    if f["mid"] is None:
        f["mid"] = (f["l"] + f["r"]) // 2

    if f["stage"] == "call_left":
        if f["l"] < f["mid"]:
            f["stage"] = "call_right"
            stack.append({
                "l": f["l"], "r": f["mid"],
                "stage": "call_left",
                "mid": None,
                "temp": [],
                "i": None, "j": None, "k": None
            })
            return {"a": f["l"], "b": f["mid"], "swap": False, "done": False}
        else:
            f["stage"] = "call_right"

    if f["stage"] == "call_right":
        if f["mid"] + 1 < f["r"]:
            f["stage"] = "merge"
            stack.append({
                "l": f["mid"] + 1, "r": f["r"],
                "stage": "call_left",
                "mid": None,
                "temp": [],
                "i": None, "j": None, "k": None
            })
            return {"a": f["mid"] + 1, "b": f["r"], "swap": False, "done": False}
        else:
            f["stage"] = "merge"

    if f["stage"] == "merge":
        f["temp"] = []
        f["i"] = f["l"]
        f["j"] = f["mid"] + 1
        f["stage"] = "merge_loop"

    if f["stage"] == "merge_loop":
        if f["i"] <= f["mid"] and f["j"] <= f["r"]:
            a, b = f["i"], f["j"]
            if items[a] <= items[b]:
                f["temp"].append(items[a])
                f["i"] += 1
            else:
                f["temp"].append(items[b])
                f["j"] += 1
            return {"a": a, "b": b, "swap": False, "done": False}

        if f["i"] <= f["mid"]:
            f["temp"].append(items[f["i"]])
            old = f["i"]
            f["i"] += 1
            return {"a": old, "b": old, "swap": False, "done": False}

        if f["j"] <= f["r"]:
            f["temp"].append(items[f["j"]])
            old = f["j"]
            f["j"] += 1
            return {"a": old, "b": old, "swap": False, "done": False}

        if f["k"] is None:
            f["k"] = f["l"]

        if f["k"] <= f["r"]:
            src_idx = f["k"] - f["l"]
            a = f["k"]
            items[f["k"]] = f["temp"][src_idx]
            f["k"] += 1
            return {"a": a, "b": a, "swap": True, "done": False}

        f["stage"] = "done"

    if f["stage"] == "done":
        stack.pop()
        return {"done": False, "a": 0, "b": 0, "swap": False}

    return {"done": True}
