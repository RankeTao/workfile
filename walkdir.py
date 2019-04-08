import pathlib
import os


def handle_csv(basepath):
    csvFilePathes = []
    csv2image_names = []
    entries = os.listdir(basepath)
    for entry in entries:
        if '.csv' in entry:
            filename = os.path.join(basepath, entry)
            csvFilePathes.append(filename)
            csv2image_names.append(entry[:-4]+'.bmp')
        else:
            pass
    return csvFilePathes, csv2image_names
if __name__ == '__main__':
    basefile = 'E:/colordetectanalysis/'
    csvfiles, csv2images = handle_csv(basefile)
    print(csvfiles)
    print(csv2images)



