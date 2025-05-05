import tensorflow as tf

model = tf.keras.models.load_model('model_result\lane_navigation.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
open("model_result\lane_navigation.tflite", "wb").write(tflite_model)