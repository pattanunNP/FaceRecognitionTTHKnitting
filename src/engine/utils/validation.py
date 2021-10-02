import joblib



def check_memory(memory):
    """Check that ``memory`` is joblib.Memory-like.
    joblib.Memory-like means that ``memory`` can be converted into a
    joblib.Memory instance (typically a str denoting the ``location``)
    or has the same interface (has a ``cache`` method).
    Parameters
    ----------
    memory : None, str or object with the joblib.Memory interface
    Returns
    -------
    memory : object with the joblib.Memory interface
    Raises
    ------
    ValueError
        If ``memory`` is not joblib.Memory-like.
    """

    if memory is None or isinstance(memory, str):
        if parse_version(joblib.__version__) < parse_version('0.12'):
            memory = joblib.Memory(cachedir=memory, verbose=0)
        else:
            memory = joblib.Memory(location=memory, verbose=0)
    elif not hasattr(memory, 'cache'):
        raise ValueError("'memory' should be None, a string or have the same"
                         " interface as joblib.Memory."
                         " Got memory='{}' instead.".format(memory))
    return memory