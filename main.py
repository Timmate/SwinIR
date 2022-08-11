if __name__ == '__main__':
    import os
    MODE = 'real'
    # MODE = 'classical'
    SCALE = 4
    if MODE == 'real':
        if SCALE == 2:
            os.system('python SwinIR/main_test_swinir.py '
                      '--task real_sr '
                      '--model_path SwinIR/experiments/pretrained_models/003_realSR_BSRGAN_DFO_s64w8_SwinIR-M_x2_GAN.pth '
                      '--folder_lq /home/tim/Downloads/swinir/input '
                      '--output_folder /home/tim/Downloads/swinir/output '
                      '--show_progress '
                      '--scale 2 ')
        elif SCALE == 4:
            os.system('python SwinIR/main_test_swinir.py '
                      '--task real_sr '
                      # '--model_path SwinIR/experiments/pretrained_models/003_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR-L_x4_GAN.pth '
                      '--model_path SwinIR/experiments/pretrained_models/003_realSR_BSRGAN_DFO_s64w8_SwinIR-M_x4_GAN.pth '
                      '--folder_lq /home/tim/Downloads/swinir/input '
                      '--output_folder /home/tim/Downloads/swinir/output '
                      '--show_progress '
                      '--scale 4 '
                      # '--large_model'
                      )
        else:
            raise Exception
    else:
        if SCALE == 2:
            os.system('python SwinIR/main_test_swinir.py '
                      '--task classical_sr '
                      '--model_path experiments/pretrained_models/001_classicalSR_DF2K_s64w8_SwinIR-M_x2.pth '
                      '--folder_lq /home/tim/Downloads/swinir/input '
                      '--output_folder /home/tim/Downloads/swinir/output '
                      '--show_progress '
                      '--scale 2 '
                      '--training_patch_size 64')
        elif SCALE == 4:
            os.system('python SwinIR/main_test_swinir.py '
                      '--task classical_sr '
                      '--model_path experiments/pretrained_models/001_classicalSR_DF2K_s64w8_SwinIR-M_x4.pth '
                      '--folder_lq /home/tim/Downloads/swinir/input '
                      '--output_folder /home/tim/Downloads/swinir/output/ '
                      '--show_progress '
                      '--scale 4 '
                      '--training_patch_size 64')
        else:
            raise Exception

