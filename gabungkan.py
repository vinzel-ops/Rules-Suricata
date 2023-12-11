import os
import sys
import getopt

def merge_rules_files(output_path):
    """
    Menggabungkan semua file .rules ke dalam satu file output.

    :param output_path: Path lokasi file output yang digabungkan.
    """
    rules_files = []
    # Menelusuri direktori saat ini dan subdirektori untuk file .rules
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".rules"):
                rules_files.append(os.path.join(root, file))

    # Menggabungkan isi dari semua file .rules
    merged_content = ''
    for filename in rules_files:
        with open(filename, 'r') as f:
            merged_content += f.read() + '\n'

    # Menulis isi gabungan ke file output
    with open(output_path, 'w') as f:
        f.write(merged_content)

    print(f"Successfully merged {len(rules_files)} rules files into {output_path}")

def main(argv):
    """
    Fungsi utama yang menguraikan argumen baris perintah dan memanggil merge_rules_files.
    
    :param argv: Argumen baris perintah.
    """
    try:
        # Menguraikan argumen baris perintah
        opts, args = getopt.getopt(argv, "hp:", ["path="])
    except getopt.GetoptError as err:
        # Menampilkan pesan error dan instruksi penggunaan jika ada kesalahan argumen
        print(err)
        print('Usage: gabungkan.py -p <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('Usage: gabungkan.py -p <outputfile>')
            sys.exit()
        elif opt in ("-p", "--path"):
            path = arg
            merge_rules_files(path)
            break
    else:
        # Menampilkan instruksi penggunaan jika tidak ada argumen yang diberikan
        print('Usage: gabungkan.py -p <outputfile>')
        sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])
