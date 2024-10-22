import os
from src import io
import hlp_fct

WORK_LOCALLY = True
# define files
data_path = hlp_fct.get_data_path(WORK_LOCALLY)
fn_nii_200ms, _, _ = os.path.join(data_path, "MR251201_22_hm_ep2d_mreg_fsat_12_200.nii.gz")
fn_nii_250ms, _, _ = os.path.join(data_path, "MR251201_55_hm_ep2d_mreg_fsat_21_250.nii.gz")

nii_200ms = io.load_nii_as_np_array(fn_nii_200ms)
nii_250ms = io.load_nii_as_np_array(fn_nii_250ms)


