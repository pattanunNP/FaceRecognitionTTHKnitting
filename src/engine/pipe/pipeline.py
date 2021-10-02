from collections import defaultdict
from itertools import islice
from joblib import Parallel
from tabulate import tabulate
from optparse import OptionParser
import inspect
from app.utils.message import message

class Pipeline:

    def __init__(self, steps, memory=None,  verbose=1):

        print("\nInitialize pipeline ... \n ")

        """
        
        Parameters
        ----------
        steps : dict

            List of {name, transformFunction} dicts (implementing fit) that are
            chained, in the order in which they are chained, with the last object
            an estimator.


        verbose : int, defualt = 1

            logging level `-1, 0, 1`

           -1 : Not print any logging 
            0 : Print imaportant logging
            1 : Print All loggin everything


        Attributes
        ----------
        named_steps : :class:`~sklearn.utils.Bunch`
            Dictionary-like object, with the following attributes.
            Read-only attribute to access any step parameter by user given name.
            Keys are step names and values are steps parameters.

        
        Examples
        --------
        >>> from app.service.model.FaceExtactor import FaceExtactor

        >>> from app.service.model.FaceLocalizer import FaceLocalizer

        >>> from app.data.Dataset import Dataset

        >>> from app.pipeline.pipeline import Pipeline


        >>> FaceExtactor = FaceExtactor()

        >>> FaceLocalizer = FaceLocalizer()   

        >>> pipe = Pipeline([
                            {'LocalizeFace', FaceLocalizer.LocalizerFace()},
                            {'FaceExtactor', FaceExtactor.exactFeature()}])

        >>> # The pipeline can be used as any other estimator
        >>> # and avoids leaking the test set into the train set

        >>> pipe.fit(X_train)
        Pipeline([
                            {'LocalizeFace', FaceLocalizer.LocalizerFace()},
                            {'FaceExtactor', FaceExtactor.exactFeature()}])

        >>> pipe.result()
        
        """
        
        self.steps = steps

        self.verbose  = verbose

        self.table = []

        for idx, item in enumerate(self.steps):
            
            self.table.append(["Step: {} {} ".format(idx+1, item)])

        print(tabulate(self.table))


    def _log_message(self, step_name):
        return f"{step_name}"
        


    def fit(self, data):
        result = {}
        assert type(data) == tuple
        for trans in self.steps:   
            method_list = inspect.getmembers(self.steps[trans], predicate=inspect.ismethod)
            for name in method_list:
                if name[0] != "__init__":
                    val = name[1](data[0])
                    result[name[0]] = val
                    
        return result

        



        


        