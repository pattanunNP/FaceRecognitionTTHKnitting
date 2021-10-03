"""
__author__ = "pattanunNP"
__version__ = "0.1.0"
__license__ = "MIT"

"""


import argparse
import logging
import colorlog

parser = argparse.ArgumentParser(description='Face Recogition Engine')


parser.add_argument('-v', '--version',
                    action='version',
                    version='%(prog)s 1.0.0a',
                    help="Show program's version number and exit.")

parser.add_argument('-d', '--directory',
                    help="image source path",
                    type=str)

parser.add_argument('-o', '--output',
                    help="Output Path",
                    type=str)

parser.add_argument('-m', '--model',
                    help="select model [spotify-annoy/faiss]",
                    choices=['spotify', 'faiss'])

parser.add_argument('-l', '--loglevel',
                    help=(
                        "Provide logging level. "
                        "Example --log debug', default='warning'"),

                    dest="loglevel",
                    choices=['debug', 'info', 'warn', 'error', 'critical'],
                    default="info",
                    type=str)

parser.add_argument('--log-file',
                    help="File to write log to",
                    default="run.log")


# system('clear')


args = parser.parse_args()

levels = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARNING,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG
}
level = levels.get(args.loglevel.lower())

if level is None:
    raise ValueError(
        f"log level given: {args.loglevel}"
        f" -- must be one of: {' | '.join(levels.keys())}")

logging.basicConfig(filename=args.log_file,
                    level=level,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class FaceRecognition:

    def __init__(self):

        logging.debug('Started Process')
        logging.info('Started Process')


#     def processImage(self, i, image, total):
#         return self.pipe.fit(image)


#     def run(self, loader, workers="logic"):


#         if workers <= self.n_logicCores:
#             workers = workers
#             message.SuccessPrint(f"Using {workers} Cores ")
#         else:
#             workers = self.n_logicCores
#             message.SuccessPrint(f"Using Maximum : {workers} Cores ")

#         out = Parallel(n_jobs=workers, backend="threading",verbose=2)(
#             delayed(self.processImage)(i, image,total=len(loader)) for i, image in tqdm(enumerate(loader), total=len(loader))
#         )
#         for i, obj in enumerate(out):
#             self.obj[i] = obj
#         return self.obj


#     def train(self, dataobj):
#         n = len(dataobj)
#         nb = int(1e7)
#         d = 512
#         i = 1
#         for img_id in dataobj:
#             # print()

#             if i ==1:
#                 out = dataobj[img_id]['extractFeature']
#                 i+=1
#             else:
#                 try:
#                     train_data = dataobj[img_id]['extractFeature']
#                     out = np.vstack([out, train_data])
#                 except:
#                     pass

#         print(out.shape)
#         xb = np.random.random((nb, d)).astype('float32')
#         self.FaceSearch.train(xb,database_path="../out/face.index")


# if __name__ == '__main__':
#     main = Main()
#     datagen = Dataset.create_json(root="../Runner/")
#     # res = main.run(datagen,workers=8)
#     # # print(res)
#     # main.train(res)
#     # # print(res)
