from src.DataScienceProject.components.data_transformation import DataTransformation
from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject import logger

from pathlib import Path

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation_pipeline(self):

        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("Your data schema is not correct")
        except Exception as e:
            raise e