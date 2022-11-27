from airflow.models.baseoperator import BaseOperator

class Notifications(BaseOperator):
    def __init__(self, mensaje:str,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mensaje = mensaje
    
    def execute(self, context):
        print(f'Esta es una notificacion: {self.mensaje}')