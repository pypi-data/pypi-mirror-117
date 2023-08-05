""" Flap reconstruction tool.

This uses a ctunet trained model to load a trained model and get the
predictions from it, after preprocessing.
"""
import logging
import os
import os.path as osp
import tempfile

from ..assets.download import DPATH
import SimpleITK as sitk
from SimpleITK import Show as sh
from ctunet.pytorch.train_test import Model

from .. import utilities as common
from ..Preprocessor import prep_img_cr
from ..tools.downloader import Downloader

WORKSPACE_PATH = os.path.expanduser('~/headctools')
DEVICE = 'cuda'


class FlapReconstruction:
    def __init__(self, input_ff, out_path=None, model=None,
                 ext='.nii.gz', show_intermediate=False, skip_prep=False):
        self.model = model
        self.input_ff = input_ff
        self.ext = ext
        self.sh_imgs = show_intermediate
        self.skip_prep = skip_prep

        alt_out_f = osp.join(input_ff, 'reconstructed') if osp.isdir(
            input_ff) else osp.join(osp.split(input_ff)[0], 'reconstructed')
        self.out_folder_path = out_path if out_path else alt_out_f

        self.run()

    def run(self):
        if not os.path.exists(self.input_ff):
            raise FileNotFoundError(f"Input path does not exists. "
                                    f"({self.input_ff})")
        if osp.isdir(self.input_ff):
            self.flaprec_folder(self.input_ff)
        if osp.isfile(self.input_ff):
            self.flaprec_file(self.input_ff)

    def flaprec_folder(self, input_folder):
        common.veri_folder(self.out_folder_path)
        for file in os.listdir(input_folder):
            if file.endswith(self.ext):
                self.flaprec_file(osp.join(input_folder, file))

    def flaprec_file(self, input_file):
        common.veri_folder(self.out_folder_path)
        df = Downloader.get_assets_per_name(self.model)  # Get asset files
        paths = [pth for pth in list(df['path']) if 'model' in pth]
        if len(paths) == 0:
            raise AssertionError(f"The csv for ({self.model}) does not "
                                 f"contain any model path.")
        elif len(paths) > 1:
            logging.info("More than one model path found. The first one will"
                         f"be used ({paths[0]}).")

        # Relative path of the model
        rel_path = paths[0]  # UNet_FlapRec/model/default.pt
        mod_full_path = os.path.join(WORKSPACE_PATH, rel_path)
        if not os.path.exists(mod_full_path):
            print(mod_full_path)
            raise FileNotFoundError("The model was not downloaded or its files"
                                    " are corrupt. Reinstall it by running: "
                                    f"headctools download {self.model}")
        mod, pro_han = rel_path.split(os.sep)[0].split('_')  # UNet, FlapRec

        fname = os.path.split(input_file)[1]  # Input file name
        out_flap = osp.join(self.out_folder_path,
                            fname.replace(self.ext, '_fl' + self.ext))
        out_inputsk = osp.join(self.out_folder_path,
                               fname.replace(self.ext, '_i' + self.ext))
        out_fullsk = osp.join(self.out_folder_path,
                              fname.replace(self.ext, '_sk' + self.ext))

        sh(sitk.ReadImage(input_file), 'input-image') if self.sh_imgs else 0

        # Preprocess
        if self.skip_prep is False:
            # Temp file
            prep_file = tempfile.NamedTemporaryFile(suffix='.nii.gz',
                                                    delete=False)
            prep_file_path = prep_file.name
            prep_file_folder, prep_file_name = os.path.split(prep_file_path)

            prep_img_cr(input_file, out_ff=prep_file_path,
                        image_identifier=None, mask_identifier=None,
                        generate_csv=False, overwrite=False)
            sh(sitk.ReadImage(prep_file_path),
               'prepr-img') if self.sh_imgs else 0

        else:
            prep_file_path = input_file
            prep_file_folder, prep_file_name = os.path.split(prep_file_path)

        # PyTorch model
        params = {
            "name": self.model,
            "test_flag": True,
            "model_class": mod,
            "problem_handler": pro_han,
            "workspace_path": WORKSPACE_PATH,  # It will lookup the model here.
            "single_file": prep_file_path,
            "device": DEVICE,
            "resume_model": mod_full_path,
            "force_resumed": True,  # Don't use the autogenerated model path
        }
        Model(params=params)

        self.model = os.path.splitext(os.path.split(self.model)[1])[0]
        out_folder = 'pred_' + self.model

        pred_flap = os.path.join(prep_file_folder, out_folder,
                                 prep_file_name.replace(self.ext,
                                                        '_fl' + self.ext))
        pred_input = os.path.join(prep_file_folder, out_folder,
                                  prep_file_name.replace(self.ext,
                                                         '_i' + self.ext))
        pred_skull = os.path.join(prep_file_folder, out_folder,
                                  prep_file_name.replace(self.ext,
                                                         '_sk' + self.ext))

        # Sum Skull + Flap
        fl_stk = sitk.ReadImage(pred_flap)
        inp_stk = sitk.ReadImage(pred_input)
        fullsk_stk = sitk.ReadImage(pred_skull)

        sh(fl_stk, 'generated-flap') if self.sh_imgs else 0
        sh(inp_stk, 'input-img') if self.sh_imgs else 0
        sh(fullsk_stk, 'generated-skull') if self.sh_imgs else 0
        sitk.WriteImage(fl_stk, out_flap)
        sitk.WriteImage(inp_stk, out_inputsk)
        sitk.WriteImage(fullsk_stk, out_fullsk)

        prep_file.close() if not self.skip_prep else 0


if __name__ == "__main__":
    FlapReconstruction('/home/fmatzkin/Code/datasets/test_pypi',
                       show_intermediate=True)
