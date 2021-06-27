import os, datetime
import logging


class Log(object):

    @classmethod
    def check_log_directory_exists(cls, base_dir):
        log_file_dir = base_dir + "/log_files"
        if not os.path.isdir(log_file_dir):
            os.mkdir(log_file_dir)
    

    @classmethod
    def check_log_file_exists(cls, file_name):
        """file_name is file absolute path"""
        if not os.path.isfile(file_name):
            open(file_name, 'w').close()
    
    @classmethod
    def get_current_date_in_str(cls):
        today = datetime.date.today()
        return today.strftime("%d-%m-%y")
    
    @classmethod
    def get_current_date_time_in_str(cls):
        current = datetime.datetime.now()
        return str(current)

    @classmethod
    def add_text_to_log(cls, text, file_path):
        f = open(file_path, "a")
        f.write(text)
        f.close()


    @classmethod
    def log_handler(cls, log_text, text_type):
        """
        log_text: String
        text_type: String (Ex: error,)
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir_parent = os.path.abspath(os.path.join(base_dir, os.pardir))
        cls.check_log_directory_exists(base_dir_parent)
        file_path =  base_dir_parent + "/log_files/" + cls.get_current_date_in_str() + "-" + text_type.lower() + ".log"
        cls.check_log_file_exists(file_path)

        log_text = cls.get_current_date_time_in_str() + "   " + log_text

        cls.add_text_to_log("{0}\n".format(log_text), file_path)

        
    @classmethod
    def info(cls, log_text, request):
        text = '{} --> IP: {}| URL: {}'.format(log_text, request.META['REMOTE_ADDR'], request.path)
        cls.log_handler(text, "info")
    
    @classmethod
    def debug(cls, log_text, request):
        text = '{} --> IP: {}| URL: {}'.format(log_text, request.META['REMOTE_ADDR'], request.path)
        cls.log_handler(text, "debug")
    
    @classmethod
    def critical(cls, log_text, request):
        text = '{} --> IP: {}| URL: {}'.format(log_text, request.META['REMOTE_ADDR'], request.path)
        cls.log_handler(text, "critical")
    
    @classmethod
    def error(cls, log_text, request):
        text = '{} --> IP: {}| URL: {}'.format(log_text, request.META['REMOTE_ADDR'], request.path)
        cls.log_handler(text, "error")

    @classmethod
    def general_log(cls, log_text, log_type):
        text = str(log_text)
        cls.log_handler(text, log_type)