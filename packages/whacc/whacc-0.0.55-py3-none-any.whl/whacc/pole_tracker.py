# -*- coding: utf-8 -*-
"""COMPILE pole_tracker_for_phil_ V_1.2.0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jR9Q1z4fIQY37rCOUgWUx8WyBO_lo_Zx
"""

import os
import glob

import cv2
import numpy as np
import time
import re
import h5py
import matplotlib.pyplot as plt
from functools import partial
from tqdm import tqdm
from PIL import Image
from whacc.image_tools import h5_iterative_creator

# import pdb
# from whacc import utils

tqdm = partial(tqdm, position=0, leave=True)

################### drive.mount('/content/gdrive')

# sorts the videos the way the OS does, this way the files will be in the ocrrect order
# import pkg_resources
# pkg_resources.require("natsort==7.1.1")
import natsort
# !pip install natsort==7.1.1 # this version has "os_sorted"
# !pip install pyicu # needed to make sure the sorting is correct (strong recommend in the documentation)
from natsort import os_sorted

"""## Build Class for template and frame matching

"""


class PoleTracking():

    def __init__(self, video_directory, template_png_full_name=None, use_narrow_search_to_speed_up=False):
        """

        Parameters
        ----------
        video_directory : str
            full path to the directory with MP4s
        template_png_full_name : numpy array
            template image HxWx3 (can be left blank and use method "cut_out_pole_template" to make a new template and use
            "save_template_img" method to save the template image
        use_narrow_search_to_speed_up : bool
            used to make pole tracker faster. after finding the first frame, it searches in a limited space around that
            frame. based on "inflation" variable in "crop_image_from_top_left" method below
        """
        self.video_directory = video_directory
        self.video_files = os_sorted(glob.glob(os.path.join(video_directory, '*.mp4')))
        self.base_names = [os.path.basename(n).split('.')[0] for n in self.video_files]
        self.use_narrow_search_to_speed_up = use_narrow_search_to_speed_up
        if template_png_full_name is not None:
            self.load_template_img(template_png_full_name)

    @staticmethod
    def crop_image_from_top_left(im, crop_top_left, size_crop, inflation=1):
        """This is an accessory function to track to improve tracking speed. This crops the initial large image into a smaller one, based on the inflation rate.
        Inflation rate of 3 = 3 x 3 template image size around the first guessed pole location.

        Parameters
        ----------
        im :
            
        crop_top_left :
            
        size_crop :
            
        inflation :
             (Default value = 3)

        Returns
        -------

        """
        inflation_shift = np.floor((np.asarray(size_crop) * (inflation - 1)) / 2).astype(int)

        size_crop = np.asarray(size_crop) * inflation
        imshape = np.asarray(im.shape[:2])

        # adjust for inflation and make copies of origianl crop inds
        crop_top_left = crop_top_left - inflation_shift
        crop_top_left2 = crop_top_left.copy()
        crop_bottom_right = crop_top_left + np.asarray(size_crop)
        crop_bottom_right2 = crop_bottom_right.copy()

        # adjust crop in case of out of bounds
        crop_top_left[crop_top_left < 0] = 0
        crop_bottom_right[crop_bottom_right > imshape] = np.asarray(imshape)[crop_bottom_right > imshape]

        # for placing cropped image in random noise image tensor (we do this in case of out of bounds issues all outputs are the same size)
        TL_adj = crop_top_left - crop_top_left2

        c_cropped = im[crop_top_left[0]:crop_bottom_right[0], crop_top_left[1]:crop_bottom_right[1], ...].astype(
            'uint8')

        # make random noise image tensor
        crop_dim = list(c_cropped.shape)
        crop_dim[:2] = size_crop.tolist()
        cropped_image = np.random.randint(256, size=crop_dim).astype('uint8')

        if len(crop_dim) > 2:  # crop 3D or more
            cropped_image[TL_adj[0]:TL_adj[0] + c_cropped.shape[0], TL_adj[1]:TL_adj[1] + c_cropped.shape[1],
            ...] = c_cropped
        else:  # crop 2D
            cropped_image[TL_adj[0]:TL_adj[0] + c_cropped.shape[0],
            TL_adj[1]:TL_adj[1] + c_cropped.shape[1]] = c_cropped

        return cropped_image, crop_top_left2, crop_bottom_right2

    def plot_pole_center(self, video_file, location_stack):
        """

        Parameters
        ----------
        video_file :
            
        location_stack :
            

        Returns
        -------

        """
        video = cv2.VideoCapture(video_file)
        success, frame = video.read()
        location_stack = location_stack + np.array(self.template_image.shape) / 2
        _ = plt.figure()
        plt.imshow(frame)
        plt.scatter(location_stack[:, 0], location_stack[:, 1], s=.2, c='r')
        plt.show()

        threshold = 50  # threshold in pixels
        distance_from_mean = np.sum(np.abs(location_stack - np.mean(location_stack, axis=0)), axis=1)
        exceed_threshold = np.mean(distance_from_mean < threshold) * 100
        print(str(np.round(exceed_threshold, 2)) + '% of the pole locations are within ' + str(
            threshold) + ' pixels from the mean pole location.')

    def track_random(self) -> object:
        """This function will randomly grab a video file within the directory and
        track all frames within there and plot tracked locations over the original image

        Parameters
        ----------

        Returns
        -------

        """
        video_file = np.random.choice(self.video_files, 1)[0]
        print('Testing tracking on ' + video_file)
        img_stack, loc_stack, max_val_stack = self.track(video_file=video_file)
        self.plot_pole_center(video_file=video_file, location_stack=loc_stack)

    def get_trial_and_file_names(self, pos_seps='-_', custom_trial_nums=None, custom_ascii_video_files=None,
                                 print_them=False, num_to_print=None):
        """pos_seps - (default = '-_') will find the number after the last of '-' or '_', can add custom notion for your naming scheme
        custom_trial_nums - override in case this is needed, list of strings equal to length of number of MP4 files (e.g. ['9', '10', '11'])
        custom_ascii_video_files - override in case this is needed, list of full file names (without base directory) must be ASCII format for saving in H5 file later
        to convert LIST (list of strings) to ASCII us -> ASCII_LIST = [os.path.basename(n).encode("ascii", "ignore") for n in LIST]
        print_them - just used to print the names to make sure the naming is what you want before spending all the time tracking.
        num_to_print - if print_them == True, this will print the first N number of files (used in case you are doing a huge amount
        of videos from many directories, we dont want to overload the terminal window)

        Parameters
        ----------
        pos_seps :
             (Default value = '-_')
        custom_trial_nums :
             (Default value = None)
        custom_ascii_video_files :
             (Default value = None)
        print_them :
             (Default value = False)
        num_to_print :
             (Default value = None)

        Returns
        -------

        """
        print(self.video_files[0])
        trial_sep = [k for k in self.video_files[0] if k in pos_seps][-1]  # '-_' are the possible separators
        self.trial_sep = trial_sep
        save_base_name = os.path.basename(self.video_files[0]).split(self.trial_sep)
        self.save_base_name = '-'.join(save_base_name[:-1])
        if custom_trial_nums is None:
            self.trial_nums = list(
                map(lambda s: re.search("^.*" + trial_sep + "([0-9]+)\.", s).group(1), self.video_files))
        else:
            self.trial_nums = custom_trial_nums

        if custom_ascii_video_files is None:
            self.ascii_video_files = [os.path.basename(n).encode("ascii", "ignore") for n in self.video_files]
        else:
            self.ascii_video_files = custom_ascii_video_files

        if print_them:  # print the files and trial nums to make sure they are sorted and match and what the user expects
            print(*['FILE->' + os.path.basename(k1).split('.')[0] + '  ' + k2 + '<-TRIAL#' for k1, k2 in
                    zip(self.video_files[:num_to_print], self.trial_nums[:num_to_print])], sep='\n')

    def track_all_and_save(self, verbose=False, save_directory=None):
        """

        Parameters
        ----------
        verbose :
             (Default value = False)
        save_directory :
             (Default value = None)

        Returns
        -------

        """
        if save_directory is None:
            save_directory = self.video_directory
        save_directory = save_directory + os.path.sep

        """
        This is the major output function of the PoleTracking class. This functions will 
        track all video files within the directory and save an H5 file with the meta information:
        - file_name_nums : this is the trial number extracted from the video file name
        - image: the tracked image stack
        - labels : this is pre-allocation for the CNN to label the images
        - trial_nums_and_frame_nums: 2 dimensional vector. Row 1 = trial number and Row 2 = frame number in that trial
        - in_range: this is pre-allocation for the pole in range tracker
        """
        loc_stack_all = np.asarray([])
        max_val_stack_all = np.asarray([])
        # get the video names and trial numbers -- this is a sperate function
        # so that you can run it before you process the videos to see if the
        # naming and numbers are correct. can run PT.get_trial_and_file_names(True)
        # to print out the file lists before you run everyhting to check.
        if 'ascii_video_files' not in [k for k in dir(self) if '_' not in k[0]]:
            self.get_trial_and_file_names()
        # save data in H5 with name similar to video
        file_name = self.save_base_name + '.h5'
        # create image stack
        final_stack = []
        len_all = 0
        start = time.time()
        h5creator = h5_iterative_creator(save_directory + file_name,
                                         overwrite_if_file_exists=True,
                                         max_img_height=self.template_image.shape[0],
                                         max_img_width=self.template_image.shape[1],
                                         close_and_open_on_each_iteration=False)
        print("Don't worry it will close automatically once finished ")
        for video in tqdm(self.video_files):
            if verbose: print('Tracking... ' + video)
            img_stack, loc_stack, max_val_stack = self.track(video_file=video)
            neg_1_filler_labels = np.float64(np.ones(img_stack.shape[0]) * -1)
            h5creator.add_to_h5(img_stack, neg_1_filler_labels)
            # loc_stack_all.append(loc_stack)
            loc_stack_all = np.vstack((loc_stack_all, loc_stack)) if len(loc_stack_all)!=0 else loc_stack
            # max_val_stack_all.append(max_val_stack)
            max_val_stack = np.asarray(max_val_stack)
            max_val_stack_all = np.hstack((max_val_stack_all, max_val_stack)) if len(max_val_stack_all)!=0 else max_val_stack
            len_all += img_stack.shape[0]
        h5creator.close_h5()

        #  frame numbers
        frame_nums = list(map(lambda s: cv2.VideoCapture(s).get(7), self.video_files))

        tnf = np.vstack([np.array(list(self.trial_nums)).astype(int),
                         np.array(list(frame_nums))])

        # populating which trial each frame is in
        fnn = []
        for a, b in zip(list(self.trial_nums), list(frame_nums)):
            fnn = np.concatenate([fnn, np.repeat(int(a), b)])

        # populating whether pole "in_range" with nan values
        in_range = np.empty(len_all)
        in_range[:] = np.nan

        # check to make sure sizes across file names and images are equal
        assert len(fnn) == len_all, '''the fnn and length of frames don't match '''

        with h5py.File(save_directory + file_name, 'r+') as hf:  # with -> auto close in case of failure
            hf.create_dataset('locations_x_y', data=loc_stack_all)
            hf.create_dataset('max_val_stack', data=max_val_stack_all)
            hf.create_dataset('file_name_nums', data=fnn)
            hf.create_dataset('trial_nums_and_frame_nums', data=tnf)
            hf.create_dataset('in_range', data=in_range)
            hf.create_dataset('full_file_names', data=self.ascii_video_files)
            hf.create_dataset('frame_nums', tnf[1, :])
            hf.close()

        print('H5 file saving under the name ' + file_name)
        print('and placed in ' + save_directory)
        elapsed = time.time() - start
        print('Tracker runtime : ' + str(elapsed / 60) + ' mins')
        return save_directory + file_name

    def track(self, video_file, match_method='cv2.TM_CCOEFF'):
        """this function scans a template image across each frame of the video to identify the pole location.
        This assumes there is a pole at each frame. Cropping optimizes scanning by ~80% and uses the first frame
        as a point of reference.

        Parameters
        ----------
        video_file :

        match_method :
             (Default value = 'cv2.TM_CCOEFF')

        Returns
        -------

        """

        # width and height of img_stacks will be that of template (61x61)
        w, h = self.template_image.shape[::-1]
        max_match_val = []
        # open video at directory
        video = cv2.VideoCapture(video_file)
        if (video.isOpened() == False):
            print('error opening video file')

        fno = 0
        img_list = []
        loc_list = []
        success, og_frame = video.read()
        method = eval(match_method)
        crop_top_left = 0
        pole_center = 0
        tmp1 = 0
        while success:
            # preprocess image
            tmp1 = tmp1 + 1
            if 'frame' in locals() and self.use_narrow_search_to_speed_up:
                frame, crop_top_left, crop_bottom_right = self.crop_image_from_top_left(og_frame,
                                                                                        crop_top_left2,
                                                                                        [w, h],
                                                                                        3)
            else:
                frame = og_frame
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype('uint8').copy()

            # Apply template Matching
            res = cv2.matchTemplate(img, self.template_image, method)
            min_val, max_val, min_loc, top_left = cv2.minMaxLoc(res)
            max_match_val.append(max_val)
            top_left = np.flip(np.asarray(top_left))

            # crop image and store
            crop_img, crop_top_left2, crop_bottom_right2 = self.crop_image_from_top_left(og_frame,
                                                                                         top_left + crop_top_left,
                                                                                         [w, h])
            img_list.append(crop_img)
            loc_list.append(np.flip(crop_top_left2))

            # iterate to next frame and crop using current details
            fno += 1
            success, og_frame = video.read()

        img_stack = np.array(img_list, dtype=np.uint8)
        loc_stack = np.array(loc_list)
        return img_stack, loc_stack, max_match_val

    def set_pole_template(self, cust_template):
        """custom template: input must be the 2D matrix (no color channels) and dtype=uint8

        Parameters
        ----------
        cust_template :
            

        Returns
        -------

        """
        self.template_image = cust_template

    def save_template_img(self, cust_save_dir='', cust_save_name='template_img'):
        """save current template image to use for similar session

        Parameters
        ----------
        cust_save_dir :
             (Default value = '')
        cust_save_name :
             (Default value = 'template_img')

        Returns
        -------

        """
        img = Image.fromarray(self.template_image, 'L')
        full_save_name = cust_save_dir + os.path.sep + cust_save_name + '.png'
        img.save(full_save_name)
        print('SAVED... ' + full_save_name)

    def load_template_img(self, img_to_load):
        """

        Parameters
        ----------
        img_to_load :
            

        Returns
        -------

        """
        self.template_image = np.asarray(Image.open(img_to_load))

    def cut_out_pole_template(self, crop_size=[61, 61], frame_num=2000, file_ind=None):
        """

        Parameters
        ----------

        crop_size :
             (Default value = [61)
        61] :
            
        frame_num :
             (Default value = 2000)
        file_ind :
             (Default value = None)

        Returns
        -------

        """
        top_left = str(crop_size[0]) + ' , ' + str(crop_size[1])
        crop_size = np.asarray(crop_size)
        if file_ind is None:
            video_file = np.random.choice(self.video_files, 1)[0]
        else:
            video_file = self.video_files[file_ind]
        plt.ion()
        plt.show()
        change_trig = True
        while 'exit' not in str(top_left).lower():
            if 'skip' in str(top_left).lower():
                video_file = np.random.choice(self.video_files, 1)[0]
                print('Randomly selecting a new video...')
            try:
                top_left = eval('[' + top_left + ']')
                if change_trig:
                    top_left = top_left - np.floor(crop_size / 2).astype('int')
                else:
                    change_trig = True
                print('Sampling video file ' + video_file.split('/')[-1])
                video = cv2.VideoCapture(video_file)
                tmp_fig = plt.figure(figsize=[6, 6])
                video.set(1, frame_num)
                _, frame = video.read()

                plt.imshow(frame)

                tmp_img, a, b = self.crop_image_from_top_left(frame, top_left, crop_size)
                template_image = tmp_img.copy()
                crop_size_2 = np.floor(crop_size / 2).astype('int')
                tmp_img[crop_size_2[0], :] = 0
                tmp_img[:, crop_size_2[1]] = 0

                _ = plt.subplot(122)
                _ = plt.imshow(tmp_img, extent=[top_left[1], tmp_img.shape[1] + top_left[1],
                                                tmp_img.shape[0] + top_left[0], top_left[0]])
                ax = plt.gca()
                ax.set_yticks(np.arange(top_left[0] + .5, top_left[0] + tmp_img.shape[0], 5), minor=True)
                ax.set_xticks(np.arange(top_left[1] + .5, top_left[1] + tmp_img.shape[1], 5), minor=True)

                plt.grid(which='minor', color='red', linestyle='-', linewidth=.2)
                frame2 = frame.copy()
                try:
                    frame2[a[0], :] = 0
                    frame2[b[0], :] = 0
                    frame2[:, a[1]] = 0
                    frame2[:, b[1]] = 0
                except:
                    print('partially out of range not plotting crosshairs on zoomed out image')
                _ = plt.subplot(121)
                _ = plt.imshow(frame2)
                ax = plt.gca()
                ax.set_yticks(np.arange(1, frame2.shape[0], 50), minor=True)
                ax.set_xticks(np.arange(1, frame2.shape[1], 50), minor=True)
                plt.grid(which='minor', color='red', linestyle='-', linewidth=.2)

                tmptop_left = top_left.copy()
                U_in_2_print = top_left + np.floor(crop_size / 2).astype('int')
                plt.draw()
                plt.pause(0.01)
                plt.show()
                top_left = input('Input the pole center coordinates seperated by a comma \ny (0 = top, max = bottom) '
                                 '\nx (0 = left, max = right) \nor enter "exit" to finalize image selection '
                                 '\nor enter "exit all" to terminate the while loop'
                                 '\nor enter "skip" to choose another random video' + '\nlast selection --> '
                                 + str(U_in_2_print[0]) + ' , ' + str(
                    U_in_2_print[1]) + '\n______________________________________________________\n')
                plt.close(tmp_fig)
                if 'exit all' == str(top_left).lower():
                    assert False, 'user exited the program'
            except:
                if 'exit all' == str(top_left).lower():
                    assert False, 'user exited the program'
                if str(top_left).lower() != 'skip':
                    print(
                        'oops try again enter a pair of numbers or enter exit to finish select... or maybe you entered an out of range pair of numbers')
                top_left = tmptop_left.copy()
                top_left = str(top_left[0]) + ' , ' + str(top_left[1])
                change_trig = False

        self.template_image = template_image[:, :, 0]




