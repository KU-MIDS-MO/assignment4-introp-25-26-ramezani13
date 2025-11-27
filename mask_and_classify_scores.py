import numpy as np

def mask_and_classify_scores(arr):
    if type(arr) != np.ndarray:
        return None

    if arr.ndim != 2:
        return None

    rows = arr.shape[0]
    cols = arr.shape[1]

    if rows != cols:
        return None
    if rows < 4:
        return None
###
    cleaned = arr.copy()

    mask_neg = cleaned < 0
    cleaned[mask_neg] = 0

    mask_big = cleaned > 100
    cleaned[mask_big] = 100
###
    levels = np.zeros_like(cleaned, dtype=int)

    mask_low = cleaned < 40
    mask_med = (cleaned >= 40) & (cleaned < 70)
    mask_high = cleaned >= 70

    levels[mask_low] = 0
    levels[mask_med] = 1
    levels[mask_high] = 2
####
    pass_mask = cleaned >= 50

    row_counts = []
    i = 0
    while i < rows:
        count = 0
        j = 0
        while j < cols:
            if pass_mask[i, j]:
                count += 1
            j += 1
        row_counts.append(count)
        i += 1

    row_pass_counts = np.array(row_counts)

    return cleaned, levels, row_pass_counts
