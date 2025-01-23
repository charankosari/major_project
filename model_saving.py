import tensorflow as tf

# Load the SavedModel format
model = tf.keras.models.load_model('mp_hand_gesture')  # Ensure this path points to your SavedModel directory

# Save the model in .h5 format
model.save('mp_hand_gesture.h5')