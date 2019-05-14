import os, sys
import numpy as np
from scipy.spatial.distance import cdist


def euclidean_dist(X_gallery, X_probe):
    return cdist(X_gallery, X_probe)


def get_cam_settings(settings):
    if settings["mode"] == "indoor":
        return [1, 2], [3, 6]
    elif settings["mode"] == "all":
        return [1, 2, 4, 5], [3, 6]
    else:
        assert False, "unknown search mode : " + settings["mode"]


def get_test_ids():
    test_id_filepath = "./data_split/test_id.mat"


def get_cam_permutation_samples():
    rand_cam_perm_filepath = "./data_split/rand_perm_cam.mat"


def get_cmc_multi_cam(Y_gallery, Y_cam_gallery, Y_probe, Y_cam_probe, dist):
    pass
