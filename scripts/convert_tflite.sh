#IMAGE_SIZE_W=288
#IMAGE_SIZE_H=160
#/home/usens/tensorflow/bazel-bin/tensorflow/contrib/lite/toco/toco \
#--input_file=tiny-yolo-obj.pb \
#--input_format=TENSORFLOW_GRAPHDEF \
#--output_format=TFLITE \
#--output_file=tiny-yolo-obj.lite \
#--inference_type=QUANTIZED_UINT8 \
#--input_array=input \
#--output_array=output \
#--input_shape=1,${IMAGE_SIZE_W},${IMAGE_SIZE_H},3 \
#--std_value=127.5 \
#--mean_value=127.5 \
#--default_ranges_min=-128 \
#--default_ranges_max=127 \
#--allow_nudging_weights_to_use_fast_gemm_kernel 

IMAGE_SIZE_W=224
IMAGE_SIZE_H=128
/home/usens/tensorflow/bazel-bin/tensorflow/contrib/lite/toco/toco \
--input_file=tiny-yolo-obj.pb \
--input_format=TENSORFLOW_GRAPHDEF \
--output_format=TFLITE \
--output_file=tiny-yolo-obj_${IMAGE_SIZE_W}_${IMAGE_SIZE_H}.lite \
--inference_type=FLOAT \
--input_array=input \
--output_array=output \
--input_shape=1,${IMAGE_SIZE_W},${IMAGE_SIZE_H},3 \ 
