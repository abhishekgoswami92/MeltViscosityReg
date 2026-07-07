import numpy as np
from scipy.optimize import curve_fit

def carreau_yasuda(omega, eta0, lam, n, a):
    return eta0 * (1 + (lam * omega)**a)**((n - 1) / a)


def fit_carreau_yasuda(omega, eta):
    # Initial guesses
    eta0_guess = np.max(eta)
    lam_guess = 1.0
    n_guess = 0.5
    a_guess = 2.0

    p0 = [eta0_guess, lam_guess, n_guess, a_guess]

    # Bounds (important!)
    bounds = (
        [1e-3, 1e-6, 0.0, 0.1],   # lower
        [1e8, 1e6, 1.0, 10.0]     # upper
    )

    # Fit in log space for stability
    def log_model(omega, eta0, lam, n, a):
        return np.log(carreau_yasuda(omega, eta0, lam, n, a))

    params, covariance = curve_fit(log_model,omega,np.log(eta),p0=p0,bounds=bounds,maxfev=20000)
    return np.array(params)  # [eta0, lambda, n, a]

def to_feature_vector(params):
    return np.log(params)

def CY_to_feature_vector(params):
    eta0, lam, n, a = params
    return np.array([
        np.log(eta0*1000),   # log: spans many decades
        np.log(lam),    # log: relaxation time, also wide range
        n,              # linear: already 0–1
        a,              # linear: shape exponent, no log needed
    ])

def estimate_x_from_features(A_feat, B_feat, T_feat):
    AB = B_feat - A_feat
    AT = T_feat - A_feat

    numerator = np.dot(AT, AB)
    denominator = np.dot(AB, AB)

    if denominator == 0:
        return None

    x = numerator / denominator
    return np.clip(x, 0, 1)  # enforce physical bounds


