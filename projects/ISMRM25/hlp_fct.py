import os


def get_data_path(work_locally=False):
    if work_locally:
        data_path = "C:\\Users\\Hendrik Mattern\\Downloads\\ismrm25_nii"
    else:
        data_path = "Y:\\Projects\\ISMRM25_EPI_MREG\\nii"
    return data_path