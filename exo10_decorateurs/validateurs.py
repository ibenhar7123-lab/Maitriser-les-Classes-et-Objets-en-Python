import functools


def valider_positif(*indices: int):
    """Décorateur qui valide que les arguments aux indices donnés sont positifs.
    Attention : l'index 0 correspond à self pour une méthode."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for idx in indices:
                if idx < len(args):
                    value = args[idx]
                    if not isinstance(value, (int, float)) or value <= 0:
                        raise ValueError(f"L'argument à l'index {idx} doit être un nombre positif.")
            return func(*args, **kwargs)
        return wrapper
    return decorator
