import csv
import json

from datetime import datetime

import luigi

class GetRawData(luigi.Task):
    time_interval = luigi.Parameter(default=interval_default())
    clear_old_temp_data = luigi.BoolParameter()
    auth_info = dict(config.items('Facebook Authentication'))

    def run(self):
        print("Getting Facebook Ad Stats {0}...".format(self.time_interval))
        fb_service = FacebookService(data_fields, self.time_interval, self.auth_info, DIRS['raw_local_dir'])
        with self.output().open('w') as output:
            if self.clear_old_temp_data:
                LFS.clear_dir(fb_service.temp_dir)
            fb_service.download_day_by_day()
            LFS.merge_json_files(fb_service.temp_dir, fb_service.all_report_names, output)


    def output(self):
        raw_local_path = get_path(DIRS['raw_local_dir'], requested_interval=self.time_interval, file_format='json')
        return luigi.LocalTarget(raw_local_path)

class SendRawFileToS3(luigi.Task):
    time_interval = luigi.Parameter(default=interval_default())
    s3_client = S3Client(luigi_config.get('s3', 'aws_access_key_id'), luigi_config.get('s3', 'aws_secret_access_key'))

    def requires(self):
        return GetRawData(time_interval=self.time_interval)

    def run(self):
        print('Sending Raw File to S3...')
        raw_local_path = get_path(DIRS['raw_local_dir'], requested_interval=self.time_interval, file_format='json')
        raw_s3_path = get_path(DIRS['raw_s3_dir'], requested_interval=self.time_interval, file_format='json')
        S3Client.put_multipart(self.s3_client, raw_local_path, raw_s3_path, 10000000)

    def output(self):
        raw_s3_path = get_path(DIRS['raw_s3_dir'], requested_interval=self.time_interval, file_format='json')
        return S3Target(raw_s3_path)

class ProcessData(luigi.Task):
    time_interval = luigi.Parameter(default=interval_default())
    skip_s3 = luigi.BoolParameter()

    def requires(self):
        required_tasks = [GetRawData(time_interval=self.time_interval)]
        if not self.skip_s3:
            required_tasks.append(SendRawFileToS3(time_interval=self.time_interval))
        return required_tasks

    def run(self):
        raw_local_path = get_path(DIRS['raw_local_dir'], requested_interval=self.time_interval, file_format='json')
        with open(raw_local_path, 'r') as raw_json, self.output().open('w') as output:
            print("Processing Facebook Ad Stats {0}...".format(self.time_interval))
            data = json.load(raw_json, object_pairs_hook=OrderedDict)
            data = FacebookService.parse_actions(data, action_types)
            headers = data_fields + [action_type.replace('offsite_conversion.', '') + 's' for action_type in action_types]
            writer = csv.DictWriter(output, headers)
            writer.writerows(data)

    def output(self):
        processed_local_path = get_path(DIRS['processed_local_dir'], requested_interval=self.time_interval, processed=True)
        return luigi.LocalTarget(processed_local_path)

class ZipData(luigi.Task):
    task_type = luigi.Parameter()
    report_date = luigi.Parameter()

    def requires(self):
        return ProcessData(task_type=self.task_type, report_date=self.report_date)

    def run(self):
        my_script.zip_files(input_file_names=self.input(), output_file_name=self.output())

    def output(self):
        return 'output_folder/{0}_{0}.zip'.format(self.task_type, self.report_date)

class SendFTP(luigi.Task):
    task_type = luigi.Parameter()
    report_date = luigi.Parameter()

    def requires(self):
        return ZipData(task_type=self.task_type, report_date=self.report_date)

    def run(self):
        my_script.send_over_ftp(self.input())

    def output(self):
        # check ftp success
        pass
