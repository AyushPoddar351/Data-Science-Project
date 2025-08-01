from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.components.model_evaluation import ModelEvaluation
from src.DataScienceProject import logger

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation_pipeline(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()