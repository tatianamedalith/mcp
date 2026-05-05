import pythoncom
import win32com.client


def create_task(params: dict, config: dict) -> dict:
    pythoncom.CoInitialize()
    
    try:
        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect()
        
        task_def = scheduler.NewTask(0)
        task_def.Settings.Enabled = True
        trigger = task_def.Triggers.Create(2)  # 1 for daily trigger
        trigger.StartBoundary = f"2026-05-05T{params['trigger_time']}:00"
        trigger.Enabled = True
        
        action = task_def.Actions.Create(0)  # 0 for executing a program
        action.Path = config['task_manager']["python_path"]
        action.Arguments = params['script_path']
        
        scheduler.GetFolder("\\").RegisterTaskDefinition(
            params['task_name'],
            task_def,
            6,
            None,
            None,
            0
        )
        return {"status": "created", "task_name": params["task_name"]}
    finally:
        pythoncom.CoUninitialize()
        
def list_task()-> dict:
    pythoncom.CoInitialize()
    
    try:
        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect()
        
        tasks = scheduler.GetFolder("\\").GetTasks(0)
        
        return {"tasks": [{"name": t.Name, "state": t.State} for t in tasks]}
    finally:
        pythoncom.CoUninitialize()      
        
def delete_task(params: dict) -> dict:
    pythoncom.CoInitialize()
    
    try:
        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect()
        
        scheduler.GetFolder("\\").DeleteTask(params["task_name"], 0)
        return {"status": "deleted", "task_name": params["task_name"]}
    finally:
        pythoncom.CoUninitialize()          