export TENSORFLOW_DIR='/home/usens/tensorflow'
export TRAIN_DIR='/home/usens/tensorflow/train_dir'
export NETWORK_NAME='ssdlite'
export OUTPUT_NODES='concat_1'
export IMAGE_SIZE_W=288
export IMAGE_SIZE_H=160

(cd ${TENSORFLOW_DIR}; bazel run -c opt //tensorflow/contrib/lite/toco:toco -- \
  --input_format=TENSORFLOW_GRAPHDEF \
  --input_file=${TRAIN_DIR}/${NETWORK_NAME}_frozen_graph.pb \
  --output_format=GRAPHVIZ_DOT \
  --output_file=${TRAIN_DIR}/${NETWORK_NAME}.quantized.dot \
  --inference_type=FLOAT \
  --input_shape=1,${IMAGE_SIZE_W},${IMAGE_SIZE_H},3 \
  --input_array=input \
  --output_array=${OUTPUT_NODES} \
  --mean_value=128 \
  --std_value=127\
)
dot -Tpdf -O ${TRAIN_DIR}/${NETWORK_NAME}.quantized.dot 
echo "** Generated PDF of graph: ${TRAIN_DIR}/${NETWORK_NAME}.quantized.dot.pdf"

