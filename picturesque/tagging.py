from imageai.Prediction import ImagePrediction
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

execution_path = os.getcwd()
prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(execution_path + "/resnet50_weights_tf_dim_ordering_tf_kernels.h5")
prediction.loadModel()


def tag_image(filepath):
    predictions, percentage_probabilities = prediction.predictImage(filepath, result_count=1)
    return predictions[0]
