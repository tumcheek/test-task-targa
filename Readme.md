# Test task

## Instruction for running
### Backend
1. Navigate to the app directory:
    ```
    cd app
    ```

2. Create a virtual environment:
    ```
    python -m venv venv
    ```

3. Activate the virtual environment (for Windows):
    ```
    venv\Scripts\activate
    ```

4. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

5. Run the server using uvicorn:
    ```
    uvicorn api:app --reload
    ```
   
### Frontend
1. Navigate to the frontend directory:
```
cd frontend
```
2. Install the required dependencies:
```
nmp install
```
3. Run frontend server:
```
nmp run dev
```