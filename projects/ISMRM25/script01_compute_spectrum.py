import os
from rainer.src import analyse, io
import hlp_fct

WORK_LOCALLY = True
# define files
data_path = hlp_fct.get_data_path(WORK_LOCALLY)
fn_nii_200ms = os.path.join(data_path, "MR251201_22_hm_ep2d_mreg_fsat_12_200.nii.gz")
fn_nii_250ms = os.path.join(data_path, "MR251201_55_hm_ep2d_mreg_fsat_21_250.nii.gz")

# load
img_200ms, aff_200, hdr_200 = io.load_nii_as_np_array(fn_nii_200ms)
img_250ms, aff_250, hdr_250 = io.load_nii_as_np_array(fn_nii_250ms)

# freq (incl. detrend)
degree_detrend = 2
n_dummy_vols = 100
freq_200ms = analyse.get_frequency_spectrum(img_200ms, tr=200, n_dummy_volumes=n_dummy_vols)
freq_250ms = analyse.get_frequency_spectrum(img_250ms, tr=250, n_dummy_volumes=n_dummy_vols)

# save
io.save_np_array_as_nii(freq_200ms, _, _,
                        os.path.join(data_path, "!MR251201_22_hm_ep2d_mreg_fsat_12_200_freq.nii.gz"))
io.save_np_array_as_nii(freq_200ms, _, _,
                        os.path.join(data_path, "!MR251201_55_hm_ep2d_mreg_fsat_21_250_freq.nii.gz"))

