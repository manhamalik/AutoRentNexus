def merge_and_move_folders(src1, src2, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)

    existing_hashes = set()

    for src in [src1, src2]:
        for root, dirs, files in os.walk(src):
            for file in files:
                src_file = os.path.join(root, file)
                file_md5 = file_hash(src_file)

                if file_md5 in existing_hashes:
                    continue  # Skip duplicate
                existing_hashes.add(file_md5)

                dst_file = os.path.join(dst, file)

                # Handle naming conflicts
                if os.path.exists(dst_file):
                    base, extension = os.path.splitext(dst_file)
                    i = 1
                    new_dst_file = f"{base}_{i}{extension}"
                    while os.path.exists(new_dst_file):
                        i += 1
                        new_dst_file = f"{base}_{i}{extension}"
                    dst_file = new_dst_file

                shutil.move(src_file, dst_file)

        # Remove empty source directories
        if os.path.exists(src):
            shutil.rmtree(src)
