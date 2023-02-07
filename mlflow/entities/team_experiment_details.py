from mlflow.entities._mlflow_object import _MLflowObject
from mlflow.protos.service_pb2 import TeamExperimentDetails as ProtoTeamExperimentDetails


class TeamExperimentDetails(_MLflowObject):
    """
     TeamExperimentDetails object
     """

    def __init__(self, id, team_id, experiment_id):
        super().__init__()
        self._id = id
        self._team_id = team_id
        self._experiment_id = experiment_id

    @property
    def id(self):
        """String ID of the team experiment map."""
        return self._id

    @property
    def team_id(self):
        """String team_id representing the team to which the experiment belongs."""
        return self._team_id

    @property
    def experiment_id(self):
        """String experiment_id of the team experiment map."""
        return self._experiment_id

    @classmethod
    def from_proto(cls, proto):
        team_experiment_details = cls(
            proto.id,
            proto.team_id,
            proto.experiment_id
        )
        return team_experiment_details

    def to_proto(self):
        team_experiment_details = ProtoTeamExperimentDetails()
        team_experiment_details.id = self.id
        team_experiment_details.team_id = self.team_id
        team_experiment_details.experiment_id = self.experiment_id
        return team_experiment_details
