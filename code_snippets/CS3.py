def extract_features(name, sample, dataset, sample_count, feature_shape, base_model, preprocess_input):
    features_path = f"/content/drive/MyDrive/Brain_Tumour_AI/{name}/feature_extraction/{sample}_features.npy"
    labels_path = f"/content/drive/MyDrive/Brain_Tumour_AI/{name}/feature_extraction/{sample}_labels.npy"

    # Check if features already exist
    if os.path.exists(features_path) and os.path.exists(labels_path):
        print(f"Features already exist, loading.")
        features = np.load(features_path)
        labels = np.load(labels_path)
        return features, labels

    # Initialize arrays
    features = np.zeros((sample_count, *feature_shape))
    labels = np.zeros((sample_count,))

    i = 0
    for images_batch, labels_batch in dataset:
        features_batch = base_model.predict(images_batch)
        features[i * batch_size : i * batch_size + len(images_batch)] = features_batch[:len(images_batch)]
        labels[i * batch_size : i * batch_size + len(labels_batch)] = labels_batch[:len(labels_batch)]
        i += 1
        if i * batch_size >= sample_count:
            break

    # Save features and labels
    np.save(features_path, features)
    np.save(labels_path, labels)
    return features, labels
