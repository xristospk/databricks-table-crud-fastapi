# databricks-table-crud-fastapi
- This demo application demonstrates an implementation for CRUD operations on a databricks table via a REST Api.
- It is implemented with [FastAPI](https://fastapi.tiangolo.com/) and [SQLAlchemy](https://fastapi.tiangolo.com/tutorial/sql-databases/)
- [databricks-dbapi](https://flynn.gg/blog/databricks-sqlalchemy-dialect/) adds support for a databricks dialect for SQLAlchemy
- FastAPI automatically comes with an [Interactive API documentation and exploration web user interfaces (SwaggerUI)](https://fastapi.tiangolo.com/features/) and [validation](https://fastapi.tiangolo.com/features/#validation) (via Pydantic) through class definitions

## Databricks preperation
- First you need to initialize the databricks database + table and retrieve the connection information of your databricks instance for the connection string
- There is demo data [crudapidata.csv](https://github.com/xristospk/databricks-table-crud-fastapi/blob/master/crudapidata.csv) and a databricks notebook [databricks-crud-api-setup.py](https://github.com/xristospk/databricks-table-crud-fastapi/blob/master/databricks-crud-api-setup.py) to create and load the databricks table in the repo
- Start your cluster
- Create (and load) data in the customer table with the notebook
- [Create a personal access token](https://docs.databricks.com/dev-tools/api/latest/authentication.html#:~:text=Generate%20a%20personal%20access%20token,-This%20section%20describes&text=in%20the%20upper%20right%20corner,the%20Generate%20New%20Token%20button.) (PAT)
- [Retrieve the databricks cluster http-path for the connection string](https://docs.databricks.com/integrations/bi/jdbc-odbc-bi.html#get-server-hostname-port-http-path-and-jdbc-url) 


## Run FastAPI application
### Configuration
- Create a '.env' configuration file in the root directory (where the README.md is located)
- Paste the content of the '.env.example' file in the root directory into '.env' 

```
. \databricks-table-crud-flask-api
├── \sql_app
├── .env            < new File
├── .env.example
├── main.py
└── ...
```

- Adjust the parameters (Access Token, HttpPath) and save the '.env' file

> .env
> ```
> DB_ACCESS_TOKEN=your-databricks-personal-access-token-here
> DB_DATABASE=crudapidb
> DB_HTTP_PATH=your-databricks-httpath-here
> ```

### If you already have another/newer Python version <> v3.7 installed:
- Download installer from https://www.python.org/downloads/release/python-379/
- Install without the option 'Add to path'
- Execute the following commands:

> C:\source\databricks-table-crud-fastapi> `pip install virtualenv`  
> C:\source\databricks-table-crud-fastapi> `virtualenv venv -p C:\Users\EMEAID\AppData\Local\Programs\Python\Python37\python.exe`  
> C:\source\databricks-table-crud-fastapi> `.\venv\Scripts\activate.ps1`  
> `(venv)` C:\source\databricks-table-crud-fastapi> `pip install https://download.lfd.uci.edu/pythonlibs/q4trcu4l/sasl-0.2.1-cp37-cp37m-win_amd64.whl`  
> `(venv)` C:\source\databricks-table-crud-fastapi> `pip install -r requirements.txt`  
> `(venv)` C:\source\databricks-table-crud-fastapi> `uvicorn main:app --reload`  


### If you only have Python Version 3.7 installed:
- Execute the following commands:
> C:\source\databricks-table-crud-fastapi> `python -m venv venv`  
> C:\source\databricks-table-crud-fastapi> `.\venv\Scripts\activate.ps1`  
> `(venv)` C:\source\databricks-table-crud-fastapi> `pip install https://download.lfd.uci.edu/pythonlibs/q4trcu4l/sasl-0.2.1-cp37-cp37m-win_amd64.whl`  
> `(venv)` C:\source\databricks-table-crud-fastapi> `pip install -r requirements.txt `  
> `(venv)` C:\source\databricks-table-crud-fastapi> `uvicorn main:app --reload  `  
  
Navigate to http://127.0.0.1:8000/docs  
Have fun creating, reading, updating and deleting records of the databricks delta table 'customers' :)

## Miscellaneous

### Debugging FastAPI:
- Do not run it with `uvicorn main:app --reload` 
- Instead follow this instructions: https://fastapi.tiangolo.com/tutorial/debugging/

### Deployment to Azure App Service
- Under Settings > Configuration > General settings set the Startup Command to `startup.sh` (which is found in the root directory)
- See [Configure a custom startup file for Python apps on Azure App Service](https://docs.microsoft.com/en-us/azure/developer/python/tutorial-deploy-app-service-on-linux-04)

<br>
<br>
Made with 🧠 by Cloud Analytics <br>

**Mit freundlichem Gruß / Kind Regards / #MFGTSS**

<img src="https://cdn.worldvectorlogo.com/logos/linktree-2.svg" alt="drawing" width="20"/>  [xristospk](https://www.linktr.ee/xristospk)

<img src="https://user-images.githubusercontent.com/26623619/135774582-194d8c26-47de-455f-9746-98a06dd0e509.png" alt="drawing" width="20"/>  [Patrick Krybus](https://www.xing.com/profile/PatrickXristos_Krybus)

<img src="https://user-images.githubusercontent.com/26623619/135774544-e9215840-e364-4386-b409-180c12ade8c3.png" alt="drawing" width="20"/>  [kbs.xrs](http://instagram.com/kbs.xrs/)

<img src="https://user-images.githubusercontent.com/26623619/135774679-778a23f7-3959-4d31-aa3f-dc6b98778495.png" alt="drawing" width="20"/>  [XYPK](https://www.facebook.com/patrick.krybus) 
