from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from config import ROOT
from schemas import DirectoryInfo, DirectoryCreation, FileCreation, FileUpdate
from utils import get_metadata, get_file_by_path, get_directory_by_path, search_directory, find_directory_by_path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get('/root/')
async def browse_in_file_system(path: str = None, is_file: bool = False):
    if is_file:
        return get_file_by_path(path)
    if path:
        return get_directory_by_path(path)
    return DirectoryInfo(
        path='',
        files=list(map(get_metadata, ROOT.files.values())),
        directories=list(map(get_metadata, ROOT.directories.values()))
    )


@app.post('/directories/')
async def create_directory(directory_name: DirectoryCreation, path: str = None) -> DirectoryInfo:
    directory = find_directory_by_path(path, ROOT) if path else ROOT
    if directory is None:
        raise HTTPException(status_code=404, detail=f'Directory with path {path} not found')
    try:
        directory.create_directory(directory_name.name)
    except KeyError:
        raise HTTPException(status_code=404, detail=f'Directory with {directory_name} already exist')
    return DirectoryInfo(
        path=path if path else '',
        files=list(map(get_metadata, directory.files.values())),
        directories=list(map(get_metadata, directory.directories.values()))
    )


@app.delete('/directories/{name}')
async def delete_directory(name: str, path: str = None) -> DirectoryInfo:
    directory = find_directory_by_path(path, ROOT) if path else ROOT
    if directory is None:
        raise HTTPException(status_code=404, detail=f'Directory with path {path} not found')
    try:
        directory.remove_directory(name)
    except KeyError:
        raise HTTPException(status_code=404, detail=f'Directory with name {name} not found')
    return DirectoryInfo(
        path=path if path else '',
        files=list(map(get_metadata, directory.files.values())),
        directories=list(map(get_metadata, directory.directories.values()))
    )


@app.post('/files/')
async def create_file(file_info: FileCreation, path: str = None) -> DirectoryInfo:
    directory = find_directory_by_path(path, ROOT) if path else ROOT
    if directory is None:
        raise HTTPException(status_code=404, detail=f'Directory with path {path} not found')
    directory.create_file(file_info.name, file_info.content)
    return DirectoryInfo(
        path=path if path else '',
        files=list(map(get_metadata, directory.files.values())),
        directories=list(map(get_metadata, directory.directories.values()))
    )


@app.delete('/files/{name}')
async def delete_file(name: str, path: str = None) -> DirectoryInfo:
    directory = find_directory_by_path(path, ROOT) if path else ROOT
    if directory is None:
        raise HTTPException(status_code=404, detail=f'Directory with path {path} not found')
    try:
        directory.delete_file(name)
    except KeyError:
        raise HTTPException(status_code=404, detail=f'File not found: {name}')
    return DirectoryInfo(
        path=path if path else '',
        files=list(map(get_metadata, directory.files.values())),
        directories=list(map(get_metadata, directory.directories.values()))
    )


@app.put('/files/{name}')
async def delete_file(content: FileUpdate,name: str, path: str = None) -> DirectoryInfo:
    directory = find_directory_by_path(path, ROOT) if path else ROOT
    if directory is None:
        raise HTTPException(status_code=404, detail=f'Directory with path {path} not found')
    try:
        directory.update_file(name, content.content)
    except KeyError:
        raise HTTPException(status_code=404, detail=f'File not found: {name}')
    return DirectoryInfo(
        path=path if path else '',
        files=list(map(get_metadata, directory.files.values())),
        directories=list(map(get_metadata, directory.directories.values()))
    )


@app.get('/search/{name}')
async def search_in_file_system(name: str, is_file: bool = False) -> dict:
    directory = search_directory(ROOT, name)
    if directory is None:
        raise HTTPException(status_code=404, detail=f'Directory or file with name {name} not found')
    return directory
