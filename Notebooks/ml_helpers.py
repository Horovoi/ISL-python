
# This is a collection of functions that I have written to help me with ML tasks

def my_formula(df, y, x_drop = None):
    """
    This function takes a dataframe and a string as input and returns a formula for use with statsmodels

    df: dataframe
    y: string, name of the target variable
    x_drop: list of strings, names of variables to be dropped from the formula
    
    returns: a formula for use with statsmodels
    """
    if x_drop is None:
        x_drop = [y]
    elif type(x_drop) == str:
        x_drop = [x_drop]
        x_drop.append(y)
    else:
        x_drop.append(y)
    
    return y + ' ~ ' + ' + '.join([x for x in df.columns if x not in x_drop])