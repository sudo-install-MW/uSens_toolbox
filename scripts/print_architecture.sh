IMAGE_SIZE_W=288
IMAGE_SIZE_H=160
/home/usens/tensorflow/tensorflow/contrib/lite/toco:toco -- \
  --input_format=TENSORFLOW_GRAPHDEF \
  --input_file=colorgesture.pb \
  --output_format=GRAPHVIZ_DOT \
  --output_file=colorgesture.quantized.dot \
  --inference_type=QUANTIZED_UINT8 \
  --input_shape=1,${IMAGE_SIZE_W},${IMAGE_SIZE_H},3 \
  --input_array=input \
  --output_array=output \
  --mean_value=128 \
  --std_value=127\
