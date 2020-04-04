import logbook

class Logger:
    def __init__( self):

        # For logging to the console:
        # logbook.StreamHandler(sys.stdout).push_application()
        
        logbook.FileHandler('application.log').push_application()
        logger = logbook.Logger(__name__)
        logbook.set_datetime_format('local')

    def log_info(self, info_message):
        logbook.info(info_message)
    
    def log_debug(self, debug_message):
        logbook.debug(debug_message)
    
    def log_warning(self, warning_message):
        logbook.warning(warning_message)
    
    def log_error(self, error_massage):
        logbook.error(error_massage)
    
    def log_critical(self, critical_message):
        logbook.critical(critical_message)