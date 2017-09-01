#!/usr/bin/python
import os

'''
# Extract the features
pos_path = "../data/dataset/pos"
neg_path = "../data/dataset/neg"
os.system("python ../object-detector/extract-features.py -p {} -n {}".format(pos_path, neg_path))
# Perform training
pos_feat_path =  "../data/features/pos"
neg_feat_path =  "../data/features/neg"
os.system("python ../object-detector/train-classifier.py -p {} -n {}".format(pos_feat_path, neg_feat_path))
'''

# Perform testing 
#test_im_path = "../data/dataset/test_image/4.pgm"
test_im_path = "../data/dataset/rebar/3.pgm"
os.system("python ../object-detector/test-classifier.py -i {} --visualize".format(test_im_path))
#os.system("python ../object-detector/polylines_recognition.py -i {} --visualize".format(test_im_path))
#os.system("python ../object-detector/maxvalue_hyper.py -i {} --visualize".format(test_im_path))
#os.system("python ../object-detector/hyperbola_recognition.py -i {} --visualize".format(test_im_path))

