from airflow.models.baseoperator import BaseOperator

class Notifications(BaseOperator):
    def __init__(self, msg:str,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg = msg
    
    def send_message(self, context):
        print(f'Esta es una notificacion: {self.msg} {{ds}}')