import logging
import sys
import traceback

class PipelineLogger:
    def __init__(self, log_file=None, logger_name="PipelineLogger"):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        handlers = []
        # Console handler
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        handlers.append(ch)

        # File handler (optional)
        if log_file:
            fh = logging.FileHandler(log_file)
            fh.setLevel(logging.INFO)
            fh.setFormatter(formatter)
            handlers.append(fh)

        # Avoid duplicate handlers
        if not self.logger.hasHandlers():
            for handler in handlers:
                self.logger.addHandler(handler)

    def log_start(self, step_name):
        self.logger.info(f"Step '{step_name}' started.")

    def log_success(self, step_name):
        self.logger.info(f"Step '{step_name}' completed successfully.")

    def log_failure(self, step_name, exc=None):
        self.logger.error(f"Step '{step_name}' failed: {exc}")
        if exc:
            tb_str = traceback.format_exc()
            self.logger.error(f"Traceback:\n{tb_str}")

    def log_message(self, message, level=logging.INFO):
        self.logger.log(level, message)
