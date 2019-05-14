import os, sys, os.path as osp
import gen_utils


def evaluate(feature_dir, prefix, result_dir, settings):
    """to evaluate and rank results for SYSU_MM01 dataset
    
    Arguments:
        feature_dir {str} -- a dir where features are saved
        prefix {str} -- prefix of file names
        result_dir {str} -- a directory to save results
    """
    gallery_cams, probe_cams = gen_utils.get_cam_settings(settings)
    all_cams = list(set(gallery_cams + probe_cams))  # get unique cams
    features = {}

    for cam_index in all_cams:
        # read features
        cam_feature_file = osp.join(feature_dir, (prefix + '_cam{}').format(cam_index))
        features[cam_index] = gen_utils.load_feature_file(cam_feature_file)


if __name__ == "__main__":
    feature_dir = "../../../scratch/sysu_mm01/deepzeropadding-14May2019-125214_deep-zero-padding/deep_zero_model#21"
    prefix = "deep_zero_model#21"
    result_dir = "./result"

    # evaluation settings
    settings = {}
    settings["mode"] = "indoor"  # indoor | all
    settings["number_shot"] = 1  # 1 = single-shot | 10 = multi-shot
    evaluate(feature_dir, prefix, result_dir, settings)
