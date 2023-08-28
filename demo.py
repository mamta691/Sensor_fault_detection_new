from sensor.components.data_ingestion import DataIngestion
from sensor.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig, DataTransformationConfig,ModelTrainerConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.components.data_validation import DataValidation
from sensor.components.data_transformation import DataTransformation
from sensor.components.model_trainer import ModelTrainer


data_ingestion = DataIngestion(data_ingestion_config=DataIngestionConfig(TrainingPipelineConfig()))
data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()

data_validation = DataValidation(DataValidationConfig(TrainingPipelineConfig()), data_ingestion_artifacts)
data_validation_artifacts = data_validation.initiate_data_validation()

data_transformation = DataTransformation(DataTransformationConfig(TrainingPipelineConfig()), data_validation_artifacts)
data_transformation_artifacts = data_transformation.initiate_data_transformation()


model_trainer=ModelTrainer(ModelTrainerConfig(TrainingPipelineConfig()),data_transformation_artifacts)
model_trainer_artifact=model_trainer.initiate_model_trainer()
