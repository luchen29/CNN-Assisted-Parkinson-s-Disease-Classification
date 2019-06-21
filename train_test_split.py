"""
Split files into training and test sub-directories
"""

import os
import shutil
from glob import glob
import random


def shuffle2(data):
    data2 = data[:]
    random.shuffle(data2)
    return data2

def get_subdirs(base_dir):
    return [i for i in glob(base_dir + "/*/") if os.path.isdir(i)]


def get_orig_struct(base_dir):
    assert os.path.isdir(base_dir)
    sub_dirs = get_subdirs(base_dir)
    original_structure = {subd: os.listdir(subd) for subd in sub_dirs}
    return original_structure


def make_train_test_dict(orig_struct_dict, test_prop):
    assert isinstance(orig_struct_dict, dict)
    new_struct = {"train": {}, "test": {}}
    for key, value in orig_struct_dict.items():
        train_dat, test_dat = train_test_split(data=value, test_prop=test_prop)
        new_struct["train"].update({key: train_dat})
        new_struct["test"].update({key: test_dat})
    return new_struct


def train_test_split(data, test_prop):
    n_test = round(len(data) * test_prop)
    n_train = len(data) - n_test
    data = shuffle2(data)
    train = data[:n_train]
    test = data[-n_test:]
    assert len(train) + len(test) == len(data)
    return train, test


def get_label(filename):
    return os.path.basename(os.path.normpath(filename))


def check_dir(filename):
    subdir_path = os.path.dirname(filename)
    try:
        os.makedirs(subdir_path)
    except OSError:
        if os.path.isdir(subdir_path):
            pass
        else:
            err_msg = "failed to create directory {}".format(subdir_path)
            raise RuntimeError(err_msg)


def create_path_lists(source, destination, test_prop):
    orig_struct = get_orig_struct(base_dir=source)
    train_test_dict = make_train_test_dict(orig_struct, test_prop)
    

    original_path = []
    new_path = []
    for tt, subdict in train_test_dict.items():
        for class_labels, files in subdict.items():
            orig = [os.path.join(class_labels, i) for i in files]
            dest = [os.path.join(destination, tt, get_label(class_labels), i) for i in files]
            original_path.extend(orig)
            new_path.extend(dest)
    return original_path, new_path


def train_test_split_dir(source, destination, test_prop=0.3):
    original_paths, new_paths = create_path_lists(source=source, destination=destination, test_prop=test_prop)
    for i, j in zip(original_paths, new_paths):
        check_dir(j) 
        shutil.copy2(i, j)
