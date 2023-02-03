from asyncio.windows_events import NULL
from doctest import OutputChecker
from turtle import color
import torch

import posenet

model = posenet.load_model(101)
model = model.cuda()
output_stride = model.output_stride

def Capture(cap):
    input_image, display_image, output_scale = posenet.read_cap(
            cap, scale_factor=0.7125, output_stride=output_stride)

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
            min_pose_score=0.15)

    keypoint_coords *= output_scale

    # TODO this isn't particularly fast, use GL for drawing and display someday...
    overlay_image = posenet.draw_skel_and_kp(
        display_image, pose_scores, keypoint_scores, keypoint_coords,
        min_pose_score=0.15, min_part_score=0.1)
    return overlay_image, keypoint_coords[0]