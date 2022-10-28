from asyncio.windows_events import NULL
from doctest import OutputChecker
import torch
import cv2
import argparse
import os

import posenet

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=int, default=101)
parser.add_argument('--scale_factor', type=float, default=1.0)
parser.add_argument('--notxt', action='store_true')
parser.add_argument('--image_dir', type=str, default='./images')
parser.add_argument('--output_dir', type=str, default='./output')
args = parser.parse_args()

model = posenet.load_model(args.model)
model = model.cuda()
output_stride = model.output_stride

def Capture(*cap):
    input_image, draw_image, output_scale = posenet.read_cap(
            cap, scale_factor=args.scale_factor, output_stride=output_stride)

    with torch.no_grad():
        input_image = torch.Tensor(input_image).cuda()

        heatmaps_result, offsets_result, displacement_fwd_result, displacement_bwd_result = model(input_image)

        pose_scores, keypoint_scores, keypoint_coords = posenet.decode_multiple_poses(
            heatmaps_result.squeeze(0),
            offsets_result.squeeze(0),
            displacement_fwd_result.squeeze(0),
            displacement_bwd_result.squeeze(0),
            output_stride=output_stride,
            max_pose_detections=10,
            min_pose_score=0.25)

    keypoint_coords *= output_scale

    if args.output_dir:
        draw_image = posenet.draw_skel_and_kp(
            draw_image, pose_scores, keypoint_scores, keypoint_coords,
            min_pose_score=0.25, min_part_score=0.25)

        cv2.imwrite(os.path.join(args.output_dir, os.path.relpath(f, args.image_dir)), draw_image)