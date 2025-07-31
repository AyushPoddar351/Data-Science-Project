from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.components.data_validation import DataValidation
from src.DataScienceProject import logger

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation_pipeline(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()