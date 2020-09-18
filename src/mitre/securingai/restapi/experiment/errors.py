from flask_restx import Api


class ExperimentAlreadyExistsError(Exception):
    pass


class ExperimentMLFlowTrackingAlreadyExistsError(Exception):
    pass


class ExperimentDoesNotExistError(Exception):
    pass


class ExperimentMLFlowTrackingDoesNotExistError(Exception):
    pass


class ExperimentMLFlowTrackingRegistrationError(Exception):
    pass


class ExperimentRegistrationError(Exception):
    pass


def register_error_handlers(api: Api) -> None:
    @api.errorhandler(ExperimentDoesNotExistError)
    def handle_experiment_does_not_exist_error(error):
        return {"message": "Not Found - The requested experiment does not exist"}, 404

    @api.errorhandler(ExperimentAlreadyExistsError)
    def handle_experiment_already_exists_error(error):
        return (
            {
                "message": "Bad Request - The experiment name on the registration form "
                "already exists. Please select another and resubmit."
            },
            400,
        )

    @api.errorhandler(ExperimentMLFlowTrackingAlreadyExistsError)
    def handle_experiment_already_exists_error(error):
        return (
            {
                "message": "Bad Request - The experiment name on the registration form "
                "already exists on the MLFlow Tracking backend. Please select another "
                "and resubmit."
            },
            400,
        )

    @api.errorhandler(ExperimentMLFlowTrackingDoesNotExistError)
    def handle_experiment_already_exists_error(error):
        return (
            {
                "message": "Bad Gateway - The requested experiment exists in "
                "our database but cannot be found on the MLFlow Tracking backend. "
                "If this happens more than once, please file a bug report."
            },
            502,
        )

    @api.errorhandler(ExperimentMLFlowTrackingRegistrationError)
    def handle_experiment_registration_error(error):
        return (
            {
                "message": "Bad Gateway - Experiment registration to the MLFlow "
                "Tracking backend experiment has failed. If this happens more "
                "than once, please file a bug report."
            },
            502,
        )

    @api.errorhandler(ExperimentRegistrationError)
    def handle_experiment_registration_error(error):
        return (
            {
                "message": "Bad Request - The experiment registration form contains "
                "invalid parameters. Please verify and resubmit."
            },
            400,
        )