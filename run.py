"""
Running the Xetra ETL application
"""

import logging
import logging.config
import yaml


def main():
    """
    Entrypoint to run the xetra ETL job
    """

    # Parse YAML file
    config_path = '/Users/shannonnewn/ETL_Course/xetra_project_repo/configs/xetra_report_config.yml'
    config = yaml.safe_load(open(config_path))

    # Configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("This is a test.")


if __name__ == '__main__':
    main()
