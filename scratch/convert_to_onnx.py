import os
import tensorflow as tf
import tf2onnx

# Paths
model_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'models')
h5_path = os.path.join(model_dir, 'cnn_lstm_model.h5')
onnx_path = os.path.join(model_dir, 'cnn_lstm_model.onnx')

print(f"Loading Keras model from {h5_path}...")
model = tf.keras.models.load_model(h5_path)

print("Converting model to ONNX format...")
# Define input signature based on model's input shape
spec = (tf.TensorSpec(model.inputs[0].shape, model.inputs[0].dtype, name="input_1"),)

# Convert Keras model to ONNX
model_proto, _ = tf2onnx.convert.from_keras(model, input_signature=spec, opset=13)

# Save the ONNX model
print(f"Saving ONNX model to {onnx_path}...")
with open(onnx_path, "wb") as f:
    f.write(model_proto.SerializeToString())

print("Model converted successfully!")
